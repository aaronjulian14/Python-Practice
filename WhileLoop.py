# i = 1
# while i <= 5:
#     print(i)
#     print('*' * i) #You can multiply strings
#     i = i+1
# print("Done")
#
# # You can use while True: to evaluate a series of conditions

##Guessing Game Exercise:
LuckyNumber = 9
attempt = int(0)

# while attempt != 3:
#     Guess = int(input("Guess: "))
#
#     #attempt = attempt + 1 #same as attempt +=1
#     attempt += 1
#     if Guess == LuckyNumber:
#         print("You win!")
#         break
#     elif attempt == 3:
#         print("Sorry you failed!")

##Approach 2
while attempt != 3:
    Guess = int(input("Guess: "))

    #attempt = attempt + 1 #same as attempt +=1
    attempt += 1
    if Guess == LuckyNumber:
        print("You win!")
        break
else:
    print("Sorry you failed!")