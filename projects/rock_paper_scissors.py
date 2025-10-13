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
        elif computer == 2:
            print( " you won! paper beats rock")
            user_score += 1
        elif computer == 3:
            print("you both chose paper")
    elif player == "rock":
        if computer == 1:
            print ("score! rock beats sciccors ")
            user_score += 1
        elif computer == 2:
            print ("thats a tie!")
        elif computer == 3:
            print("awh you lost paper beats rock")
            computer_score = 3 
    elif player == "sciccors":
        if computer == 1:
            print("you tied!")
        elif computer == 2:
            print("awh you lost rock beats sciccors")
            computer_score += 1 
        elif computer == 2:
            print("you won! sciccors beats paper")
            user_score += 1
    else:
        print('you cant play that')
    if computer_score == 1:
        print("the computer has won")
    elif user_score == 1:
        print("you have won ")
    else:
        print("you tied")
        



        

