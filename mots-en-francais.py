# NumPy is imported, seed is set
from email.policy import strict
from importlib.resources import contents
from operator import le
from re import X
import string
from turtle import title
from typing import Concatenate
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import os

from bs4 import BeautifulSoup
import requests
import re

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")

#np.random.seed(123)

os.system('cls')

url = 'https://usito.usherbrooke.ca/index/mots#a'

result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")

print('-'*30)
wordtags = doc.find('ol').find_all('a')

numRows= len(wordtags)

numCols= 3 #  not done but we can read the num of attrs in tag('a') if needed, len(wordtags[0].attrs) + 1 car on fait un split 


wordlist =  [['' for i in range(numCols)] for j in range(numRows)]




for index, atag in enumerate(wordtags):
    split = wordtags[index].attrs['title'].split(':')

    wordlist[index][0] = split[0]
    wordlist[index][1] = split[1]
    wordlist[index][2]= 'https://usito.usherbrooke.ca' + wordtags[index].attrs['href'] 
    

df_letters = pd.DataFrame(data =wordlist)



print(df_letters)



df_Allwords = pd.DataFrame()

#--------------------------------
#letters = doc.find('ol')


for url in  df_letters[2]:

    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")


    
    words = doc.find('ul').find_all('a')
    
    


    df_words = pd.DataFrame(data =words)
    
    df_Allwords = pd.concat([df_Allwords,df_words], axis = 1)
    


df_Allwords.columns = df_letters[0]
df_Allwords.to_csv('C:/Users/Rene_/OneDrive/Bureau/pythontest1/toutlesmotsdict.csv')
print(df_Allwords.info())
"""
listletters=[]

lettres = list(doc.find('ol').find_all('a'))
for l in lettres:

    listletters.append(l.attrs['title'])
        
print(listletters)

df_letters = pd.DataFrame(data =listletters)
print(df_letters)





#------------------------------------------



a= df_words[0].str.count('a') >1

b= df_words[0].str.count('f') >1   
test = a & b
#test  =  df_words[df_words[0].str.count('abc') >1  ]
print(df_words, df_words[test] )








#df_words['...'] = re.match(pattern, df_words[0])
#print(df_words)


filename = ('netflix_titles.csv')


netflix = pd.read_csv(filename)

print('-*20')
print(netflix.iloc[:,1:3].mode())


netflix['rating'].replace(np.nan, netflix.rating.mode()[0], inplace=True)

netflix['date_added'] = pd.to_datetime(netflix['date_added'])
netflix['year_added'] = netflix['date_added'].dt.year
    
#print(variables)


print(netflix.info())

#print(type(var))
print(type(netflix.index))
print(type(netflix.columns))
print(netflix.country.mode().shape)
"""