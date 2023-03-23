# BasLem
Lemmatizing code for Basque text

# A tokenizer for Basque
I present a basic code (currently under costruction) to lemmatize and stemm Basque text. I came up with the idea while I was trainning a sentiment analysis word embedding. The shortage of resources for low-resource languages (LRLs) is making these languages to be left out of the AI, ML, and NLP wave. Feel free to comment, re and de-construct the code, and modify it as you want, all contributions are welcome!

# Limitations
Even if it is able to clean text and modify determiner in nouns (katua < katu[0]), it still needs 'bounding' of exceptions. I will be working on that.

I am also working on ways to effectively lemmatize complex word formations such as verbs and cases.

- There is a new addition to the code that allows skipping exceptions (get_lemmas -> stoppers = str)
