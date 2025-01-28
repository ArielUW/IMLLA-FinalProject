import os
import pandas as pd

def duplicate_columns (dataset):
    dataset["target_sentence"] = dataset.loc[:,"source_sentence"]
    return dataset

def clean_examples(dataset):
    dataset = dataset.query('type'<2)
    return dataset


if __name__=="__main__":
    os.chdir("/Users/arieldrozd/Downloads/IMLLA-FinalProject/cleaned_examples")
    full_dataset = pd.DataFrame({"type":[],"source_sentence":[],"target_sentence":[]})
    for file in os.listdir("/Users/arieldrozd/Downloads/IMLLA-FinalProject/cleaned_examples"):
        if file.endswith("logopeda.csv"):
            print(file)
            dataset = pd.read_csv(file)
            dataset = clean_examples(dataset)
            dataset = duplicate_columns(dataset)
            dataset.join(full_dataset)
    full_dataset.to_csv(f"target_{file}")