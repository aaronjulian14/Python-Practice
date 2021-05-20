Weight = float(input('Weight: '))
#print('Weight: '+Weight)
UnitOfMeasure=input('(L)bs or (K)g:')
UnitOfMeasure=UnitOfMeasure.capitalize()
print(UnitOfMeasure)

if UnitOfMeasure == 'K':
    ConvertedWeight = Weight*2.2
    #print("You are ",ConvertedWeight," pounds")
    print(f"You are {ConvertedWeight} pounds")
elif UnitOfMeasure == 'L':
    ConvertedWeight = Weight*0.45
    print(f"You are {ConvertedWeight} kilograms")
else:
    print("Please enter a valid unit of measure")

