'''
Created on May 20, 2019

@author: Nathan Liang
'''

import csv
with open('PreferredMetaphorJune18_TextProofreadTest.csv', 'r', newline='') as csvfile:
    nate_lang = csv.reader(csvfile, delimiter=',')
    for row in nate_lang:
        for idx in range(len(row)):
            if row[idx] != '':
                punct = row[idx][-1]
                if punct != '.' or punct != '!' or punct != '?':
                    row[idx] += '.'
with open('PunctChecked.csv', 'w+', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for idx in range(len(teachthoughts_tokens)):
        filewriter.writerow(teachthoughts_tokens[idx])

if __name__ == '__main__':
    pass