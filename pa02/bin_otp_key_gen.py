#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:30:12 2019

@author: stbrb@mst.edu
"""
import sys, secrets

def main():
    
    f = open(sys.argv[1], "w") #open the 'keyfile.sec'
    
    for i in range(1, 501): #loop through 500 OTP keys
        otpKey = '' #initialize the key to an empty string
        for j in range(2048): #loop through the length that the key should be
            otpKey = otpKey + secrets.choice('01') #add the randomly gen'd secrets 
        f.write('%s %s\n' % ('{:03d}'.format(i), otpKey)) #write the key to the file   
    
    f.close() #close the file


if __name__ == '__main__':
    main()