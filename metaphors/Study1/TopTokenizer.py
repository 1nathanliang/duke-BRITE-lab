'''
Created on May 18, 2019

@author: Nathan Liang, BRITE Lab
@contact: nathan.liang@duke.edu, 1nathan.liang@gmail.com, (503) 719-3275
@summary: Natural language Processing for Preferred Metaphor June 2018
'''
import csv
import nltk
'''nltk.download('all-corpora')'''

# Reading preferred metaphor CSV
with open('New_Top45.csv', 'r', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    sculptor_tokens = []
    gardener_tokens = []
    coach_tokens = []
    appstore_tokens = []
    tourguide_tokens = []
    captain_tokens = []
    personal_tokens = []
    for row in filereader:
        sculptor_tokens.append(nltk.word_tokenize(row[0])) #1
        gardener_tokens.append(nltk.word_tokenize(row[1])) #2
        coach_tokens.append(nltk.word_tokenize(row[2])) #3
        appstore_tokens.append(nltk.word_tokenize(row[3])) #4
        tourguide_tokens.append(nltk.word_tokenize(row[4])) #5
        captain_tokens.append(nltk.word_tokenize(row[5])) #6
        personal_tokens.append(nltk.word_tokenize(row[6])) #7

# Writing preferred metaphor .csv for 'x' tokens
with open('Tokenized_Top_Sculptor.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(sculptor_tokens)):
        filewriter.writerow(sculptor_tokens[idx])
        
with open('Tokenized_Top_Gardener.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(gardener_tokens)):
        filewriter.writerow(gardener_tokens[idx])
        
with open('Tokenized_Top_Coach.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(coach_tokens)):
        filewriter.writerow(coach_tokens[idx])
        
with open('Tokenized_Top_AppStore.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(appstore_tokens)):
        filewriter.writerow(appstore_tokens[idx])

with open('Tokenized_Top_TourGuide.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(tourguide_tokens)):
        filewriter.writerow(tourguide_tokens[idx])
        
with open('Tokenized_Top_Captain.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(captain_tokens)):
        filewriter.writerow(captain_tokens[idx])
        
with open('Tokenized_Top_Personal.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(
        csvfile, 
        delimiter=',', 
        quotechar='|', 
        quoting=csv.QUOTE_MINIMAL
    )
    for idx in range(len(personal_tokens)):
        filewriter.writerow(personal_tokens[idx])  
          
if __name__ == '__main__':
    pass
    