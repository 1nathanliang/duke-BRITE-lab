'''
Created on July 27, 2019

@author: Nathan Liang 
@contact: nathan.liang@duke.edu, 1nathan.liang@gmail.com, (503) 719-3275
@summary: NLP for Metaphor data (BRITE Lab)
'''

# ============== IMPORTS & DOWNLOADS ============== #

import csv
import nltk
from nltk.util import ngrams
import pandas as pd
import spellchecker
import re
from spellchecker import SpellChecker
from collections import Counter
#nltk.download('all-corpora')


# ============== DATA INITIALIZATION & PREPROCESSING ============== #

# Initialize the .csv file into either a list or a string.
def makeList(fname):
    '''
    Using the input document name,
    creates a list of strings:
    ['word1', 'word2', ..., 'wordn']
    '''
    with open(fname, 'r+', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',') 
        finalList = []
        for row in filereader:
            finalList += row
    finalList = [word.lower() for word in finalList]
    return finalList

def makeString(fname):
    '''
    Using the input document name,
    creates a single string.
    '''
    with open(fname, 'r+', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        finalString = ''
        for row in filereader:
            for idx in range(len(row)):
                finalString += (row[idx].lower() + ' ')
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

def stopWords(lemmatized):
    '''
    Removes the stop words from
    a given file and re-writes
    it as a new .csv file.
    '''
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_sentence = [w for w in lemmatized if not w in stop_words]
    custom = ['teacher', 'student', 'teachers', 'students']
    newfiltered_sentence = [w for w in filtered_sentence if not w in custom]
    return newfiltered_sentence
#     with open(fname, 'w+', newline='') as csvfile:
#         filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         filewriter.writerow(filtered_sentence)


# ============== NLP DESCRIPTIVES ============== #

def wordCount(finalList):
    '''
    Returns counts of word
    frequencies for every word
    in finalList.
    '''
    text = finalList
    nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
    filtered = [w for w in text if nonPunct.match(w)]
    counts = Counter(filtered)
    print('MOST COMMON WORDS:')
    for elt, count in counts.most_common(len(counts)):
        print('%s: %7d' % (elt, count))

def similarWords(targetWordList,targetWord):
    """
    Prints the similar words surrounding the word for a given word in the file
    """
    print("\n" + "Similar words for '" + targetWord + "': ")
    text = nltk.Text(targetWordList)
    print(text.similar(targetWord))

def commonContexts(targetWordList,targetWords):
    '''
    Prints the most common slot-and-frame
    grammar for a given word in the file.
    '''
    print("\n" + "Common contexts: ")
    text = nltk.Text(targetWordList)
    print(text.common_contexts(targetWords))

def nGrams(finalList,n):
    nGrams = ngrams(finalList,n)
    nGramsFreq = Counter(nGrams)
    mostCommon = nGramsFreq.most_common(len(nGramsFreq))
    for gram in mostCommon:
        print(gram)
    
# ============== MAIN BLOCK (FUNCTION CALLS) ============== #

if __name__ == '__main__':

    finalList = makeList('metaphorthoughts_study3_tokenized.csv')
    finalString = makeString('metaphorthoughts_study3_tokenized.csv')
#     wordCount(stopWords(finalList))
    nGrams(finalList,2)
#     token = finalString.split(' ')
#     text = nltk.Text(token)

