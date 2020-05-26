# NLP with sessions transcripts  from Panama National Assembly
We use pdfplumber for read the 10 pdfs examples files from Panama National Assembly website.
# Files
## NLPTesting.ipynb 
 In this Jupyter Notebook we are testing if the data can works properly with NLP, thats why we are using only one PDF located in resources/pdfs. We crop the footer and index number then use Regex for match only the paragraphs and not the name of the person who said it and save the final data in a txt call "Resultado.txt". After the data extract we use Spacy for parse, tokenization, NER, Similarity, vectorization and SentimentClassifier with nltk (Not so good).

## Testing_TopicModeling.ipynb
We only using 10 pdfs, extract the data, clean the data with regex and then pass to a txt file. After the data is ready, we use nltk and gensim for make three Topic Models (HDP, LSI and LDA). After the models are ready we compare in terms of coherence and the winner was HDP but the data need to be improve (Read recommendations). 

## Resultado.txt
The data ready for NLPTesting. 
# Resources
## pdf_Enero
There are the ten PDFS using for Testing_TopicModeling. 

## pdf_txts
There are the ten txt files ready for the Topic Modeling. 

## pdfs

Only one PDF used in NLPTesting.

## Regex_sanbox 
Txt files NOT ready, only the exctract text without regex and crop. 

# Recommendations 
1. Each PDF can have many topics, depending on the debate or law that is being discussed, the text needs to be divided according to the law or debate to obtain better results.
2. Add more some words in the black list for avoid unimportant words. 
