'''

@Author: Nagashree C R
@Date: 2024-08-8-07
@Last Modified by: Nagashree C R
@Last Modified: 2024-08-07
@Title :User registration problems UC6-User need to follow pre-defined Password rules.
        Rule2– Should have at least 1 Upper Case

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
    """
    Definition:
        Prompts user for a email and validates its format.
    Parameters:
           None
    Return:
           None
        
    """
    while True:
        gmail=input('Enter the gmail: ')
        if re.search(r'\b[A-Z].*@bl.co.*',gmail):
            print(f'Your email is valid and saved as {gmail}')
            break
        else:
            print(f"{gmail} is not valid \n please follow the rules:\n E.g. abc.xyz@bl.co.in \n 1.Email has 3 mandatory parts (abc, bl & co)\n 2.two optional (xyz & in) with precise @ and . positions")           

def check_phonenumber():
    """
    Definition:
        Prompts user for a phone number and validates its format  and Confirms the number with the user before saving it.
    Parameters:
           None
    Return:
           None
        
    """
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
            print("you have entered wrong phone number format reffer the E.g. 91 9919819801 - Country code follow by space and re enter the ph.number")
            

def check_password():
    """
    Definition:
        Prompts user for a password and confirms it and Ensures the password is 
        1.at least 8 alphanumeric characters long
        2.Should have at least 1 Upper Case
    Parameters:
           None.
    Return:
           None.
        
    """
    while True:
        password = input("Enter your password: ")
        # Improved regex for at least 8 alphanumeric characters
        pattern = r'(?=.*[A-Z]).[A-Za-z0-9]{8,}$'
        
        if re.search(pattern, password):
            while True:
                confirm = input("Confirm your password: ")
                if password == confirm:
                    print(f'Your password is saved as: {password}')
                    return  # Exit both loops
                else:
                    print("Password did not match. Please try again.")
        else:
            print('Invalid password. 1.It must be at least 8 alphanumeric characters long.\n 2.Should have at least 1 Upper Case')

          
def main():
    perform()
    check_email()
    check_phonenumber()
    check_password()
        
if __name__=='__main__':
    main()
    print("Thanks for the information....your data is sucessfully saved")