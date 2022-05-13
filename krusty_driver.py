'''
Author: 
SID: 
Unikey: 
'''
import krusty
letter = input('New order [Y/N]: ')
letter_lowercase = letter.lower().strip() 
#saves the input in lower case.
order_num = 0
#set order num to 0 since orders haven't yet been taken.

while letter_lowercase != 'n': 
    if letter_lowercase == 'y':
        krusty.main() #prints everything in the main function of krusty.py.
        order_num +=1 # increment order number by one after order has been taken.
        letter = input('New order [Y/N]: ')
        letter_lowercase = letter.lower().strip()
    else: # if the input was not y or n.
        letter = input('New order [Y/N]: ')
        letter_lowercase = letter.lower().strip()
