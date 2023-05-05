import nltk
import numpy as np
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords

text = 'محمود يعيش في مصر'

#word_tokenize(text)

#print(word_tokenize(text))

#list(ngrams (text.split(), 1))

sw = stopwords.words('english')

len(sw)