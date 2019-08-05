'''
Created on July 27, 2019

@author: Nathan Liang, BRITE Lab
@contact: nathan.liang@duke.edu, 1nathan.liang@gmail.com, (503) 719-3275
@summary: Natural language Processing for Preferred Metaphor June 2018
'''
import csv
import nltk
'''nltk.download('all-corpora')'''

# Reading preferred metaphor CSV
with open('metaphorthoughts_study3_raw.csv', 'r+', newline='', encoding="utf8") as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    metaphorthink_tokens = []
    for row in filereader:
        metaphorthink_tokens.append(nltk.word_tokenize(row[0])) #1

# Writing preferred metaphor .csv for 'x' tokens
with open('metaphorthoughts_study3_tokenized.csv', 'w+', newline='', encoding="utf8") as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(metaphorthink_tokens)):
        filewriter.writerow(metaphorthink_tokens[idx])
          
if __name__ == '__main__':
    pass