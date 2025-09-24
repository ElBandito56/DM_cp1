#DM letter grade 2cnd period

grade = float(input("what grade do you have in percentage?"))

if grade >= 94:
    print(f"wow you have an A and your grade is {grade:.2f}%")
elif grade >= 90:
    print(f"wow you have an A- and your grade is {grade:.2f}%")
elif grade >= 87:
    print(f"wow you have an B+ and your grade is {grade:.2f}%")
elif grade >= 83:
    print(f"wow you have an B and your grade is {grade:.2f}%")
elif grade >= 80:
    print(f"wow you have an B- and your grade is {grade:.2f}%")
elif grade >= 77:
    print(f"wow you have an C+ and your grade is {grade:.2f}%")
elif grade >= 74:
    print(f"wow you have an C and your grade is {grade:.2f}%")
elif grade >= 70:
    print(f"wow you have an C- and your grade is {grade:.2f}%")
elif grade >= 67:
    print(f"wow you have an D+ and your grade is {grade:.2f}%")
elif grade >= 64:
    print(f"wow you have an D and your grade is {grade:.2f}%")
elif grade >= 60:
    print(f"wow you have an D- and your grade is {grade:.2f}%")
elif grade <= 59:
    print(f"wow you have an F and your grade is {grade:.2f}%")
else:
    print ('thats not a real grade')
    