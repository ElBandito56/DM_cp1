#Dm period 2 crew

total_money = input("how much money did they make?") 
crew = input("how muvh crew member are there?")
share = total_money/crew 
captain = share * 7 
first_mate = share * 3
total_money = captain  + first_mate - total_money
print( "the captain gets " + captain + " the first mate has " + first_mate + " and the crew is still owed" + total_money)