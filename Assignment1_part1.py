#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ListDivideException(Exception):
    """An error occurred"""
    
def listDivide(numbers, divide = 2):
    cnt = 0
    for num in numbers:
        if  num % divide == 0: 
            cnt += 1
            
    return(cnt)

def testlistDivide():
    try:
        print(listDivide([1, 2, 3, 4, 5]))
        print(listDivide([2, 4, 6, 8, 10]))
        print(listDivide([30, 54, 63, 98, 100], divide=10))
        print(listDivide([]))
        print(listDivide([2, 4, 6, 8, 10], 1))
    except ListDivideException: 
        print("InvalidInputError:")
        
            

testlistDivide()


    
    

