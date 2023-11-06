# Working with Strings
# https://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/03_Strings/Hangman/
# Hangman

import random

# taking input
l1 = input("Enter a word : ").lower()

# checking whether special character is present or not
special = "!@#$%^&*()_-+=}{][?/>.<,"

# List Creation
li = list(l1)

number_of_dashes = random.randint(2, len(l1) - 1)

# by using sample from random ,we randomly chose some letters which we are going to hide
removed_letters = random.sample(l1, number_of_dashes)

chances = 6

# keeps track of the indexes of each letter after the
# correct value as been entered so the player won't re-enter
# correct value
mapping = list(enumerate(li))

# replacing the removed_letters with "_" as hidden
for i in removed_letters:
    for j in range(len(li)):
        if i == li[j]:
            li[j] = "_"
            break

wrong_letters = ""
correct = []
print(" ".join(li))
# Six chances for the player to correctly guess the correct letter
while chances:
    if "_" not in li:

        break
    else:
        enter = input("Enter a character:")
        if enter in special or enter.isalpha == False:
            print("Print a valid character:")
        elif enter not in removed_letters:
            print("wrong_letters answer,Try again")
            wrong_letters += enter
            print("wrong_letterer given characters are ", wrong_letters)

            chances -= 1
            print("Chances remaining: ", chances)
        else:
            enter = enter.lower()
            if enter in removed_letters:
                for e in mapping:
                    if e[1] == enter:
                        li[e[0]] = enter
                        correct.append(e[0])
                        break
                mapping.remove(e)
                print(" ".join(li))
if chances > 0:
    print("Game won")
else:
    print("Lose")
