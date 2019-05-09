#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The first line is a shebang.
# The python3 part could be bash, zsh, ruby, whatever
# There are many ways to do a shebang, this is the best!

"""
Created on Tue Jan 22 23:21:14 2019

@author: stbrb@mst.edu
"""

import sys
f = open(sys.argv[1], "r")
contents = f.read()
f.close()

f = open(sys.argv[2], "w")
f.write("Hello ")
f.write(contents)
f.close()
