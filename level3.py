# 3. Brute force attack
# Challenge Description: Create a Python script that tries to guess a password of a certain lenght using brute force

import itertools
import string

password = "cab"
password_length = len(password)

characters = string.ascii_lowercase
attempt_count = 0

print(characters)

for combination in itertools.product(characters,repeat=password_length):
    guess="".join(combination)
    attempt_count+=1
    if guess == password:
        print("Password found:",guess)
        print("Attempts:", attempt_count)
        break
