# 1. Email Validator
# Challenge Description: Implement a Python program that validates email addresses to ensure they meet a specific format, using regular expressions.

import re

email = input("Enter an email address: ")
pattern=r"[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]+"
match=re.fullmatch(pattern,email)
if match:
    print("Valid email")
else:
    print("Invalid email")


