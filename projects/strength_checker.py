#Dm 2 passowrd checker
#set up  list of special characters
special_char =  ("z","!",'@','#','$','%','^','&','*','(',')','_','+','-',"=",'[',']','{','}','|',';',':',',','.','<',',','>','?')
#set the rtating to the start as 0
upper = False
lower = False
special = False
length = False
num = False
rating= 0
#have user input their PASSWPRD
password = input("whats your password")
#check if the password has at least 8 characters if so add one to the rating
if len(password) >= 8:
    rating += 1
    length = True
#check if password has at least one uppercase  if so add one to the rating
for i in password:
    if i.isupper():
        rating += 1
        upper = True
        break
#check if password has at least one lowercase if so add one to the rating
for i in password:
    if i.islower():
        rating += 1
        lower = True
        break
#check if password has at least one number  if so add one to the rating
for i in password:
    if i.isnumeric():
        rating +=1
        num = True
        break
#check if password has at least one specisl character  if so add one to the rating
for i in password: 
    if i in special_char:
        rating += 1
        special = True
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
#checking  if they have  the requirements and telling the user what they have and what there missing
if length == False:
    print ("your password is too short")
if upper == False:
    print ("your password needs an uppercase letter")
if lower == False:
    print ("your password needs a lowercase letter")
if num == False:
    print ("your password needs a number")
if special == False:
    print("your password needs a special character")
if length == True:
    print ("your password is a good length")
if upper == True:
    print ("your password has a uppercase letter")
if lower == True:
    print ("your password has a lowercase letter")
if num == True:
    print ("your password has a number")
if special == True:
    print("your password  has a  special character")

