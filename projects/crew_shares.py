#Dm period 2 crew

total_money = float(input("how much money did they make?"))
crew = int(input("how muvh crew member are there?"))
share = (total_money)/(crew + 10)
captain = share * 7 
first_mate = share * 3
total = captain  + first_mate - total_money
print(f"the captain gets ${captain:.2f} the first mate has ${first_mate:.2f} and the crew is still owed ${total:.2f}")