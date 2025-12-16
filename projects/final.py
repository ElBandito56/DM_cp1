import random 

def game():
   while True:

      start_game = input("welcome to Big scary dream... input (1) when you are ready to begin...")
      if start_game == "1":
         print("After a long day of trick or treating and watching scary movies your mom told you not to watch, you rest your eyes with a stomach full of candy. But as you slumber in your tiny little bed Suddenly your tiny  are arms jolted, you wake up screaming, pulled by a mysterious dark force as you're thrusted into the main hall, you looked up and saw its john shadow from the horror movie! You pick up a nightlight and get prepared to brawl" )
         combat(250,"Its john shadow, you raise your arms at the terryfying beast",20,80,30, "superman bandaid", "after blinding the monster, it screeches and flees into the hallways of your house, you find it best to go back to bed in your room.")
         break
      else:
        print("input (1) when you are ready")
      
      
      
      
      

def combat(monhp,mondio,monap1,monap2,monap3,mondrop,Dedio):
   while True:
    if Hp > 0:
   
      f"{mondio} it stares at you ready to brawl."
      whogoesfirst = random.randint(1,2)
      if whogoesfirst == 1:
       pc =  input("check inventory(1)\n attack(2)")
       if pc == "1":
          f"{inventory} would you like to use anything"
       elif pc == 2:
        Ap - monhp
     
       
      elif whogoesfirst == 2:
         Matk = random.randint(1,2,3)
         if Matk == 1:
          monap1 - Hp
         elif Matk == 2:
            monap2 - Hp
         elif Matk == 3:
            monap3 - Hp
    elif Hp == 0:
      play_again_choice = input("would you like to play again, if so press (1)")
      if play_again_choice == '1':
        game()
      else:
        print("hope you had fun!")
       
      
    elif monhp == 0:
      f"{Dedio}"
      inventory.append(mondrop)



Hp = 150
Ap = 50
Speed =100
Terror = 100
crit = random.randint(1,5)



def investigate(preroom):
  if preroom == mainhall: 
      Mchoice = input("you are in the main hall\n go to kitchen (1)\n go to the living room(2) \n go to bathroom(3) \n")
      if Mchoice == 1:
         preroom = kitchen
      elif Mchoice == 2:
        preroom = livroom
      elif Mchoice == 3:
        preroom = baro

  elif preroom == kitchen:
    kchoice = input("s")
      






game()
investigate(mainhall)

