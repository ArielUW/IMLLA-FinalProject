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
6. Monika deployed the model on the test split and calculated binary evaluation metrics. i.e.: Attempted noun neutralisation precision and Attempted noun neutralisation recall (reference directory: outputs and evaluation).
7. Ariel prepared the evaluation of metrics based on Levenstein's distance (reference directory: outputs and evaluation).
8. Alongside of other work, Ariel prepared the dataset's readme file and this readme, which was supplemented by Monika near the end, when she had obtained results of the evaluation.
9. Ariel and Monika filled in addtional details in the model card on Hugging Face.

## Evaluation of the model

### Metrics:
– Attempted noun neutralisation precision: []
– Attempted noun neutralisation recall: []
Both values are above the assumed minimum threshhold value (50%).

– Normalized Levensthein's distance for type 1: [0.0395]
– Normalized Levensthein's distance for type 0: [0.0001]
Both values are below the assumed maximum thershold value (0.04 and 0.02).
Note: instead of using [edit_distance()] from NLTK library, [distance()] from Levenshtein library was used.

* Only one out of 250 (0%) type 0 targets was different from the correct anwser.
Additionally, it was revealed that the mistake was caused by the appearance of a semantic edge case in type 0 subset, which should not be the case:
_Target in the test set:_ Oprócz wątka sakralnego, który towarzyszyć będzie *autorowi* przez całe życie, szczególnie bliskiego wielu tym, którzy, jak Paszkiewicz, w bardzo młodym wieku zetknęli się z tragedią obozów koncentracyjnych, upodleniem, rozpaczą, gwałtowną śmiercią lub jej przeciwieństwem - powolnym umieraniem z głodu i wycieńczenia, ujawnia się tu głęboko humanistyczny i humanitarny zarazem krzyk w obronie ""ginących w nicość i samotność"", próba uratowania ich od ostatecznego unicestwienia.
_Target generated by the model:_ Oprócz wątka sakralnego, który towarzyszyć będzie *osobie autorskiej* przez całe życie, szczególnie bliskiej wielu tym, którzy, jak Paszkiewicz, w bardzo młodym wieku zetknęli się z tragedią obozów koncentracyjnych, upodleniem, rozpaczą, gwałtowną śmiercią lub jej przeciwieństwem - powolnym umieraniem z głodu i wycieńczenia, ujawnia się tu głęboko humanistyczny i humanitarny zarazem krzyk w obronie ""ginących w nicość i samotność"", próba uratowania ich od ostatecznego unicestwienia.

* 133 out of 250 (53%) type 1 targets were non-identical to the gold-standard counterparts.
However, many of the non-identical tagets still contained valid attempts and neutralisation (as evidenced by high precision and the qualitative analysis). Oftentimes the differences were minor (as evidenced by low mean standardized Levensthein distances) and/or beyond the scope of the main interest of the study (as evidenced by high precision), or even fully attributable to mistakes in the dataset (as laid out in the qualitative analysis).

### Qualitative analysis of errors in type 1 examples

Examples are presentend in the following order: *target prepared by annotators* ▶️ *generated target*

1. There were some valid attempts at neutralising a job title that lead to incorrect results:
– parlamentarzysta: *_Osoba parlamentarzystyczna_ nie chce uczestniczyć w kluczowej dla współczesnej Europy debacie: jak budować poczucie obywatelskiej wspólnoty i wzajemnego zaufania w wielokulturowym świecie.* ▶️ *_Osoba parlamentarska_ nie chce uczestniczyć w kluczowej dla współczesnej Europy debacie: jak budować poczucie obywatelskiej wspólnoty i wzajemnego zaufania w wielokulturowym świecie.*
– psychiatra: *U młodej dziewczyny _osoba zajmująca się psychiatrią_ rozpoznała początki choroby psychicznej, dziewczyna myśli o samobójstwie.* ▶️ *U młodej dziewczyny _osoba psychiaterska_ rozpoznała początki choroby psychicznej, dziewczyna myśli o samobójstwie.*
– narrator: *Ten, kto dyktuje warunki, kto powołał _osobę narratorską_ i kto tak długo zostawiał bez odpowiedzi listy i faksy, przypomina sobie co jakiś czas o zaległych sprawach, poczynając od cieknącego kranu, a kończąc na bankowych dyspozycjach.* ▶️ *Osoba, która dyktuje warunki, kto powołał _osobę narraterską_ i kto tak długo zostawiał bez odpowiedzi listy i faksy, przypomina sobie co jakiś czas o zaległych sprawach, poczynając od cieknącego kranu, a kończąc na bankowych dyspozycjach.*
– operator: *Grochulski - wskazał rudego - też robi za siebie i _osobę operatorską_ radaru.,Grochulski - wskazał rudego - też robi za siebie i _osoby operaterskiej_ radaru.*
– pilot: *Załogę samolotu stanowią dwie _osoby pilockie_ i osoba inżynierska pokładowa oraz sześć osób obsługi pokładowej.* ▶️ *Załogę samolotu stanowi dwie _osoby pilotackie_ i inżynierskie pokładowe oraz sześć osób obsługi pokładowej.*
– wicepremier: *_Osoba wicepremierska_ Roman Malinowski pyta o rozmiary sił i środków niezbędnych dla przeprowadzenia tej akcji i czy możliwe będzie zbudowanie tych przegród na Wiśle do 15 bm.* ▶️ *_Osoba wicepremerska_ Roman Malinowski pyta o rozmiary sił i środków niezbędnych dla przeprowadzenia tej akcji i czy możliwe będzie zbudowanie tych przegród na Wiśle do 15 bm.*

2. In other cases, job titles were left completely unchanged:
– kopista (rare job title): *Baszmaczkina sam niegdyś postawiłem w dzienniku obok osoby kopistycznej Bartleby z noweli Melville'a.* ▶️ *Baszmaczkina sam niegdyś postawiłem w dzienniku obok kopisty Bartleby z noweli Melville'a.*
– mistrzyni (feminine noun in source): *Oprócz rekordu, _Osoba Mistrzowska_ zaprezentowała swoją siłę także na inne sposoby – unosząc samochód oraz podnosząc nad głowę ponad 80-kilogramowego mężczyznę.* ▶️ *Oprócz rekordu, _Mistrzyni_ zaprezentowała swoją siłę także na inne sposoby – unosząc samochód oraz podnosząc nad głowę ponad 80-kilogramowego mężczyznę.*
– sprzątaczka (feminine noun in source): *Sięgnął po słuchawkę, wybrał numer wewnętrzny sekretariatu, ale odezwała się tylko _osoba sprzątająca_.* ▶️ *Sięgnął po słuchawkę, wybrał numer wewnętrzny sekretariatu, ale odezwała się tylko _sprzątaczka_.*
– rówieśnik (semantic edge case that probably shouldn't be included): *Ja sam w szkole chodziłem w czapce w kamuflarz z doszytym futerkiem ""na irokeza"" i budziłem niezdrowe emocje w _osobach rówieśniczych_.* ▶️ *Ja sam w szkole chodziłem w czapce w kamuflarz z doszytym futerkiem ""na irokeza"" i budziłem niezdrowe emocje w _rówieśnikach_.*
– politycy, żurnaliści (multiple changes in one sentence + a rare job title): *Wiadomość z Langley oznacza, że osoba generalska Jaruzelski wprowadzając stan wojenny ocaliła 200 tysięcy ludzi, ale zaślepione osoby hunwejbińskie z IPN oraz prawicowe _osoby polityckie_ i _żurnalistyczne_ uważają inaczej.* ▶️ *Wiadomość z Langley oznacza, że osoba generalska Jaruzelski wprowadzając stan wojenny ocaliła 200 tysięcy ludzi, ale zaślepieni hunwejbini z IPN oraz prawicowi _politycy_ i _żurnaliści_ uważają inaczej.*
– mleczarz: *W 2000 roku sejneńskie _osoby mleczarskie_ skupiły ponad 23 mln litrów surowca.* ▶️ *W 2000 roku sejneńscy _mleczarze_ skupili ponad 23 mln litrów surowca.*
– ślusarz: *Prosty chłopak, z zawodu _osoba ślusarska_, a proszę, do czego doszedł: dwa domy, kilka samochodów, duże pieniądze.* ▶️ *Prosty chłopak, z zawodu _ślusarz_, a proszę, do czego doszedł: dwa domy, kilka samochodów, duże pieniądze.*
– poseł (multiple changes in one sentence): *_Osoba poselska_ od 1997 r. Andrzej Markowiak - 54 l., osoba inżynierska mechanicza.","_Poseł_ od 1997 r. Andrzej Markowiak - 54 l., osoba inżynierska mechaniczna.*
– cukiernik: *Jako ceniona _osoba cukeirnicza_ trafił od razu do jednego z pięciogwiazdkowych hoteli w stolicy kraju, Seulu.* ▶️ *Jako ceniony _cukiernik_ trafił od razu do jednego z pięciogwiazdkowych hoteli w stolicy kraju, Seulu.*

3. A lot of model's mistakes were related to case agreement and other morphosyntactical aspects that were deemed beyond the scope of the project, but had to be included in the target sentences nevertheless, eg:
– subject-verb agreement: *Do pracy naukowej _wróciła_ również niedawna osoba liderska UP, RYSZARD BUGAJ.* ▶️ *Do pracy naukowej _wrócił_ również niedawna osoba liderska UP, RYSZARD BUGAJ.* (prevalent group of morphosyntactic errors, additional examples: 5)
– object-verb agreement: *Na razie jedynie weto Kwaśniewskiego może powstrzymać _pazerne osoby awuesiarskie_, którzy mnożąc urzędy rozbudowują dla siebie przechowalnię.* ▶️ *Na razie jedynie weto Kwaśniewskiego może powstrzymać _pazernych osób awuesiarskich_, którzy mnożąc urzędy rozbudowują dla siebie przechowalnię.*
– attribute-noun agreement: *– bo on chyba _jakąś_ osobą dyrektorską przecież został nie?* ▶️ *– bo on chyba _jakimś_ osobą dyrektorską przecież został nie?*
– word order: *Ta wizja macierzyństwa spotkała się z polemiką ze strony _pacyfistycznej i feministycznej osoby działaczej_ Madeleine Vernet (1878-1949).* ▶️ *Ta wizja macierzyństwa spotkała się z polemiką ze strony _osoby działaczej pacyfistycznej i feministycznej_ Madeleine Vernet (1878-1949).*
– some issue related to numerals (most likely: different behaviour of masculine vs feminine nouns for cardinals 2-4 in nominative case, but also possibly: morphosyntactic difference between cardinals expressing the value of 2-4 and >4 ): *_Cztery młode osoby żołnierskie_ w granatowych mundurach MSW mocno _zapukały_ do drzwi.* ▶️ *_Czterech młodych osób żołnierskich_ w granatowych mundurach MSW mocno _zapukało_ do drzwi.*
– issues related to more complex isuess with abstract reasoning, such as the total number of people in the sentence: *Załogę samolotu stanowią _dwie osoby pilockie i osoba inżynierska pokładowa_ oraz sześć osób obsługi pokładowej.* ▶️ *Załogę samolotu stanowi dwie _osoby pilotackie i inżynierskie pokładowe_ oraz sześć osób obsługi pokładowej.*

4. Some changes were made in fact correctly, but they were beyond the scope of what was expected from the model, or the model invented a different valid form than the one provided in the set:
– czytelnik (correct form, but with object-verb agreement error): *Rozwiązując swoją drugą zagadkę kryminalną, młoda osoba detektywistyczna po raz kolejny zabiera _młodych czytelników_ w pasjonującą podróż po barwnym świecie opactwa benedyktyńskiego* ▶️ *Rozwiązując swoją drugą zagadkę kryminalną, młoda osoba detektywistyczna po raz kolejny zabiera _młodych osób czytelniczych_ w pasjonującą podróż po barwnym świecie opactwa benedyktyńskiego"*
– pilegrzymi (correct alternative version): *Za chwilę zgłosiła się ta sama osoba pracująca w recepcji i bez wstępów, widocznie konsultowała rzecz z siostrą, powiedziała: - Łączę z działem obsługi _osób pielgrzymujących_.* ▶️ *Za chwilę zgłosiła się ta sama osoba pracująca w recepcji i bez wstępów, widocznie konsultowała rzecz z siostrą, powiedziała: - Łączę z działem obsługi _osób pielgrzymskich_.*
– szef (correct alternative version): *Informację tygodnika ""Capital"", iż komisja śledcza Bundestagu ds. afery finansowej CDU zbada zarzuty przeciwko Siemensowi i b. osobie kanclerskiej, potwierdziła wczoraj _osoba szefująca_ komisji Volker Neumann.* ▶️ *Informację tygodnika ""Capital"", iż komisja śledcza Bundestagu ds. afery finansowej CDU zbada zarzuty przeciwko Siemensowi i b. osobie kanclerskiej, potwierdziła wczoraj _osoba szefowska_ komisji Volker Neumann.*
– fotograf (model's proposition is somewhat acceptable): *Pewnego dnia _osoba zajmująca się fotografią_ odkryje prawdę i będzie musiała zdecydować: czy kocha miłą powierzchowność Noelle czy fascynującą osobowość, ale i niezbyt kształtną figurę Abby.* ▶️ *Pewnego dnia _osoba fotografska_ odkryje prawdę i będzie musiał zdecydować: czy kocha miłą powierzchowność Noelle czy fascynującą osobowość, ale i niezbyt kształtną figurę Abby.*

5. Other differences are related to technical mistakes in the dataset:
– missing annotation of the second job title: *Ponownie zabrakło punktów osoby juniorskiej - powiedział _opiekun Płomienia_, Franciszek Hylla.* ▶️ *Ponownie zabrakło punktów osoby juniorskiej - powiedziała _osoba opiekująca się Płomienia_, Franciszek Hylla.*
– missing annotation of the second job title: *Straciła zezwolenie i została oskarżona. 72-letnia osoba farmaceucka sprzedawała więcej niż jej _pracownicy_.,Straciła zezwolenie i została oskarżona. 72-letnia osoba farmaceucka sprzedawała więcej niż jej _osoby pracownicze_.*
– grammaticar error of the annotator: *Osoby lekarskie i pielęgniarskie o oczach czerwonych od niewyspania _słaniali_ się na nogach ze zmęczenia, samoloty dowoziły szczepionkę z różnych końców świata: epidemia była przecież wtedy zaskoczeniem.* ▶️ *Osoby lekarskie i pielęgniarskie o oczach czerwonych od niewyspania _słaniły_ się na nogach ze zmęczenia, samoloty dowoziły szczepionkę z różnych końców świata: epidemia przecież była wtedy zaskoczeniem.*
– grammaticar error of the annotator: *W takiej sytuacji decyzję podejmuje sama osoba podatnicza, _który_ samodzielnie wypełnia roczne zeznanie podatkowe i nie musi przy tym pytać osób urzędniczych o zdanie.* ▶️ *W takiej sytuacji decyzję podejmuje sama osoba podatnicza, _która_ samodzielnie wypełnia roczne zeznanie podatkowe i nie musi przy tym pytać osób urzędniczych o zdanie.*
– grammaticar error of the annotator: *Osoba naczelnicza ulicznych osób rzeźniczych _wykrzywił_ twarz.* ▶️ *Osoba Naczelnicza ulicznych osób rzeźniczych _wykrzywiła_ twarz.*
– spelling error of the annotator: *Jaka jest pewność, że Pismo Święte po wielu tłumaczeniach oddaje wiernie to, co osoby autorskie _mialy_ na myśli...* ▶️ *Jaka jest pewność, że Pismo Święte po wielu tłumaczeniach oddaje wiernie to, co osoby autorskie _miały_ na myśli...*
– trailing white space: *Osoba logopedzka diagnozuje i leczy wady wymowy u dzieci i dorosłych. * ▶️ *Osoba logopedzka diagnozuje i leczy wady wymowy u dzieci i dorosłych.*
– no-break whitespace after one-letter words (removed by the model): *Kto z państwa osób senatorskich jest za przyjęciem poprawek: dwudziestej trzeciej, dwudziestej szóstej, trzydziestej szóstej i czterdziestej, proszę o naciśnięcie przycisku ""za"".* ▶️ *Kto z państwa osób senatorskich jest za przyjęciem poprawek: dwudziestej trzeciej, dwudziestej szóstej, trzydziestej szóstej i czterdziestej, proszę o naciśnięcie przycisku ""za"".*

6. The most exceptional change is a completely unexpexted application of the rule to a gendered pronoun:
"_Ten, kto dyktuje warunki_, kto powołał osobę narratorską i kto tak długo zostawiał bez odpowiedzi listy i faksy, przypomina sobie co jakiś czas o zaległych sprawach, poczynając od cieknącego kranu, a kończąc na bankowych dyspozycjach."
"_Osoba, która dyktuje warunki_, kto powołał osobę narraterską i kto tak długo zostawiał bez odpowiedzi listy i faksy, przypomina sobie co jakiś czas o zaległych sprawach, poczynając od cieknącego kranu, a kończąc na bankowych dyspozycjach."

## Errors and shortcomings

1. Despite our best efforts, there were mistakes in the dataset: the reason for that is the fact that we didn't have enough resources to provide any proofreading. Standard practice would be to have at least two annotators and one superannnotator – in our case, every example was prepared by one annotator without proofreading. Additionally, even though some normalization has been performed at different stages for different subsets of the data, it wasn't consistent enough to ensure adequate conditions for fully reliable metrics based on Levensthein's distance.
– On one hand, errors present in the training/validation splits may have contributed to worse-than-possible training results (model could come to "wrong conclusions" based on erroneous examples in training),
– On the second, errors present in the test split have likely caused the output quality to be underreported (there are at least two cases where model was "more right" than the test data target, while it is very unlikely for the annotators to commit an error *exactly* the same as an error later commited by the model for *exactly* the same test example),
– However, the number of errors is not too big and can be easily remediated by having even one round of proofreading. Proofreading has not been performed before submitting this project, as at this state it would equate to falsifying documentation.

2. The dataset was not balanced the way it was intended to be (in terms of morphological variety of job titles), nor was it as homogenous as intended (there were semantic edge cases present, as well as a variety of cases instead of just singular nominative forms), and some of the examples contained more than one job title.
– This has made the task all the more complicated for the model, as there are more parameters influencing the quality of the output, such as possible mistakes concetning case endings, number agreement, recognizing edge cases etc.

## Conclusions

The results are very promising and much better than expected. The relatively high quality of the obtained outputs is especially surprising given the errors present in the dataset. Despite it not being the goal, the model made valid attempts at neutralizing edge cases (_osoby czytelnicze_) and provided partially correct gramatical adjustments.

It is advisable to proofread the existing dataset [ArielUW/jobtitles], as well as to expand it with additional examples tailored to adress:
– the most problematic morphological types of job titles (such as the ones neutralised to: _osoba zajmująca się (...)_),
– feminine nouns,
– morphosyntactic inticacies of subject-verb agreement, case and number agreement and co-reference,
– multiple changes per one sentence.

Finally, the texts in the dataset need to be properly normalised, especially in the test split, to ensure uniformity in terms of:
– dashes (en vs em),
– hyphens (breaking vs non-breaking ones),
– ellipsis (three dots vs single elpisis character),
– whitespaces (standard vs no-break space),
– quotation marks,
– no trailing whitespaces.

It is worth considering if more than one correct version (if it exist for a particular sentence) should be provided in the test split for a more accurate evaluation.

After that the training process should be repeated from scratch for the base model, as the here presented fine-tuned model was most likely negatively affected by the existence of errors in the dataset.