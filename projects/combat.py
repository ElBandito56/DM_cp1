#Dm 2cnd combat program
import random
Mdistance = random.randint(1,60)
Mhealth = 50
Mrange = 50
Mspeed = 50
Mattack = 50



name = input("whats your name?")
Type_class = input("what class would you like to be, 1 for fighter,2 for mage, 3 for assasin")
if Type_class == "1":
    health = 40
    speed = 50
    attack = 50
    range1 = 40
    print ("hello " ,name, "your class is fighter, your stats are ",health," ",speed, " ", attack," " ,range1, " ")
elif Type_class == "2":
    health =70
    speed = 25
    attack = 60
    range1 = 60
    print ("hello " ,name, "your class is mage, your stats are ",health," ",speed, " ", attack," " ,range1, " ")
elif Type_class == "3":
    health = 10
    speed = 60
    attack = 90
    range1 = 20
    print ("hello " ,name, "your class is assasin, your stats are ",health," ",speed, " ", attack," " ,range1, " ")
print("you are being attacked by a werewolf")
if speed > Mspeed:
    if range1 > Mdistance:
        Action = input("would you like to attack or to flee")
        if Action == 'attack':
            
