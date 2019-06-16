'''
Created on May 20, 2019

@author: Nathan Liang
Linguistic Analyses
'''
import csv, nltk

# Initialize the .csv file into either a list or a string.
def makeList(fname):
    '''
    Using the input 
    document name,
    creates a list 
    of strings.
    '''
    with open(fname, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        finalList = []
        for row in filereader:
            finalList += row
    return finalList
            
def makeString(fname):
    '''
    Using the input 
    document name,
    creates a 
    single string.
    '''
    with open(fname, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        finalString = ''
        for row in filereader:
            for idx in range(len(row)):
                if row[idx] != '.':
                    finalString += (row[idx] + ' ')
                else:
                    finalString -= (' ')
                    finalString += ('. ')
    return finalString

# Text wrangling
def stemWords(finalList,fname):
    '''
    Stem words in file
    '''
    stemmer = nltk.PorterStemmer()
    plurals = finalList
    singles = [stemmer.stem(plural) for plural in plurals]
    singles = ' '.join(singles)
    with open(fname, 'w+', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(singles)

# Remove stop words in file
def stopWords(finalList,fname):
    '''
    Removes the stop words from
    a given file and re-writes 
    it as a new .csv file.
    '''
    stop_words = set(nltk.corpus.stopwords.words('english'))  
    filtered_sentence = [w for w in finalList if not w in stop_words]
    with open(fname, 'w+', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(filtered_sentence)

# NLP Analyses: Descriptives
def wordCount():
    '''
    Counts total 
    number of words 
    in the .csv file.
    '''
    print("Total word count is: " + "???")

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

# n-Gram Analyses
def bigram():
    new_trigrams = []
    c = 2
    while c < len(token) - 2:
        new_trigrams.append((token[c], token[c+1], token[c+2]))
        c += 2
    print(new_trigrams)
    
if __name__ == '__main__':
    
    # Teacher Thoughts
    '''
    finalList = makeList('Tokenized_TeachThoughts.csv')
    finalString = makeString('Tokenized_TeachThoughts.csv')
    stopWords(finalList, 'Tokenized_StopWorded_TeachThoughts.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_TeachThoughts.csv')
    finalString = makeString('Tokenized_StopWorded_TeachThoughts.csv')
    '''
    
    # Sculptor
    # '''
    finalList = makeList('Tokenized_Top_Sculptor.csv')
    finalString = makeString('Tokenized_Top_Sculptor.csv')
    stopWords(finalList, 'Tokenized_StopWorded_Top_Sculptor.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_Top_Sculptor.csv')
    finalString = makeString('Tokenized_StopWorded_Top_Sculptor.csv')
    # '''
    
    # Gardener
    # '''
    finalList = makeList('Tokenized_Top_Gardener.csv')
    finalString = makeString('Tokenized_Top_Gardener.csv')
    stopWords(finalList, 'Tokenized_StopWorded_Top_Gardener.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_Top_Gardener.csv')
    finalString = makeString('Tokenized_StopWorded_Top_Gardener.csv')
    # '''
    
    # Coach
    # '''
    finalList = makeList('Tokenized_Top_Coach.csv')
    finalString = makeString('Tokenized_Top_Coach.csv')
    stopWords(finalList, 'Tokenized_StopWorded_Top_Coach.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_Top_Coach.csv')
    finalString = makeString('Tokenized_StopWorded_Top_Coach.csv')
    # '''
    
    # App Store
    # '''
    finalList = makeList('Tokenized_Top_AppStore.csv')
    finalString = makeString('Tokenized_Top_AppStore.csv')
    stopWords(finalList,'Tokenized_StopWorded_Top_AppStore.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_Top_AppStore.csv')
    finalString = makeString('Tokenized_StopWorded_Top_AppStore.csv')
    # '''
    
    # Tour Guide
    # '''
    finalList = makeList('Tokenized_Top_TourGuide.csv')
    finalString = makeString('Tokenized_Top_TourGuide.csv')
    stopWords(finalList,'Tokenized_StopWorded_Top_TourGuide.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_Top_TourGuide.csv')
    finalString = makeString('Tokenized_StopWorded_Top_TourGuide.csv')
    # '''
    
    # Captain
    # '''
    finalList = makeList('Tokenized_Top_Captain.csv')
    finalString = makeString('Tokenized_Top_Captain.csv')
    stopWords(finalList,'Tokenized_StopWorded_Top_Captain.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_Top_Captain.csv')
    finalString = makeString('Tokenized_StopWorded_Top_Captain.csv')
    # '''
    
    # Personal
    # '''
    finalList = makeList('Tokenized_Top_Personal.csv')
    finalString = makeString('Tokenized_Top_Personal.csv')
    stopWords(finalList,'Tokenized_StopWorded_Top_Personal.csv')
    token = finalString.split(' ')
    text = nltk.Text(token)
    finalList = makeList('Tokenized_StopWorded_Top_Personal.csv')
    finalString = makeString('Tokenized_StopWorded_Top_Personal.csv')
    # '''
    
