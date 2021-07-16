
# Import required libraries
import re, random, string
import numpy as np
import nltk 
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer

wordnet_lemma = WordNetLemmatizer()  
Stopwords = set(stopwords.words('english'))  #set of all stopword

# Preparing dataset file

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
    return sentence 

def preprocessing_text(news_type="tech"):
    sentence_corpus = set()
    text = ""
    with open(news_type+".txt","r") as doc :
        for line in doc :

            line = clean_sentence(line)  #clean sentence 

            line = re.sub("^\s+"," ",line)  #removing extra whitespaces (if any) from text
            
            line = ''.join([i for i in line if i not in string.punctuation])  #remove punctuations
            
            line = ' '.join([i.lower() for i in line.split()])   #Normalization i.e. convert to lower-case each word 

            line = ' '.join([i for i in line.split() if i not in Stopwords])  # Removing stopwords
            
            line = ' '.join([wordnet_lemma.lemmatize(i) for i in line.split()]) #convert each word in its noun form
            
            new_ = [re.findall("^[a-z]*$",i) for i in line.split() if re.findall("^[a-z]*$",i) !=[] ]  #excluding numbers present (if any)
            line = ' '.join([x[0] for x in new_])

            text += line+","+news_type+"\n"
        
    return text



headings = ['health','india','entertainment','sports','world','tech']
news_headlines = []
n = 7000                                                                 # Total no of headlines of each category

for news_type in headings :
    type_headlines = preprocessing_text(news_type)
    type_headlines = type_headlines.split("\n") 
     
    if (len(type_headlines)>=n):
        type_headlines=type_headlines[0:n]               #Take initial n headlines 
    news_headlines.extend(type_headlines)  

news_headlines=np.array(news_headlines) 
random.shuffle(news_headlines)

with open('news_headlines.csv','w+') as f:
    f.truncate()                                        # clear already existing content
    f.write('news_headline,news_category'+'\n')
    for news in news_headlines :
        f.write(news+'\n')
        


