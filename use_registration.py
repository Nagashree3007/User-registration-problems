'''

@Author: Nagashree C R
@Date: 2024-08-8-07
@Last Modified by: Nagashree C R
@Last Modified: 2024-08-07
@Title :User registration problems UC2- User need to enter a valid Last Name - Last name

'''

import re 


def check_name(name):
    '''
       Definition:
       The check_name function is designed to validate a given first/last name based on specific criteria.
       Parameters:
       name (str): A string representing the first/last name to be checked.
       Return:
       1 if the first_name/second_name is at least 3 characters long and starts with an uppercase letter.
       0 otherwise.
    
    '''
    x=re.search(r"\b[A-Z]",name)
    if len(name)>=3 and x:
        return 1
    else:
        return 0
        
def main():
    flag=0
    while flag!=1:
        first_name=input("Enter your first name : ")
        if check_name(first_name):
            flag=1
            while flag!=0:
                second_name=input("Enter your second name : ")
                if check_name(second_name):
                    flag=1
                    print(f'Your Name is saved as {first_name} {second_name}')
                    break
                else:
                    print(f"{second_name} is not valid \n please follow the rules:\n 1.second name starts with Cap  \n 2.enter minimum 3 characters")           
        else:
            print(f"{first_name} is not valid \n please follow the rules:\n 1.first name starts with Cap  \n 2.enter minimum 3 characters")
            
        
        
if __name__=='__main__':
    main()