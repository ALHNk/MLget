import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from collections import Counter
import os
from sklearn.model_selection import train_test_split


# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def preprocesses(text, stopwords, punctuation_marks):
  tokens= word_tokenize(text.lower())
  lemmatizer = WordNetLemmatizer()
  prep_text = []
  for token in tokens:
    if token not in punctuation_marks:
      lemma = lemmatizer.lemmatize(token, get_wordnet_pos(token))
      if lemma not in stopwords:
        prep_text.append(lemma)

  return prep_text

max_words = 10000
random_state = 42

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'datasets/laptops.csv')
laptops = pd.read_csv(file_path, sep = ",")

punctuation_marks = ['!', ',', '(', ')', ':', '-', '?', '.', '..', '...', '«', '»', ';', '–', '--', '[', ']']
stop_words = stopwords.words("english")

laptops["preproccessed_text"] = laptops.apply(lambda row: preprocesses(row['review'], stop_words, punctuation_marks), axis = 1)

X = laptops['preproccessed_text']
y = laptops['rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)
# print(f"train x is {X_train}, train y is: {y_train}, test x is {X_test}, test y is {y_test}")

train_df = pd.DataFrame({'text': X_train, 'rating': y_train})
test_df = pd.DataFrame({'text': X_test, 'rating': y_test})

train_df.to_csv(os.path.join(base_path, 'datasets/train_data_laptops.csv'), index=False)
test_df.to_csv(os.path.join(base_path, 'datasets/test_data_laptops.csv'), index=False)

