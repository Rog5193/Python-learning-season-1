number = int(input("Please enter a number: ")) 

ones = number % 10 # Extract the ones digit
removed_ones_number = number - ones # Remove the ones digit
next_multiple_of_ten = removed_ones_number + 10 # Add 10 to get the next multiple

print(f"The next multiple of ten is: {next_multiple_of_ten}")