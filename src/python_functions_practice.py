def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x // y

def length_of_string(string):
    return len(string)

def join_string(first_str, second_str):
    return first_str + second_str

def add_string_as_number(first_str, second_str):
    return int(first_str) + int(second_str)

#   I've got the list out of the functions in order to use them in both.
#   I couldn't find any shorter solution
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(number):
    return months[number -1]

def number_to_short_month_name(number):
    month_name = months[number -1]
    return month_name[0:3]

def volume_of_cube(side):
    return side * side * side

def reverse_string(word):
    list_of_chars = [char for char in word]
    list_of_chars.reverse()

    reversed_string = ""

    for char in list_of_chars:
        reversed_string += char
    return reversed_string

    # solution from w3schools but returns None
    # check later on with different functions
# def reverse_string(word):
#     txt = word
#     print(txt[::-1])

#   mentor solution
# def string_reverse(str):
#     string_reversed = ''
#     index = len(str)

#     while index > 0:
#         string_reversed = string_reversed + str [ index -1 ]
#         index = index -1

#     return string_reversed    

def fahrenheit_to_celcius(temperature):
    return round((temperature - 32) * 5/9)