import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
from nltk.tag import pos_tag

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')

tokenizer = TreebankWordTokenizer()

def removeStopWord(text):
    words = tokenizer.tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    tagged_words = pos_tag(filtered_words, lang='eng')  # 👈 language specified
    relevant_tags = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS']
    relevant_words = [word for word, tag in tagged_words if tag in relevant_tags]
    return ' '.join(relevant_words)
