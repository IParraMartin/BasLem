import BasLem

tokenizer = BasLem.Tokenization()

text = "- Katua eta ni nire etxerantz joan ginen Bilboko kaleetatik jokatzen zituzten."

data = tokenizer.get_clean_text(text)
lemmas = tokenizer.get_lemmas(data)

print(lemmas)