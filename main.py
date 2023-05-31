import random
user_wins =0
computer_wins=0

possibilities = ["rock","paper","scissors"]

while True:
    user_input = input("type rock , peper , scissor or  q to Quit: ").lower()
    if user_input== "q":
        break
    if user_input not in possibilities:
        continue
    random_num = random.randint(0,2)
    computer_pick = possibilities[random_num]
    print("computer picked ", computer_pick +".")
    if user_input=="rock" and computer_pick== "scissors":
        print("you won! : )")
        user_wins+=1
    elif user_input=="paper" and computer_pick== "rock":
        print("you won! : )")
        user_wins+=1
    elif user_input=="scissors" and computer_pick== "paper":
        print("you won! : )")
        user_wins+=1
    else:
        print("you lost :(")
        computer_wins+=1

print("############################")
print("you won ",user_wins," times.")
print("you lost ",computer_wins," times against computer.")
print("okay , see you again !")
print("############################")

