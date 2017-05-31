filename='pi_million_digits.txt'

with open(filename) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string+=line.rstrip()

birthday=input("Enter your birthday, in the from yymmdd: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


import json

filename='username.json'

try:
    with open(filename) as f_obj:
        username=json.load(f_obj)
except FileNotFoundError:
    username=input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+username+"!")
else:
    print("Welcome back, "+username+"!")

