import re

# example to test the performance
text = '- Katua eta ni nire etxerantz joan ginen Bilboko kaleetatik jokatzen dut.'

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

    changes_counter = 0
    
    stoppers = ['eta', 'baina', 'zela']
    eduki_verb = ['dut', 'duzu', 'du', 'dute', 'duzue', 'ditut', 'dituzu', 'ditu', 'dituzte', 'dituzue']
    listatik = []
    lemmatized_tokens = []

    for token in data:
    
        if token.endswith('a') and token not in stoppers:

            token = token[:-1]
            lemmatized_tokens.append(token)
            changes_counter += 1
        
        elif token.endswith('rantz'):
            token = token[:-5]
            lemmatized_tokens.append(token)
            changes_counter += 1

        elif token.endswith('ko'):
            token = token[:-2]
            lemmatized_tokens.append(token)
            changes_counter += 1

        elif token.endswith('tatik'):

            listatik.append(token)

            for token in listatik:

                if re.search(r'(etatik|tatik)$', token):

                    if token.endswith('etatik'):

                        token = token[:-6] #one character less to delete for double vowels
                        lemmatized_tokens.append(token)
                        changes_counter += 1

                    else:
                        token = token[:-5] #usual -tatik
                        lemmatized_tokens.append(token)
                        changes_counter += 1
        
        elif token.endswith('tzen'):

            token = token[:-4]
            token = token+str('tu')
            lemmatized_tokens.append(token)
            changes_counter += 1

        elif token in eduki_verb:

            token = 'eduki'
            lemmatized_tokens.append(token)
            changes_counter += 1

        else:

            lemmatized_tokens.append(token)
    
    print(f'Changes made: {changes_counter}')

    return lemmatized_tokens

lemmatized = get_lemmas(list_tokens)
print(lemmatized)