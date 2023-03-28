import re
import unicodedata

class Tokenization:

    def __init__(self):

        try: #runs a try to make sure the requirements are fullfilled
            import re
        except:
            print("Regex library is not installed, try pip install re")

        try:
            import unicodedata
        except:
            print("Unicodedata library is not installed, try pip install unicodedata")


    def get_clean_text(self, data):

        data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore').decode('utf-8')
        lowercase = data.lower()
        numbers = re.sub('[0-9]', ' ', lowercase)
        punctuation = re.sub('[^\w]', ' ', numbers)
        spacing = re.sub("\s\s+", " ", punctuation)

        return spacing
    

    def get_lemmas(self, data):

        changes_counter = 0
        
        
        stoppers = ['eta', 'baina', 'zela'] 
        eduki_verb = ['dut', 'duzu', 'du', 'dute', 'duzue', 'ditut', 'dituzu', 'ditu', 'dituzte', 'dituzue']
        listatik = []
        lemmatized_tokens = []
        conjugations = ["a", 'rantz', 'ko', 'etatik', 'tatik', 'tzen']
        

        tokens = data.split()

        for token in tokens:

            if not token.endswith(tuple(conjugations)):

                token = token
                lemmatized_tokens.append(token)
            
            else:
            
                for conjugation in conjugations:

                    if token.endswith(conjugation) and token not in stoppers:

                        token = token[:-1*len(conjugation)]
                        lemmatized_tokens.append(token)
                        changes_counter+=1

                        break

        return lemmatized_tokens
    

tokenizer = Tokenization()
text = "- Katua eta ni nire etxerantz joan ginen Bilboko kaleetatik jokatzen."
data = tokenizer.get_clean_text(text)
















# import re
# import unicodedata

# # example to test the performance
# text = '- Katua eta ni nire etxerantz joan ginen Bilboko kaleetatik jokatzen.'

# # cleaning function
# def get_clean_text(data):

#     data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore').decode('utf-8')

#     lowercase = data.lower()
#     numbers = re.sub('[0-9]', ' ', lowercase)
#     punctuation = re.sub('[^\w]', ' ', numbers)
#     spacing = re.sub("\s\s+", " ", punctuation)

#     return spacing

# clean = get_clean_text(text)

# list_tokens = clean.split()

# # lemmatizing and stemming
# def get_lemmas(data):

#     changes_counter = 0
    
#     stoppers = ['eta', 'baina', 'zela']
#     eduki_verb = ['dut', 'duzu', 'du', 'dute', 'duzue', 'ditut', 'dituzu', 'ditu', 'dituzte', 'dituzue']
#     listatik = []
#     lemmatized_tokens = []
#     conjugations = ["a", 'rantz', 'ko', 'etatik', 'tatik', 'tzen']
#     conjugations = ['etatik', 'tatik', 'rantz', 'a' , 'k'] # check for biggest conjugations first

#     for token in data:
#         for conjugation in conjugations:
#             if token.endswith(conjugation) and token not in stoppers:
#                 token = token[:-1*len(conjugation)]
#                 lemmatized_tokens.append(token)
#                 changes_counter+=1
#                 break

    
#         if token.endswith('a') and token not in stoppers:

#             token = token[:-1]
#             lemmatized_tokens.append(token)
#             changes_counter += 1
        
#         elif token.endswith('rantz'):
#             token = token[:-5]
#             lemmatized_tokens.append(token)
#             changes_counter += 1

#         elif token.endswith('ko'):
#             token = token[:-2]
#             lemmatized_tokens.append(token)
#             changes_counter += 1

#         elif token.endswith('tatik'):

#             listatik.append(token)

#             for token in listatik:

#                 if re.search(r'(etatik|tatik)$', token):

#                     if token.endswith('etatik'):

#                         token = token[:-6] #one character less to delete for double vowels
#                         lemmatized_tokens.append(token)
#                         changes_counter += 1

#                     else:
#                         token = token[:-5] #usual -tatik
#                         lemmatized_tokens.append(token)
#                         changes_counter += 1
        
#         elif token.endswith('tzen'):

#             token = token[:-4]
#             token = token+str('tu')
#             lemmatized_tokens.append(token)
#             changes_counter += 1

#         elif token in eduki_verb:

#             token = 'eduki'
#             lemmatized_tokens.append(token)
#             changes_counter += 1

#         else:

#             lemmatized_tokens.append(token)
    
#     print(f'Changes made: {changes_counter}')

#     return lemmatized_tokens

# lemmatized = get_lemmas(list_tokens)
# print(lemmatized)