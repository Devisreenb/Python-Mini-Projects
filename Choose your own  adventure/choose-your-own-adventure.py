name = input("Type your name : ").capitalize()
print("Welcome",name,"to this adventure")
answer = input("You are on dirt road .It has come to an end and you can go left or right. Which would you like to go ? ")
if answer == "left":
    answer = input("You come to a river. you can walk around it or swin across ? Type walk to walk around and swim to swim across : " )
    if answer == "walk":
        print("You walked for many miles and ran out of water . You lose .")
    elif answer == "swim":
        print("While you are swimming , you are eaten by alligetor. You lose.")
    else:
        print("Invalid option. You lose")
elif answer=="right":
    answer = input("You come to a bridge, it looks lovely. Do you want to cross it or back it (cross/back) ? ")
    if answer == "back" :
        print("You go back and lose .")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no) ? ")
        print("eljljo",answer)
        if answer == "yes" :
            answer = input("The stranger gave you the mystery box. Do you want to unlock it or give it to someother ? Type unlock to unlock or give to give it to the other person ? ")
            if answer == "unlock":
                print("You won ! Its ok to have your reward ")
            elif answer == "give":
                print("you won ! Its nice to see you giving ")
            else:
                print("Invalid option. you lose. ")
        elif answer == "no":
            print("You lose")
        else:
            print("Invalid option. you lose.")
    else:
        print("Invalid option. you lose.")
else:
    print("Invalid option. you lose.")

print("Thanks for trying out .")