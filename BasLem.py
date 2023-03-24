import re

# example to test the performance
text = '- Katua eta ni nire etxerantz joan ginen Bilboko kaleetatik jokatzen.'


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

    stoppers = ['eta', 'baina', 'zela']
    listatik = []
    lemmatized_tokens = []

    for token in data:
    
        if token.endswith('a') and token not in stoppers:

            token = token[:-1]
            lemmatized_tokens.append(token)
        
        elif token.endswith('rantz'):
            token = token[:-5]
            lemmatized_tokens.append(token)

        elif token.endswith('ko'):
            token = token[:-2]
            lemmatized_tokens.append(token)

        elif token.endswith('tatik'):

            listatik.append(token)

            for token in listatik:

                if re.search(r'(etatik|tatik)$', token):

                    if token.endswith('etatik'):

                        token = token[:-6] #one character less to delete for double vowels
                        lemmatized_tokens.append(token)

                    else:
                        token = token[:-5] #usual -tatik
                        lemmatized_tokens.append(token)
        
        elif token.endswith('tzen'):

            token = token[:-4]
            token = token+str('tu')
            lemmatized_tokens.append(token)
        
        else:

            lemmatized_tokens.append(token)

    return lemmatized_tokens

lemmatized = get_lemmas(list_tokens)
print(lemmatized)