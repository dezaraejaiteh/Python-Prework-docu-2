#Please upload your answers to the 5 pre-work coding questions here.
#upload them as a .py file, a .ipynb file, or as a repo containing a .py or a .ipynb 
#The questions, if you need them:

#Coding Questions

#Complete the Coding Questions below in one .py file
#Create an account at https://github.com/

#Upload this file to github.com and submit the Git repository to the google classroom assignment.

#Watch this video walkthrough(Git/Github/Google Clasrrom)

#You will be turning in this assignment to your Google classroom. Please save your 5 functions to one .py file and demark the question numbers and the question in a comment above its respective function.

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"hello_{user_name}!")

    hello_name("Alice")
        
               
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

    def first_odds():
        for number in range(1, 101):
            if number % 2 != 0:
               print(number)
            
    first_odds()        
               

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

    def max_num_in_list(a_list):
        if not a_list:
            return None
        max_num = a_list(0)
        for num in a_list:
            if num > max_num:
                max_num = num
        return max_num

    number_list = [2,4,3,6,7,9]
    print(max_num_in_list(number_list))        

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

    def is_leap_year(a_year):
        if (a_year % 4 == 0 and a_year % 
    100 != 0) or (a_year % 400 == 0):
            return True
        else:
            return False
               
    print(is_leap_year(2024))      
    print(is_leap_year(2020))
    print(is_leap_year(2015))       

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

    def is_consecutive(a_list):
        if not a_list:

            return False
        sorted_list = sorted(a_list)
        for i in range(len(sorted_list) - 1):
        
            if sorted_list[i] + 1 !=
        sorted_list[i + 1]:
            return False
            return True
        
        print(is_consecutive([4,5,6,7,8]))
        print(is_consecutive([1,5,6,9]))
        