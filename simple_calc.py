#!/usr/bin/python3

def addition(x,y):
    return x + y
def multiply(x,y):
    return x * y
def subtract(x,y):
    return x - y
def division(x,y):
    return x / y

def calc():

    choice = input ("1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n")

    if choice == '1':
        x=int(input('1st number'))
        y=int(input('2nd number'))
        print(f'The result is: {addition(x,y)}')
    elif choice == '2':
        x=int(input('1st number'))
        y=int(input('2nd number'))
        print(f'The result is: {subtract(x,y)}')
    elif choice == '3':
        x=int(input('1st number'))
        y=int(input('2nd number'))
        print(f'The result is: {multiply(x,y)}')
    elif choice == '4':
        x=int(input('1st number'))
        y=int(input('2nd number'))
        print(f'The result is: {division(x,y)}')
    elif choice == 'exit':
        print("Goodbye!")
        exit()
    else:
        print('Wrong input, please try again!')
    return calc()

calc()
