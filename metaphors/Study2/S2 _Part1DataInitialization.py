'''
Created on July 27, 2019

@author: Nathan Liang, BRITE Lab
@contact: nathan.liang@duke.edu, 1nathan.liang@gmail.com, (503) 719-3275
@summary: Natural language Processing for Preferred Metaphor June 2018
'''
import csv
import nltk
'''nltk.download('all-corpora')'''

def initializeData(rfname, condition, wfname,):
    # Reading preferred metaphor CSV
        with open(rfname, 'r+', newline='', encoding='utf8') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',')
            metaDict = {}
            allTokens = []
            next(filereader)
            for row in filereader:
                metaType = row[2]
                responses = row[7]
                if metaType not in metaDict:
                    metaDict[metaType] = []
                if metaType == condition:
                    metaDict[condition].append(nltk.word_tokenize(responses))
                else:
                    allTokens.append(nltk.word_tokenize(responses))
        with open(wfname, 'w+', newline='', encoding='utf8') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            if condition != 'all':
                for idx in range(len(metaDict[condition])):
                    filewriter.writerow(metaDict[condition][idx])
            else:
                for idx in range(len(allTokens)):
                    filewriter.writerow(allTokens[idx])
            
if __name__ == '__main__':
    initializeData('FINAL_mTurk_Under30_Data.csv', 'all', 'S2_Tokenized_All.csv')
    initializeData('FINAL_mTurk_Under30_Data.csv', 'sculptor', 'S2_Tokenized_Sculptor.csv')
    initializeData('FINAL_mTurk_Under30_Data.csv', 'coach', 'S2_Tokenized_Coach.csv')
    initializeData('FINAL_mTurk_Under30_Data.csv', 'gardener', 'S2_Tokenized_Gardener.csv')
    initializeData('FINAL_mTurk_Under30_Data.csv', 'tourguide', 'S2_Tokenized_TourGuide.csv')
    
    