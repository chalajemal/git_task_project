# Get input from the user
user_input = input("Enter something: ")  # Prompt the user to enter some input and store it in the variable user_input

# Print the inputted data
print("You entered:", user_input)  # Print the inputted data along with a message

# Count the number of characters
num_characters = len(user_input)

# Count the number of words
num_words = len(user_input.split())

# Count the number of lines
num_lines = user_input.count('\n') + 1  # Count the newline characters to determine the number of lines

# Print the analysis results
print("Number of characters:", num_characters)
print("Number of words:", num_words)
print("Number of lines:", num_lines)
