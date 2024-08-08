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


def perform():
    '''
    
    Definition:
          function prompts the user to input their first and second names, validates each using the check_name
    parameters:
           None
    return:
           None
    
    '''
    first_name=input("Enter your first name : ")
    if check_name(first_name):
        while True:
            second_name=input("Enter your second name : ")
            if check_name(second_name):
                print(f'Your Name is saved as {first_name} {second_name}')
                return first_name,second_name
            else:
                print(f"{first_name} is not valid \n please follow the rules:\n 1.First name starts with Cap  \n 2.enter minimum 3 characters")           
    else:
        print(f"{first_name} is not valid \n please follow the rules:\n 1.First name starts with Cap  \n 2.enter minimum 3 characters")
        perform()
        
def check_email():
    while True:
        gmail=input('Enter the gmail: ')
        if re.search(r'\b[A-Z].*@bl.co.*',gmail):
            print(f'Your email is valid and saved as {gmail}')
            break
        else:
            print(f"{gmail} is not valid \n please follow the rules:\n E.g. abc.xyz@bl.co.in \n 1.Email has 3 mandatory parts (abc, bl & co)\n 2.two optional (xyz & in) with precise @ and . positions")           
            
def main():
    perform()
    check_email()
    while True:
        phone_num=input('Enter present working contact number :')
        if re.search(r'^\+?[0-9]{2}\s[0-9]{10}$',phone_num):
            print(f'your contact number is {phone_num}')
            verify=int(input("Are you sure about the number you gave???...if no please enter 1 else 0  :"))
            if verify==1:
                pass
            else:
                print(f'your contact number is saved as {phone_num}')
                break
        else:
            print()
    
if __name__=='__main__':
    main()
    print("Thanks for the information....your data is sucessfully saved")