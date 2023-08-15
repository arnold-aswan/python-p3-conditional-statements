#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if ((username == 'admin' or username == 'ADMIN') and password == '12345'):
        return 'Access granted'
    else:
        return "Access denied"


def hows_the_weather(temperature):
    # your code here
    match temperature:
        case (temperature) if temperature > 85:
            return "It's too dang hot out there!"
        case (temperature) if temperature <= 65 and temperature >= 40:
            return "It's a little chilly out there!"
        case (temperature) if temperature < 40:
            return "It's brisk out there!"
        case _:
            return "It's perfect out there!"


def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    # your code here
    match operation:
        case (operation) if operation == "+":
            return num1 + num2
        case (operation) if operation == "-":
            return num1 - num2
        case (operation) if operation == "/":
            return num1 / num2
        case (operation) if operation == "*":
            return num1 * num2
        case _:
            print('Invalid operation!')
            return None
