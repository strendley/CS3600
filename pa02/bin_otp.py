#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:47:56 2019

@author: stbrb@mst.edu
"""

import sys

def main():
    keyFile = sys.argv[1] #grab all inputs
    keyNum = sys.argv[2]
    inFile = sys.argv[3]
    outFile = sys.argv[4]
    
    convertedString = convertInput(inFile) #convert the input file into binary
    binaryString = getOtpKey(keyFile, keyNum) #grab the otpkey corresponding to keynum
    XORString= XOR(convertedString, binaryString) #perform XOR on strings
    translated = ASCII(XORString) #translate XOR'd string into ASCII 
    
    f = open(outFile, "w") #write the encrypted message to the outfile
    f.write(translated)
    f.close()

    
def convertInput(inFile):
    f = open(inFile, mode='r', encoding='utf-8-sig') #read in the input file
    inf = f.read()
    f.close()

    #if encoding, the length may be greater than 256 because of newline char???
    if len(inf) > 256:
        for letter in inf: #if there are any newline characters, remove them
            if letter == '\n':
                inf = inf.replace('\n', '')
    
    #convert the string into binary
    converted = ' '.join('{0:08b}'.format(ord(i), 'b') for i in inf)  
    
    #remove all spaces from the string
    converted = converted.replace(' ', '')
    return converted
    
def getOtpKey(keyFile, keyNum):
    #read in the keyfile
    f = open(keyFile, "r")
    key = f.read()
    f.close()
    
    #check how the user inputs the keynum
    intKeyNum = int(keyNum)
    
    #add 0's to the front for consistency with the keyfile
    if intKeyNum < 10:
        num = '00' + str(intKeyNum)
    elif intKeyNum < 100:
        num = '0' + str(intKeyNum)
    else:
        num = keyNum
    
    #grab the otpkey corresponding to the keynum
    otp = key[key.find(num) + 4 : key.find(num) + 2052]
    
    return otp

def XOR(convertedString, binaryString):  
    #convert the strings into ints and XOR them
    result = int(convertedString, 2) ^ int(binaryString, 2) 
    
    #convert/format the result back into binary string
    XORString = bin(result)[2:].zfill(len(convertedString))
      
    return XORString
    
def ASCII(XORString):
  
    translated = ''
    for i in range(0,len(XORString),8): #from the start to the finish, every 8 chars
        translated += chr(int(XORString[i:i+8],2)) #convert the 8-bit string into ascci
    
    #print(translated)    
    return translated
    
    
if __name__ == '__main__':
    main()