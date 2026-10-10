# 2. Password Strength Checker / Breaker
# Challenge Description: Write a Python program to check the strength of a password based on predefined criteria (length, inclusion of numbers, uppercase and lowercase letters, and special characters).

password = input("Enter a password: ")
length_ok = len(password)>=8
has_number = any(char.isdigit() for char in password) 
#“Is at least ONE of these things True?”
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_special = any(not char.isalnum() for char in password)
if length_ok and has_lower and has_upper and has_number and has_special:
    print("Strong password")
else:
    print("Weak password")


