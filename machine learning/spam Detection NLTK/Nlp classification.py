import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, balanced_accuracy_score
from sklearn.naive_bayes import MultinomialNB

from warnings import filterwarnings
filterwarnings('ignore')
import nltk

messages=pd.read_csv("C:/Users/Mahmoud Elkolfat/Downloads/spam.csv", encoding='latin-1')
messages.head()

messages.info()

messages.columns=['label', 'c1','c2','c3','c4']
messages.head(1)

messages.fillna(' ', inplace=True)

messages['text']=messages['c1']+' '+messages['c2']+' '+messages['c3']+' '+messages['c4']
messages.drop(columns=['c1','c2','c3','c4'], inplace=True)
messages.info()

messages.describe()

messages.groupby('label').describe()

messages['length']=messages['text'].apply(len)
messages.head(3)


messages['length'].plot.hist(bins=100)
plt.xlabel('Length of text')
plt.show()


messages.hist(column='length',by='label', bins=100, figsize=(12,4))
plt.show()

good_msg = messages[messages['label'] =='ham']
spam_msg = messages[messages['label']=='spam']
# Create numpy list to visualize using wordcloud
good_msg_text = " ".join(good_msg.text.to_numpy().tolist())
spam_msg_text = " ".join(spam_msg.text.to_numpy().tolist())


# wordcloud of good messages
ham_msg_cloud = WordCloud(width =520, height =260, stopwords=STOPWORDS, max_font_size=50, background_color ="black",
                          colormap='Blues').generate(good_msg_text)
plt.figure(figsize=(16,10))
plt.imshow(ham_msg_cloud, interpolation='bilinear')
plt.axis('off') # not display axis
plt.show()


# wordcloud of spam messages
spam_msg_cloud = WordCloud(width =520, height =260, stopwords=STOPWORDS,max_font_size=50, background_color ="black", 
                           colormap='Blues').generate(spam_msg_text)
plt.figure(figsize=(16,10))
plt.imshow(spam_msg_cloud, interpolation='bilinear')
plt.axis('off') # not to display
plt.show()



string.punctuation

name='Hi! I am Senan.'

name=[c for c in name if c not in string.punctuation]

name=''.join(name)

nltk.download('stopwords')
stopwords.words('english')

name.split()

clean=[word for word in name.split() if word.lower() not in stopwords.words('english')]
clean


def text_process(data):
    # removing punc
    # removing stopwords
    nopunc=[char for char in data if char not in string.punctuation]
    nopunc=''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


messages.iloc[:3,1].apply(text_process)



transformer1=CountVectorizer(analyzer=text_process).fit(messages['text'])

len(transformer1.vocabulary_)

a=messages['text'][1]
a

b=transformer1.transform([a])
print(b)

print(b.shape)

transformer1.get_feature_names_out()[2455] 
# an istance: 2455 indexed feature name is "Joking"

transformed=transformer1.transform(messages['text'])
transformed.shape
print('Sparsity:', 1-(100.0 * transformed.nnz/(transformed.shape[0]*transformed.shape[1])))

tfidf_transformer = TfidfTransformer().fit(transformed)
transformed2=tfidf_transformer.transform(b)
print(transformed2)

messages_tfidf=tfidf_transformer.transform(transformed)

sp_model = MultinomialNB().fit(messages_tfidf, messages['label'])

sp_model.predict(transformed2)

messages['label'][1]

prd=sp_model.predict(messages_tfidf)
prd

train_x, test_x, train_y, test_y =train_test_split(messages['text'], messages['label'], test_size=0.6, random_state=25)

# to do actions sequentially
pipeline=Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(train_x, train_y)



pred=pipeline.predict(test_x)

print(classification_report(test_y, pred))
print('-----------------------------------------')
print('Accuracy score: ',accuracy_score(test_y, pred))
print('-----------------------------------------')
print('Balanced Accuracy score: ',balanced_accuracy_score(test_y, pred))

# from skl2onnx import convert_sklearn
# from skl2onnx.common.data_types import FloatTensorType, StringTensorType

# initial_type = [('numfeat', FloatTensorType([None, 3]))]
# model_onnx = convert_sklearn(pipeline, initial_types=initial_type)
# # model_onnx.opset_import()

from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Specify an initial type for the model ( similar to input shape for the model )
initial_type = [
    ( 'input_study_hours' , FloatTensorType( [None,3] ) ) 
]

# Write the ONNX model to disk
converted_model = convert_sklearn(pipeline , initial_types=initial_type )
with open("sklearn_model.onnx", "wb") as f:
    f.write( converted_model.SerializeToString())
    

