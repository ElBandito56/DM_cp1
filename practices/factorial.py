#DM 2cnd 
#while user has not entered interger:
while True:
   gg = input("enter a number")
   if gg.isdigit():
      float(gg)
      gg.round()
      int(gg)
      break 
   else:
      continue
def factorial(number):
   factor = number
   while factor > 1:
       number = number * factor
       factor = factor -1
       
       return number

#if input is a digit
#make input a float
#round number
#make input an integer
#else  if input is not a digit
#ask user again restarting loop

#define function called factorial
#factor = number
#while factor is greather than 1
#number = number x factor
#factor = factor - 1
#return number after functional
#print (ignal number:[number]. new number:
#[number post factorial)].")