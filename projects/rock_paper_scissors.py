#Dm 2cnd period rock paper sciccors
#test = 0
import random
user_score =0
computer_score =0
while True:
    player = input('lets play rockpaper sciccors what do you want to play "rock" "paper" or "sciccors" please input at least one' )
    computer = random.randint(1,3)
    if player == "paper":
        if computer == 1:
            print("you lost! sciccors beats paper")
            computer_score += 1
        elif computer 

