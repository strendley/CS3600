#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:10:47 2019

@author: stbrb@mst.edu
"""
import crypt, os, sys

def main():
    hashedBossPass = sys.argv[1]
    salt = sys.argv[2]
    crackedPass = ""
       
    f = open('/usr/share/john/password.lst')
    
    for line in f:
        if hashedBossPass == crypt.crypt(line[:-1], salt):
            crackedPass = line[:-1]
            break
    f.close()
    

    print(crackedPass)



if __name__ == '__main__':
    main()