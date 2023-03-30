# Import library 
import BasLem

# Set tokenizer 
tokenizer = BasLem.Tokenization()

# Import text to be lemmatized/stemmed 
text = "- Katua eta ni nire etxerantz joan ginen Bilboko kaleetatik jokatzen zituzten."

# Process the text
data = tokenizer.get_clean_text(text)
lemmas = tokenizer.get_lemmas(data)
print(lemmas)