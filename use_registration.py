'''

@Author: Nagashree C R
@Date: 2024-08-8-07
@Last Modified by: Nagashree C R
@Last Modified: 2024-08-07
@Title :User registration problems UC4-User need to follow pre-defined Mobile Format 
        - E.g. 91 9919819801 - Country code follow by space

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
                  
def check_phonenumber(phone_num):
    if re.search(r'^\+?[0-9]{2}\s[0-9]{10}$',phone_num):
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
                            flag=1
                            while flag!=0:
                                phone_num=input('Enter present working contact number :')
                                if check_phonenumber(phone_num):
                                    flag=1
                                    print(f'your contact number is {phone_num}')
                                    verify=int(input("Are you sure about the number you gave???...if no please enter 1 else 0  :"))
                                    if verify==1:
                                        pass
                                    else:
                                        print(f'your contact number is saved as {phone_num}')
                                        break
                                else:
                                    print("you have entered wrong phone number format reffer the E.g. 91 9919819801 - Country code follow by space and re enter the ph.number") 
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
    print("Thanks for the information....your data is sucessfully saved")