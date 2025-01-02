import nltk
from nltk.tokenize import word_tokenize

# Load Sanskrit corpus
corpus = open('E:\Projects\VS Code\Dummy\slokas.txt', encoding='utf-8').read()
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
# Tokenize corpus
tokens = word_tokenize(corpus)

# Label tokens with parts of speech
pos_tags = nltk.pos_tag(tokens)

# Save labeled corpus to file
with open('E:\Projects\VS Code\Dummy\sanskrit_corpus_pos.txt', 'w', encoding='utf-8') as f:
    for token, pos in pos_tags:
        f.write(token + '\t' + pos + '\n')