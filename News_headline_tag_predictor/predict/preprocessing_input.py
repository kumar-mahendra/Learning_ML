import re 
import nltk 
import string 
try : 
    from nltk.corpus import stopwords 
except : 
    nltk.download('stopwords')
    nltk.download('wordnet')

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
wordnet_lemma = WordNetLemmatizer()  
Stopwords = set(stopwords.words('english'))  #set of all stopword


def clean_sentence(sentence):

    # A little bit sentence cleaning first to handle scenerio like his-her (note if dash is removed then 'hisher' is a nonsense word) by adding comma before and after such symbols . 
    sentence = sentence.replace('-',' - ')
    sentence = sentence.replace('.',' . ')
    sentence = sentence.replace('/',' / ')
    sentence = sentence.replace(',', ' , ')  # and so on.....as much as you like but these are a few common ones

    Words=sentence.split()
    sentence = ''
    for word in Words:
        word = word.replace("'s",' is')
        word = word.replace("'nt",' not')
        word = word.replace("n't",' not')
        word = word.replace("'d", ' had')
        word = word.replace("'ll",' will')
        word = word.replace("'m",' am')
        word = word.replace("'ve",' have')
        word = word.replace("'re", ' are')
        sentence = sentence + word + ' '
    sentence = re.sub("^\s+"," ",sentence)  #removing extra whitespaces (if any) from text
    sentence = ''.join([i for i in sentence if i not in string.punctuation])  #remove punctuations
    sentence = ' '.join([i.lower() for i in sentence.split()])   #Normalization i.e. convert to lower-case each word 
    sentence = ' '.join([i for i in sentence.split() if i not in Stopwords])  # Removing stopwords
    sentence = ' '.join([wordnet_lemma.lemmatize(i) for i in sentence.split()]) #convert each word in its noun form
    new_ = [re.findall("^[a-z]*$",i) for i in sentence.split() if re.findall("^[a-z]*$",i) !=[] ]  #excluding numbers present (if any)
    sentence = ' '.join([x[0] for x in new_])

    return [sentence] 
