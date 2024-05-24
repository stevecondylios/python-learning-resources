

As always, this is a working doc. An attempt to summarise the learnings from [*Learn Python the Hard Way*](https://learnpythonthehardway.org/python3/)

- Unclear where this belongs, but my Google doc python notes: https://docs.google.com/document/d/1Io9lLJuSm58cXrBIpVhbu6_u7w3BZ3fG0eWbQBhrSD0/edit


### Some tidbits


- Make a file called `test.py`, inside it, place `print(2 * 2)`, in the terminal type `python3 test.py`, and that should print 4 to the screen.

- You can start python in the terminal with `python3`, but also something like `python3.8` (note: apparently on [windows](https://learnpythonthehardway.org/python3/ex1.html) you always type `python` rather than `python3`). 


### Notes from LPTHW


```py
# Multiple arguemnts to print() will print them space-separated
print("hi there", 3 + 2)
# hi there 5

print("Is it greater?", 5 > -2)
# Is it greater? True


round(1.73333)
# 2


# f-strings
pet = "dog"
f"my pet {avariable}"
# 'my pet dog'

# Another way is to use .format()
formatter.format("jane", 22)
"My name's jane, I'm 22 years old"

print("." * 10)
..........

# More printing form derek banas: https://www.youtube.com/watch?v=H1elmMBnykA&t=15m45s

print(12, 21, 1974, sep="/")
# 12/21/1974

# Triple quoting allows you to use quotes 
'''something with a 'quote', cool'''
# "something with a 'quote', cool


# To get the type (which I think's a synonym for class)
type(5.4)
# <class 'float'>

# Convert (AKA "cast") to string
str(5.4)


# NOTE: chr() *I think* grabs the i'th ASCII character
chr(97)
# 'a'
chr(98)
# 'b' ... etc 

# Escaping works as you'd expect	
str = "Some text \t \n \' \" \\, see!"
print(str)
# Some text 	
#  ' " \, see! 


# More formatting capabilities. From Derek: https://www.youtube.com/watch?v=H1elmMBnykA&t=17m15s
print("\n%04d %s %.2f %c" % (1, "John", 1.234, 'A'))
# 
# 0001 John 1.23 A


# Some imports
import sys
import math
import random
import threading
import time
from functools import reduce

# Derek's code in full: https://github.com/derekbanas/PythonTutorial/blob/main/pythontut.py

"""
Multi-line
Comment
"""





```




MY TODO LIST

- How to tell an object's class/type
- how to convert "5" to interger, float
- How to define a dict/hash, or whatever it's called
- How to look up documentation for a method (e.g. .format())
- Is there an interactive debugger? 



