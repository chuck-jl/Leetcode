class Solution(object):
def no_duplicates_no_structures(str):
    
""" Now without using additional data structures """

    
    for letter in str:
        
        if str.count(letter) > 1:
            
           return False
    
    else:
        
        return True
