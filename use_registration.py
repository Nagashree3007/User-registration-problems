'''

@Author: Nagashree C R
@Date: 2024-08-8-07
@Last Modified by: Nagashree C R
@Last Modified: 2024-08-07
@Title :User registration problems UC1-User need to enter a valid First Name

'''

import re 


def check_firtname(first_name):
    '''
       Definition:
       The check_firstname function is designed to validate a given first name based on specific criteria.
       Parameters:
       first_name (str): A string representing the first name to be checked.
       Return:
       1 if the first_name is at least 3 characters long and starts with an uppercase letter.
       0 otherwise.
    
    '''
    x=re.search(r"\b[A-Z]",first_name)
    if len(first_name)>=3 and x:
        return 1
    else:
        return 0
        
def main():
    first_name=input("Enter your first name : ")
    if check_firtname(first_name):
        print(f"{first_name} is valid")
    else:
        print(f"{first_name} is not valid \n please follow the rules:\n 1.First name starts with Cap  \n 2.enter minimum 3 characters")
        
    
        
if __name__=='__main__':
    main()