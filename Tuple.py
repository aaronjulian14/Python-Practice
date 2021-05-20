#review list
# list = use square brackets
# tuple = use parenthesis, tuples can't be modified

numbers = (1,2,3)
print(numbers[0])

##Unpacking -- setting variables from a tuple
coordinates = (1,2,3)
## instead of this
# x = coordinates[0]
# x = coordinates[1]
# x = coordinates[2]

## we can use this

x,y,z = coordinates
# python will evaluate the tuple or list, first value will be assigned to x an so on

