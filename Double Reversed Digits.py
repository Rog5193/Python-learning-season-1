#Calculate two times the reversed digits of a number

number=int(input("Please enter a 3-digit number: "))

if not (number>=100 and number<=999):
    print("Not a 3-digit! Try again!")
else:
    new_hundreds= str(number % 10)
    new_tens= str((number // 10) % 10)
    new_ones= str(number // 100)
    reversed_number=int(new_hundreds + new_tens + new_ones)
    two_times_reversed=2*reversed_number
    print(f"The answer is: {two_times_reversed}")