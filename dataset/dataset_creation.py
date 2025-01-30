import os
import pandas as pd
from huggingface_hub import HfApi, Repository
import shutil

def merge_and_sort(tables, output_files, output_folder, columns):
    frames = []
    for table in tables:
        try:
            frames.append(pd.read_csv(table, sep=";"))
            print(f"File '{table}' successfully prepared for merging.")
        except:
            try:
                frames.append(pd.read_csv(table, sep=","))
                print(f"File '{table}' successfully prepared for merging.")
            except:
                try:
                    frames.append(pd.read_csv(table, sep="\t"))
                    print(f"File '{table}' successfully prepared for merging.")
                except Exception as e:
                    print(f"Unable to merge file '{table}': {e}")
    full_df = pd.concat(frames).filter(items=columns,axis=1)
    zero = full_df.loc[(full_df['type'] == 0)]
    zero = zero.sample(frac = 1) # shuffling examples
    zero.to_csv(f"{output_folder}{output_files[0]}", index=False)
    one = full_df.loc[(full_df['type'] == 1)]
    one = one.sample(frac = 1) # shuffling examples
    one.to_csv(f"{output_folder}{output_files[1]}", index=False)

def validate_csv(file_path: str, columns):
    """
    Validates the structure of the CSV file to ensure it contains valid columns.
    """
    df = pd.read_csv(file_path, sep=',')
    required_columns = set(columns)
    if not required_columns.issubset(df.columns):
        raise ValueError(f"The TSV file must contain the following columns: {required_columns}")
    print(f"CSV file '{file_path}' is valid with {len(df)} rows.")

def create_splits(output_folder, output_files, dataset_name, dataset_structure):
    zero = pd.read_csv(f"{output_folder}{output_files[0]}")
    one = pd.read_csv(f"{output_folder}{output_files[1]}")
    for split, structure in dataset_structure.items():
        try:
            for key, value in structure.items():
                if key=="zero":
                    rows_zero = zero.iloc[:value]
                    zero.drop(rows_zero.index, inplace=True)
                elif key=="one":
                    rows_one = one.iloc[:value]
                    one.drop(rows_one.index, inplace=True)
                else:
                    print(f"Invalid key in dataset structure: {key} in f{split} part.")
            df = pd.concat([rows_zero, rows_one])
            df = df.sample(frac = 1) # shuffling examples
            print(df)
            df.to_csv(f"{output_folder}{dataset_name}{split}.csv", index=False)
            print(f"Created {split} split.")
        except Exception as e:
            print(f"Failure while creating the {split} splt: {e}")

def push_dataset_to_HF(file_path: str, repo_name: str, token: str, git_name: str, git_email: str):
    try:
        api = HfApi()
        # Specify repo_type="dataset" here
        repo_url = api.create_repo(
            repo_id=repo_name,
            token=token,
            exist_ok=True,
            repo_type="dataset"
        )

        repo_dir = f"./{repo_name}"
        if os.path.exists(repo_dir):
            shutil.rmtree(repo_dir)

        repo = Repository(
            local_dir=repo_dir,
            clone_from=repo_url,
            use_auth_token=token,
            git_user=git_name,
            git_email=git_email,
            repo_type="dataset"
        )

        dest_file_path = os.path.join(repo_dir, os.path.basename(file_path))
        shutil.copy2(file_path, dest_file_path)

        repo.git_add(pattern=".")
        repo.git_commit(f"Add dataset file: {os.path.basename(file_path)}")
        repo.git_push()
        print(f"Dataset '{file_path}' has been uploaded to {repo_url}")

    except Exception as e:
        print(f"Error occurred during upload: {str(e)}")
        raise

    # Make sure output directory exists
    output_dir="job_titles_dataset"
    os.makedirs(output_dir, exist_ok=True)

    # Initialize Hugging Face Hub API
    api = HfApi()
    repo_id = f"{user}/{repo_name}"
    
    # Create or update repository
    api.create_repo(repo_id=repo_id, exist_ok=True)

    # Push files to Hub
    api.upload_folder(
        folder_path=output_dir,
        repo_id=repo_id,
        commit_message=f""
    )
    print(f"Model pushed to: https://huggingface.co/{repo_id}")

if __name__=="__main__":
    os.chdir="/Users/arieldrozd/Downloads/IMLLA-FinalProject"
    tables = ["./examples_monika/final_table_together.csv", "./cleaned_examples_ariel/nkjp_ariel.csv", "./cleaned_examples_ariel/wikipedia.csv", "cleaned_examples_ariel/nowela.csv"]
    output_folder = "./dataset/"
    output_files = ["zero.csv", "one.csv"]
    dataset_name = "jobtitles/"
    columns=['type', 'source_sentence', 'target_sentence']
    merge_and_sort(tables, output_files, output_folder, columns)
    for file in output_files:
        validate_csv(f"{output_folder}{file}", columns)
    #test split -> zero: 250, one: 250
    #validation split -> zero: 500, one: 50
    #training split -> zero: 4221, one: 610 -> actually: all that is left
    dataset_structure = {"test":{"zero":250,"one":250}, "validation":{"zero":500,"one":50}, "train":{"zero":4221,"one":610}}
    final_dataset = create_splits(output_folder, output_files, dataset_name, dataset_structure)