import spacy
import medspacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("John Smith presented with speech delay on 12/03/2022.")
print("test")
print(doc.ents)
for ent in doc.ents:
    if ent._.is_phi:  # spaCy extension
        print(ent.text, ent.label_)
    else:
        print("no")   