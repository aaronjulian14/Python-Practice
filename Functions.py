# def greet_user():
#     print ('Hi there!')
#     print ('Welcome aboard')
# ##good practice - add two line breaks after defining a function
#
# print("Start")
# greet_user() ##call gree_user() function
# print("Finish")

## how to pass information to your functions


def greet_user(first_name, last_name):
    print (f'Hi {first_name} {last_name}!')
    print ('Welcome aboard')
##good practice - add two line breaks after defining a function

# print("Start")
# greet_user("John","Smith") ##call gree_user() function
# greet_user("Mary","Jane") ##call gree_user() function
# print("Finish")
#
# ## Keyword argument
#
# print("Start")
# greet_user(last_name="Smith", first_name="John") ## this will output the same result
# ## even if you rearrange the order of your argument because of the keyword
# greet_user("Mary","Jane") ##call gree_user() function
# print("Finish")

def square(number):
    print number * number
print(square(3))
 