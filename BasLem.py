import re

# example to test the performance
text = '-Katua eta ni nire etxerantz joan ginen Bilboko kaleetatik.'


# cleaning function
def get_clean_text(data):

    lowercase = data.lower()
    numbers = re.sub('[0-9]', ' ', lowercase)
    punctuation = re.sub('[^\w]', ' ', numbers)
    spacing = re.sub("\s\s+", " ", punctuation)
    clean = spacing

    return clean

clean = get_clean_text(text)


list_tokens = clean.split()

# lemmatizing and stemming
def get_lemmas(data):

    stoppers = ['eta']
    lemmatized_tokens = []

    for token in data:
    
        if token.endswith('a') and token not in stoppers:

            token = token[:-1]
            lemmatized_tokens.append(token)
        
        else:

            lemmatized_tokens.append(token)

    return lemmatized_tokens

lemmatized = get_lemmas(list_tokens)
print(lemmatized)