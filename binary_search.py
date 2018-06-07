#binary search
import numpy as np

def binarysearch(filename,num):
    handle = open(filename,'r')
    contents = handle.readlines()
    string = contents[0]  
    if string.find(str(num)) == -1:
        print(num,'is not found in this file')
    else:
        print(num,'is in this file')

binarysearch('test.txt',23)





















