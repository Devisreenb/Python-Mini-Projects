import random 

user_wins = 0
computer_wins = 0

options =["rock","paper","scissors"]

while True :
    user_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    computer_input = random.randint(0,2)
    # 0 - rock , 1 - paper , 2 - scissors
    computer_input = options[computer_input]

    if user_input == "rock" and computer_input =="scissors" :
        print("You won it !")
        user_wins+=1
    elif user_input == "scissors" and computer_input == "paper" :
        print("You won it !")
        user_wins +=1
    elif user_input == "paper" and computer_input == "rock" :
        print("You won it !")
        user_wins +=1 
    elif user_input == computer_input :
        print("It's a clash !")
        continue
    else:
        print("You lost it !")
        computer_wins += 1

print("You won",user_wins,"times !")
print("Computer won",computer_wins,"times !")

