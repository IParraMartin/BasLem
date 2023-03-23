import re

text = '-Nire etxerantz joan ginen Bilboko kaleetatik.'

def get_clean_text(data):

    lowercase = data.lower()
    numbers = re.sub('[0-9]', ' ', lowercase)
    punctuation = re.sub('[^\w]', ' ', numbers)
    spacing = re.sub("\s\s+", " ", punctuation)
    clean = spacing

    return clean

clean = get_clean_text(text)
print(clean)

list_tokens = clean.split()
print(list_tokens)




