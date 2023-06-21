print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes" :
    quit()

name = input("what is your name ? ")
print("Let's play ! "+name.capitalize())

score = 0

answer = input("What does CPU stand for ? ")
if answer.lower() =="central processing unit":
    print("correct !")
    score+=1
else:
    print("Incorrect !")

answer = input("What does GPU stand for ? ")
if answer.lower() == "graphics processing unit":
    print("Correct ! ")
    score += 1
else:
    print("Incorrect !")

answer = input("What does RAM stand for ? ")
if answer.lower() == "random access memory":
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

answer = input("What does PS stand for ? ")
if answer.lower() == "power supply":
    print("Correct !")
    score += 1 
else:
    print("Incorrect !")

print("You got "+str(score) + " marks !")
print("You got "+str((score/4)*100)+" %")


