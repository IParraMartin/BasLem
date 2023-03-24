![GitHub repo file count](https://img.shields.io/github/directory-file-count/IParraMartin/BasLem)
![GitHub repo size](https://img.shields.io/github/repo-size/IParraMartin/BasLem?color=red)

# BasLem
Lemmatizing code for Basque text

## A tokenizer for Basque
I present a basic code (currently under costruction) to lemmatize and stemm Basque text. I came up with the idea while I was trainning a sentiment analysis word embedding. The shortage of resources for low-resource languages (LRLs) is making these languages to be left out of the AI, ML, and NLP wave. Feel free to comment, re and de-construct the code, and modify it as you want, all contributions are welcome!

## New features record
- There is a new addition to the code that allows skipping exceptions (get_lemmas -> stoppers = str)
- New additions on present participle lemmatizing (e.g. jokatzen < jokatu)
- Verb 'eduki' (to have) in present form is now normalized to its infinitival form
- Added change counter. Visualizes the relative effectivity of the lemmatizer/stemmer

## Limitations
Even if it is able to clean text and modify determiner in nouns (katua < katu[0]), it still needs 'bounding' of exceptions. I will be working on that.

I am also working on ways to effectively lemmatize complex word formations such as verbs and cases.


