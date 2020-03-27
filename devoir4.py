# coding: utf-8

#Bonjour JH, je n'ai pas été en mesure de réussir le devoir 4. Voici mes notes de cours.

#Importer le .csv des chroniques à R. Martineau et le module NLTK
import csv
import nltk

#Importer à partir de NLTK : tokenizer (isoler mots), counter (nb occurences), snowballstemmer (racine des mots) et stopwords (mots vides)
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

#Créer, ouvrir et rouler le script dans les chroniques à R. Martineau
inspect = "martino.csv"
a = open(inspect)
chroniques = csv.reader(a)
next(chroniques)
inter = []

for mot in chroniques:
    tokens = word_tokenize(inter[25])

#Aller à la racine
fr = SnowballStemmer('french') 
racines = [fr.stem(mot)for mot in word_tokenize(inter[50])] 
print(racines)

tokens = [mot for mot in word_tokenize(inter[50])if mot not in stopwords.words('french')]
print(tokens)

#Supprimer la ponctuation
tokens = [mot for mot in word_tokenize(inter[50])if mot not in stopwords.words('french') and mot not in string.punctuation]
print(tokens)

#Calculer occurences de chaques mots
mots = [fr.stem(mot)for mot in word_tokenize(inter[50])if mot not in stopwords.words('french') and mot not in string.punctuation]
print(mots)

#Boucle pour ''islam'' et ''musulman''
for mot in mots: 
    "islam".append(mot)
    freq = Counter("islam") 
    freq = Counter("islam") 
    print(freq.most_common(50)) 
    print(len("islam"))

for mot in mots: 
    "musulm".append(mot)
    freq = Counter("musulm")
    freq = Counter("musulm") 
    print(freq.most_common(50)) 
    print(len("musulm"))