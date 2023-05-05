import PyPDF2

#pre-processing imports here
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import string


#mount Google drive
from google.colab import drive
drive.mount('/content/drive')

#file locations on drive
grimm_url = '/content/drive/My Drive/Lessons/storyTeller/FairytalesByTheBrothersGrimm.txt'
coraline_url = '/content/drive/My Drive/Lessons/storyTeller/Coraline.pdf'
alice_url = '/content/drive/My Drive/Lessons/storyTeller/AlicesAdvanturesInWonderland.txt'

#load punctuation symbols
punct = string.punctuation

#a function to pre process Coraline by Neil Gaiman

def preprocess_coraline(book):
  '''
  param book: url od a PDF book file
  '''
  output = ""
  data = open(book, 'rb')
  data = PyPDF2.PdfFileReader(book)
  npages = data.getNumPages()
  for i in range(npages):
    page_i = data.getPage(i).extractText()
    output += page_i
  output = output[1227:]
  output = output.lower()
  for word in output:
    for char in word:
        if char in punct:
            word = word.replace(char, "")
  remove_punct = "".join([word for word in output if word not in punct])
  processed = word_tokenize(remove_punct)
  print('Coraline database includes {} tokens, and {} unique tokens after editing'.format(len(processed), len(set(processed)))) 
  return processed

coraline = preprocess_coraline(coraline_url) 

#a function to pre process Alice's Advantures in Wonderland by Lewis Carroll

def load_alice(text_file, punct, not_a_word):
    '''
    param text_file: url to Project Gutenberg's text file for Alice's Advantures in Wonderland by Lewis Carroll
    param punct: a string of punctuation characters we'd like to filter
    param not_a_word: a list of words we'd like to filter
    '''
    book = open(text_file, 'r')
    book = book.read()
    book = book[715:145060]
    book_edit = re.sub('[+]', '', book)
    book_edit = re.sub(r'(CHAPTER \w+.\s)', '', book)
    words = word_tokenize(book_edit.lower())
    
    word_list = []
    
    # filtering punctuation and non-words
    for word in words:
        for char in word:
            if char in punct:
                word = word.replace(char, "")
        if word not in punct and word not in not_a_word:
            word_list.append(word)

    print('Alice database includes {} tokens, and {} unique tokens after editing'.format(len(word_list), len(set(word_list)))) 
    return word_list

alice = load_alice(alice_url, (punct.replace('-', "") + '’' + '‘'), ['s', '--', 'nt', 've', 'll', 'd'])

def load_fairytales(text_file):
    '''
    param text_file: url to Project Gutenberg's text file for Fairytales by The Brothers Grimm
    '''
    book = open(text_file, encoding='cp1252')
    book = book.read()
    book = book[2376:519859]
    book_edit = re.sub('[(+*)]', '', book)
    words = word_tokenize(book_edit.lower())

    # filtering punctuation inside tokens (example: didn't or wow!)
    for word in words:
        for char in word:
            if char in punct:
                word = word.replace(char, "")

    # filtering punctuation as alone standing tokens(example: \ or ,)
    words = [word for word in words if word not in punct]

    print('Fairytales database includes {} tokens, and {} unique tokens after editing'.format(len(words), len(set(words))))            
    return words

brothers_grimm = load_fairytales(grimm_url)


data = coraline + alice + brothers_grimm
data[:10]

