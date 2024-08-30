#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username.lower() == "admin" and password == 12345):
        print("Access granted")
    else:
        print("Access denied")

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        print("It's brisk out there!")
    elif (temperature >= 40 and temperature <= 65):
        print("It's a little chilly out there!")
    elif (temperature > 85):
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")

def fizzbuzz(num):
    # your code here
    if (num % 3 == 0 and num % 5 ==0):
        print("FizzBuzz")
        return "FizzBuzz"
    elif num % 3 == 0:
        print("Fizz")
        return "Fizz"
    elif num % 5 == 0:
        print("Buzz")
        return "Buzz"
    else:
        print(num)
        return num

def calculator(operation, num1, num2):
    # your code here
    if (operation == "+"):
        addition = num1 + num2
        print(addition)
        return addition
    elif (operation == "-"):
        subtraction = num1 - num2
        print(subtraction)
        return subtraction
    elif (operation == "*"):
        multiplication = num1 * num2
        print(multiplication)
        return multiplication
    elif (operation == "/"):
        division = num1 / num2
        print(division)
        return division
    else:
        print("Invalid operation!")
        return None

admin_login("ADMIN", 12345)
hows_the_weather(75)
fizzbuzz(30)
calculator("/", 4, 5)