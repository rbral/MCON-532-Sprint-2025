from palindrome import is_palindrome  # Import the function

user_input = input("Enter a string to check if it's a palindrome: ")
result = is_palindrome(user_input)
print(f"It is {result} that '{user_input}' is a palindrome.")
