first_number = int(input("Please enter the first number: "))
second_number = int(input("Please enter the second number: "))

if first_number > second_number:
    print(f"The bigger number is: {first_number}")

elif first_number == second_number:
    print("They are equal!")

else:
    print(f"The bigger number is: {second_number}")