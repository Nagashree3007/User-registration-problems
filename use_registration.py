'''

@Author: Nagashree C R
@Date: 2024-08-8-07
@Last Modified by: Nagashree C R
@Last Modified: 2024-08-07
@Title :User registration problems UC3-User need to enter a valid email.
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

def check_mail(gmail):
    if re.search( r'^[a-zA-Z0-9._%+-]+@bl\.co(\.in)?$',gmail):
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
                    flag=0
                    print(f'Your Name is saved as {first_name} {second_name}')
                    while flag!=1:
                        gmail=input('Enter the gmail: ')
                        if check_mail(gmail):
                            print(f'Your email is valid and saved as {gmail}')
                            break
                        else:
                            print(f"{gmail} is not valid \n please follow the rules:\n E.g. abc.xyz@bl.co.in \n 1.Email has 3 mandatory parts (abc, bl & co)\n 2.two optional (xyz & in) with precise @ and . positions")
                    flag=1
                    break
                else:
                    print(f"{second_name} is not valid \n please follow the rules:\n 1.second name starts with Cap  \n 2.enter minimum 3 characters")           
        else:
            print(f"{first_name} is not valid \n please follow the rules:\n 1.first name starts with Cap  \n 2.enter minimum 3 characters")
            
        
if __name__=='__main__':
    main()