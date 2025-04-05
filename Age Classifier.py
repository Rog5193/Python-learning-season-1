age = int(input("Please enter your age!: "))

if age <= 0:
    print("Invalid age. Please enter a positive number.")

elif age < 6:
    print ("You are a toddler!")

elif age >= 6 and age < 10:
    print ("You are a child!")

elif age >= 10 and age < 14:
    print ("You are a preteen!")   

elif age >= 14 and age < 24:
    print ("You are a young adult!")   

elif age >= 24 and age < 40:
    print ("You are an adult!")  

else:
    print ("You are a middle-aged adult!")      