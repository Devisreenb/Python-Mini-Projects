import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0 : 
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

print("Welcome to Number guessing game ! ")

random_number = random.randint(0,top_of_range)
count = 0 
while True:
    count += 1 
    answer = input("Make a guess : ")
    if answer.isdigit():
        answer = int(answer)
    else:
        print("Please enter a number next time . . . ")
        continue
    if answer == random_number : 
        print("You got it ! ")
        break 
    else:
        print("You got it wrong ! ")
        hint = input("Do you want a hint ? ")
        if hint.lower() != "yes" :
            pass
        else:
            if answer > random_number :
                print("You were above the number ! ")
            else:
                print("You were below the number !")


print ("You got it in", count , "guesses ")
     