#
#
# ##Variables - use to temporary store data into computer's memory
# #1.Define variable
# price = 10
# #2. Print Variable
# print(price)
#
# #boolean values example
# is_active = True
# print ('is_active',' ',is_active) #Concatenate strings
#
#
#
# ##TEST
# Name = 'John Smith'
# Age = 20
# Is_New = True
#
# print(Name)
# print(Age)
# print(Is_New)
#
# ##Receiving input
#
# name = input('What is your name? ')
# print('Hi ',name)
#
#
# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year) ##Need to convert to integer if you are expecting a numerical value
# print(age)
# print(type(age))
#
# #Exercise
# ##Ask a user their weight in pounds and convert it to kilograms
#
# weight_lbs = input('What is your weight in lbs? ')
# weight_kg = float(weight_lbs)/float(2.2)
# print('Your weight in kilograms is: ',weight_kg)
#
# ##Strings
#
# course="Python's for beginners" #Use double quotes when you need to use single quote on a string
#
# print (course)
#
# ##Multi Line String #Use triple quotes
#
# greeting='''
# Hi john,
#
# Here is our first email to you
# Thank you,
# The Support Team'''
#
# print(greeting)
#

#Indexing in Python
# course="Python for beginners"
# print(course[0:4])

#String Methods
#Formatted Strings #-prefixed with f

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder' ##can use + to concatenate
# msg = f'{first} [{last}] is a coder' ##curly braces defines placeholders
# #1. prefix your strings with curly braces 2. Use Curly brace for variables
#
# print(message)
# print(msg)


course = 'Python for Beginners'
print(len(course)) #function to get length of string
print(course.upper())
print(course.lower())
print(course)
print(course.find('P')) ##Will search for the index of the first occurence of letter P
print(course.replace('Beginners','Absolute Beginners')) ##This is how you replace string in Python

##Check existence of string - You may use "in operator"

print('Python' in course) ##result is boolean(True or false)


##Search functions vs methods