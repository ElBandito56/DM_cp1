#Dm 2nd Flexibile caluclator
#make a way to add
#make a way to multiply 
#make a way to find the min
#make a way to find the median
#make a way to find the max
#ask the user what they want to do, multiply,add, or find  the min,median or max.
response = input('welcome, would you like to multiply, add, or find the min median or mode')
if response == 'add':
    add1 =float(input('whats your first number?'))
    add2 = float(input("whats your second number?"))
    addser = float(add1) + float(add2)
    print(addser)
elif response == "multiply":
    multi1 = float(input('whats your first number?'))
    multi2 = float(input("whats your second number?"))
    mulser = multi1 * multi2 
    print(mulser) 
elif response == "median":
    while True:
        response2 = input("would you like to input another number? (y/n)")
        if response2 == "y":
            num = float(input("give me a number"))
        elif response2 == "n":
            print("okay thank you for your time")
            False 
        else:
            print("you cant do that")
            

else:
    print("that dont make sense stoopid")

#if they choose add or multiply make them input 4 numbers and if they choose to mutilpy or add make them input two numbers

