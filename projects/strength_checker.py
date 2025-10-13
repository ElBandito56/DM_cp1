#Dm 2 passowrd checker
#set up  list of special characters
special_char =  ("z","!",'@','#','$','%','^','&','*','(',')','_','+','-',"=",'[',']','{','}','|',';',':',',','.','<',',','>','?')
#set the rtating to the start as 0
rating= 0
#have user input their PASSWPRD
password = input("whats your password")
#check if the password has at least 8 characters if so add one to the rating
if len(password) >= 8:
    rating += 1
#check if password has at least one uppercase  if so add one to the rating
for i in password:
    if i.isupper():
        rating += 1
        break
#check if password has at least one lowercase if so add one to the rating
for i in password:
    if i.islower():
        rating += 1
        break
#check if password has at least one number  if so add one to the rating
for i in password:
    if i.isnumeric():
        rating +=1
        break
#check if password has at least one specisl character  if so add one to the rating
for i in password: 
    if i in special_char:
        rating += 1
        break
    
#then if they have a 5 display very strong password
if rating == 5:
    print("your rating is A 5/5  thats VERY strong password")
#elif they have a 4 display they have a strong passowrd
elif rating == 4:
    print("wow you got a rating of 4! thats a strong password")
#elif they have a 3 display they have a mediorcre password
elif rating == 3:
    print("you got a 3 you have  mediorce password")
#elif they have a 1-2 they have a weak password
elif rating == 1 or 2:
    print("you got a 1-2 thats a weak password")
#else display they didnt input anything
else:
    print("thats not a real password")