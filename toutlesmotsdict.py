# NumPy is imported, seed is set
from email.policy import strict
from fileinput import nextfile
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

#np.random.seed(123)

os.system('cls')

sd = ',ksjdrgfvergfuchshhh'

def letterRepetition (word) :

    letters = {}

        if letter not in letters:
            letters[letter] = 1 
        else:
            letters[letter] =  letters[letter] + 1
    return letters


a = letterRepetition(sd)


max = max(a.values())


if 1 not in a.values():
    next
else:
    print('il y a letter en double')


filename = ('toutlesmotsdict.csv')
df = pd.read_csv(filename)

df.to_string()
print(df.columns)
for col in df:
    if col == 'Unnamed: 0':
        next
    else:
        

        #print(df[col].dtype)veretvesce vvvrebe v as vas vve vedette verge  verset vertezx waters    ssabra tzaer tzaer rtzar  vg vase   vs vaste  ra  r rabattage  saa sa faste fat fartage fartadet fardage fatwa ferry fetardf efez va 
    
        #print(df[col])

        
        maingauche = r'[qwertyuiopasdfghjkl]'
        mainby = 'b|y'
        maindroite = '[uiophjklnm]'
      
        
        print( df[col][df[col].str.contains(maingauche)    & ~df[col].dropna().str.contains('[^qwertyuiopasdfghjkl]')   ]) 
        #print(df[(df[col].str.contains(maingauche) | df[col].str.contains(mainby)) & ~df[col].str.contains(maindroite) ])  ~df[col].dropna().str.contains(maindroite) & ~dfcaratNotaccep



         

