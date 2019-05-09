#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:14:12 2019

@author: stbrb@mst.edu
"""
# Simple Substitution Cipher Hacker, but better
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import timeit, sys, re, freqAnalysis
from urllib.request import urlopen
from urllib.error import URLError

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ .'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    start = timeit.default_timer()
       
    f = open(sys.argv[1], "r")
    message = f.read()
    f.close()   
    
    # Determine the possible valid ciphertext translations:
   # print('Hacking...')
    
    isOnInternet, hackedBook = checkInternet(message)
    
    if isOnInternet == True:
        hackedMessage = hackedBook
    else: 
        print(":(")
        #replace the message using frequency analysis
        freqLetterMapping = freqMapping(message)
       # frequentMessage, updatedMap = replaceLetters(message, freqLetterMapping);  
    
        #newMap = hackSimpleSub(frequentMessage)
        #print(newMap)
        #wordPatternMessage = decryptWithCipherletterMapping(frequentMessage, newMap)
       
        hackedMessage = BruteForceLetters(message, freqLetterMapping)
    
    f = open(sys.argv[2], "w")
    f.write(hackedMessage)
    f.close()
    
    stop = timeit.default_timer();
    print("Run Time:", stop - start, "seconds")
    
def freqMapping(message):
    #get a blank letter mapping
    freqMap = getBlankCipherletterMapping()
    #find the order of the most frequent letters in the encrypted message
    freqOrder = freqAnalysis.getFrequencyOrder(message)
    
    #create a string containing the most frequent chars in english language
    mostFrequent = ' ETAION'
        
    for i in freqOrder[:4]: #loop through the most common chars
        addedChar = False #create a bool to know if the current char has been added to the mapping
        for j in mostFrequent: #loop through the most frequent chars
            if freqMap[j] == []: #if the frequent map is empty for this char
                if i not in freqMap[j] and addedChar == False: #if the char is not in the map and a char hasnt been added
                    freqMap[j].append(i) #append the char into the map
                    addedChar = True #do not add this char anymore
                     
    return freqMap
                    
def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': [], ' ': [], '.': []}

def replaceLetters(message, letterMapping):
    
    print(letterMapping)
    newMessage = ''
    for letter in message: #loop through each letter of the message
        addedChar = False
        for key, value in letterMapping.items(): #loop through the key/value pairin the mapping
            if letter.upper() in value: #if the letter is equal to the value in the mapping
                if letter.isupper():
                    newMessage += key.upper()
                    addedChar = True
                    #newMessage = newMessage.replace(letter, key.upper()) #replace the message letter with the key value
                else:
                    newMessage += key.lower()
                    addedChar = True
                    #newMessage = newMessage.replace(letter, key.lower())
                if addedChar == False:
                        newMessage += letter      
              
    #remove letters from map have been successfully replaced
    #for key, value in dict(letterMapping).items(): #loop through map
     #   if value != []: #if the value has a letter in its mapping
      #      del letterMapping[key] #delete it from the map
                
    return newMessage, letterMapping #return the message and new letterMapping

def BruteForceLetters(message, letterMapping):
    n =''
    foundAMatch = False
    projectString = 'The Project Gutenberg EBook'
    
    #account for random char at the beginning of a file
    if message[:1] not in LETTERS:
        messageStart = message[1:28]
    else:
        messageStart = message[:27]
    #map the string to the encrypted letters
    for i,j in zip(messageStart, projectString):
            for key, value in letterMapping.items():
                if j.upper() == key and value == []:
                    letterMapping[key].append(i.upper())
    
    #attempt to brute force 'w'
    for i in range(len(message) - 1):
        if message[i + 1] == message[i] and message[i] == message[i-1]: #if it is a series of the same letter
            if message[i-2] == "/": #and the next char is a slash
                foundAMatch = True #its 'w'
                letter = message[i] #grab the encrypted char
        #if message[i+1] == '"':
         #   n += message[i]
        #if message[i+1] == "\n":
        #    n += message[i]
        #if message[i+1] == ' ' and message[i+2].isupper():
         #   n += message[i]
    
    #map the char to 'w'
    if foundAMatch == True:
        letterMapping['W'].append(letter.upper())
    
    
        
    #freq = freqAnalysis.getFrequencyOrder(n);   
    #letterMapping['.'].append(freq[0])
    
    #print(n)
   # print(letterMapping)
    
    newMessage, letterMap = replaceLetters(message, letterMapping)
    
    return newMessage


def checkInternet(message):
    bookNumber = ''
    isOnInternet = False
    bestURL = ''
    contents = ''
    
    #find all of  the chars between # and ]
    book = message[message.find('#'):message.find(']')]
    bookNumber = book[1:] #remove '#' from the string
    
    #two possible ways books are stored on the gutenberg website
    gutenbergWebsite0 = 'http://www.gutenberg.org/files/?/?-0.txt'
    gutenbergWebsite1 = 'http://www.gutenberg.org/cache/epub/?/pg?.txt'

    #replace the urls with the book number
    url0 = gutenbergWebsite0.replace('?', bookNumber)
    url1 = gutenbergWebsite1.replace('?', bookNumber)

#attempt to load the web page
    try:
        urlopen(url0, timeout=10)
        isOnInternet = True
        bestURL = url0
    except URLError as err:
        try:
           urlopen(url1, timeout=10)
           isOnInternet = True
           bestURL = url1
        except URLError as err:
            isOnInternet = False
               
    #if the page was found, grab the book and throw it into contents
    if isOnInternet == True:
        with urlopen(bestURL) as data:
            for line in data:
                line = line.decode('utf-8')
                contents += line
    
    #used to test if the internet strategy fails
    #isOnInternet = False
    
    return isOnInternet, contents

if __name__ == '__main__':
    main()