# IMLLA-FinalProject
Repository for the final project for Introduction for Machine Learning for Linguistics Applications.

## Project proposal

Full description of the project is available on Google Docs: https://docs.google.com/document/d/1cfPv_zhlnV8oHgj630l0FwApVC4BhZqme6AO02B6pac

## Workflow documentation
1. Joint work: creation of reference tables with job titles (reference dictionary: resources)
2. Monika worked on type 1 examples from NKJP using tokenization – most of type 1 examples were annotated by her (referenece directory: examples_monika)
3. Ariel worked on some type 1 examples from NKJP using regexes and added type 0 examples: some of them were found in NKJP while cleaning type 1 examples, the rest was added from Wikipedia using scraper from week 7 and by copying and pasting short novels from WolneLektury into a txt file (referenece directories: raw_examples_ariel, cleaned_examples_ariel)
4. After making sure the examples properly coded (no job titles in type 0 examples!) and the proportions are correct, Ariel compiled the data into one dataset and pushed it to Hugging Face (reference directory: dataset, refernece repository: https://huggingface.co/datasets/ArielUW/jobtitles)
5. Monika trained the network and pushed it to Hugging Face (reference directory: training, reference repository: [to fill in])
6. Monika deployed the model on the test split and calculated binary evaluation metrics. i.e. Attempted noun neutralisation precision and Attempted noun neutralisation recall (reference directory: outputs and evaluation).
7. Ariel prepared the evaluation of metrics based on Levenstein's distance (reference directory: outputs and evaluation).

## Evaluation of the model

### Metrics:
– Normalized Levensthein's distance for type 1: [0.0395]
– Normalized Levensthein's distance for type 0: [0.0001]
Note: instead of using [edit_distance()] from NLTK library, [distance()] from Levenshtein library was used.
Both values are below the assumed maximum thershold value.

### Qualitative analysis

*U młodej dziewczyny osoba zajmująca się psychiatrią rozpoznała początki choroby psychicznej, dziewczyna myśli o samobójstwie.* ▶️ *U młodej dziewczyny osoba psychiaterska rozpoznała początki choroby psychicznej, dziewczyna myśli o samobójstwie.*

A lot of model's mistakes were related to case agreement and other morphosyntactical aspects beyond the scope of the project, eg:
– object-verb agreement: *Na razie jedynie weto Kwaśniewskiego może powstrzymać _pazerne osoby awuesiarskie_, którzy mnożąc urzędy rozbudowują dla siebie przechowalnię.* ▶️ *Na razie jedynie weto Kwaśniewskiego może powstrzymać _pazernych osób awuesiarskich_, którzy mnożąc urzędy rozbudowują dla siebie przechowalnię.*
– issues related to numerals: *_Cztery młode osoby żołnierskie_ w granatowych mundurach MSW mocno _zapukały_ do drzwi.* ▶️ *_Czterech młodych osób żołnierskich_ w granatowych mundurach MSW mocno _zapukało_ do drzwi.*
– subject-verb agreement: *Do pracy naukowej _wróciła_ również niedawna osoba liderska UP, RYSZARD BUGAJ.* ▶️ *Do pracy naukowej _wrócił_ również niedawna osoba liderska UP, RYSZARD BUGAJ.*

## Errors and shortcomings
1. Despite our best efforts, there were mistakes in the dataset: the reason for that is the fact that we didn't have enough resources to provide any proofreading. Standard practice would be to have at least two annotators and one superannnotator – in our case, every example was prepared by one annotator without proofreading.
* First, errors present in the training/validation splits may have contributed to worse-than-possible training results (model could come to "wrong conclusions" based on erroneous examples in training),
* Second, errors present in the test split have likely caused the output quality to be underreported (there are at least two cases where model was "more right" than the test data target, while it is very unlikely for the annotators to commit an error *exactly* the same as an error later commited by the model for *exactly* the same test example),
* However, the number of errors is not too big and can be easily remediated by having even one round of proofreading. Proofreading has not been performed before submitting this project, as at this state it would equate to falsifying documentation.
2. The dataset was not balanced the way it was intended to be (in terms of morphological variety of job titles), nor was it as homogenous as intended (there were semantic edge cases present, as well as a variety of cases instead of just singular nominative forms).
* This has made the task all the more complicated for the model, as there are more parameters influencing the quality of the output, such as possible mistakes concetning case endings, number agreement, recognizing edge cases etc.

## Conclusions

The results are very promising and much better than expected. The high quality of the initial outputs is especially surprising given the errors present in the dataset.

It is advisable to proofread the existing dataset [ArielUW/jobtitles], as well as to expand it with more examples tailored to adress:
– the most problematic morphological types of job titles
– morphosyntactic inticacies of subject-verb agreement, case and number agreement and co-reference.
After that the training process should be repeated for the base model, as the here presented fine-tuning was interfered with by the existence of errors in the dataset.