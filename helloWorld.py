# Get input from the user
user_input = input("Enter something: ")  # Prompt the user to enter some input and store it in the variable user_input

# Remove spaces and convert to lowercase for case-insensitive comparison
cleaned_input = user_input.replace(" ", "").lower()

# Check if the cleaned input is a palindrome
is_palindrome = cleaned_input == cleaned_input[::-1]

# Print the result
if is_palindrome:
    print("The input is a palindrome!")
else:
    print("The input is not a palindrome.")
