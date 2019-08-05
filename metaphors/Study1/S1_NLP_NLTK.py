'''
Created on May 20, 2019

@author: Nathan Liang 
@contact: nathan.liang@duke.edu, 1nathan.liang@gmail.com, (503) 719-3275
@summary: NLP for Metaphor data (BRITE Lab)
'''

# ============== IMPORTS & DOWNLOADS ============== #

import csv
import nltk
import pandas as pd
import spellchecker
import re
from spellchecker import SpellChecker
from collections import Counter
#nltk.download('all-corpora')


# ============== DATA INITIALIZATION & PARSING ============== #

# Initialize the .csv file into either a list or a string.
def makeList(fname):
    '''
    Using the input document name,
    creates a list of strings:
    ['word1', 'word2', ..., 'wordn']
    '''
    with open(fname, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',') 
        finalList = []
        for row in filereader:
            finalList += row

def makeString(fname):
    '''
    Using the input document name,
    creates a single string.
    '''
    with open(fname, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        finalString = ''
        for row in filereader:
            for idx in range(len(row)):
                finalString += (row[idx] + ' ')
    return finalString

def proofread(finalList):
    spell = SpellChecker()
    misspelled = spell.unknown(finalList) 
    for word in misspelled:
        print(spell.correction(word))
        
    
# ============== TEXT WRANGLING ============== #

def stemWords(finalList,fname):
    '''
    Stem the words in file using the
    SnowballStemmer algorithm.
    '''
    from nltk.stem.snowball import SnowballStemmer
    stemmer = snowballStemmer("english")
    plurals = finalList
    singles = [stemmer.stem(plural) for plural in plurals]
    with open(fname, 'w+', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(singles)

def stopWords(lemmatized,fname):
    '''
    Removes the stop words from
    a given file and re-writes
    it as a new .csv file.
    '''
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_sentence = [w for w in lemmatized if not w in stop_words]
    with open(fname, 'w+', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(filtered_sentence)

# ============== NLP DESCRIPTIVES ============== #

def wordCount(finalList):
    '''
    Counts total
    number of words
    in the .csv file.
    '''
    text = finalList
    nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
    filtered = [w for w in text if nonPunct.match(w)]
    counts = Counter(filtered)
    print(counts)

def mostCommon(text,top):
    '''
    Prints the most common
    words in the file.
    '''
    fdist1 = nltk.FreqDist(text)
    topwords = fdist1.most_common(top)[0:]
    print("\n" + str(top) + " most common words:", topwords)

def commonContexts(targetWordList):
    '''
    Prints the most common slot-and-frame
    grammar for a given word in the file.
    '''
    print("\n" + "Common contexts for",targetWordList,": ")
    return text.common_contexts(targetWordList)

def similarWords(targetWord):
    """
    Prints the similar words surrounding the word for a given word in the file
    """
    print("\n" + "Similar words for '" + targetWord + "': ")
    return text.similar(targetWord)

# ============== MAIN BLOCK (FUNCTION CALLS) ============== #

if __name__ == '__main__':

    # Sculptor
    
    finalList = makeList('Tokenized_Gardener.csv')
    finalString = makeString('Tokenized_Gardener.csv')
    wordCount(finalList)

#     proofread(finalList)
    
#     finalList = makeList('Tokenized_Lemmatized_Top_Sculptor.csv')
#     stopWords(finalList,'Tokenized_Lemmatized_StopWorded_Top_Sculptor.csv')
#     token = finalString.split(' ')
#     text = nltk.Text(token)

    # Gardener
    '''
    finalList = makeList('Tokenized_Top_Gardener.csv')
    finalString = makeString('Tokenized_Top_Gardener.csv')
    lemmatizeWords(finalList,'Tokenized_Lemmatized_Top_Gardener.csv')
    finalList = makeList('Tokenized_Lemmatized_Top_Gardener.csv')
    stopWords('Tokenized_Lemmatized_Top_Gardener.csv','Tokenized_Lemmatized_StopWorded_Top_Gardener.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    '''

    # Coach
    '''
    finalList = makeList('Tokenized_Top_Coach.csv')
    finalString = makeString('Tokenized_Top_Coach.csv')
    lemmatizeWords(finalList,'Tokenized_Lemmatized_Top_Coach.csv')
    finalList = makeList('Tokenized_Lemmatized_Top_Coach.csv')
    stopWords(finalList,'Tokenized_Lemmatized_StopWorded_Top_Coach.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    '''

    # App Store
    '''
    finalList = makeList('Tokenized_Top_AppStore.csv')
    finalString = makeString('Tokenized_Top_AppStore.csv')
    lemmatizeWords(finalList,'Tokenized_Lemmatized_Top_AppStore.csv')
    finalList = makeList('Tokenized_Lemmatized_Top_AppStore.csv')
    stopWords(finalList,'Tokenized_Lemmatized_StopWorded_Top_AppStore.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    '''

    # Tour Guide
    '''
    finalList = makeList('Tokenized_Top_TourGuide.csv')
    finalString = makeString('Tokenized_Top_TourGuide.csv')
    lemmatizeWords(finalList,'Tokenized_Lemmatized_Top_TourGuide.csv')
    finalList = makeList('Tokenized_Lemmatized_Top_TourGuide.csv')
    stopWords(finalList,'Tokenized_Lemmatized_StopWorded_Top_TourGuide.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    '''

    # Captain
    '''
    finalList = makeList('Tokenized_Top_Captain.csv')
    finalString = makeString('Tokenized_Top_Captain.csv')
    lemmatizeWords(finalList,'Tokenized_Lemmatized_Top_Captain.csv')
    finalList = makeList('Tokenized_Lemmatized_Top_Captain.csv')
    stopWords(finalList,'Tokenized_Lemmatized_StopWorded_Top_Captain.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    '''

    # Personal
    '''
    finalList = makeList('Tokenized_Top_Personal.csv')
    finalString = makeString('Tokenized_Top_Personal.csv')
    lemmatizeWords(finalList,'Tokenized_Lemmatized_Top_Personal.csv')
    finalList = makeList('Tokenized_Lemmatized_Top_Personal.csv')
    stopWords(finalList,'Tokenized_Lemmatized_StopWorded_Top_Personal.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    '''
