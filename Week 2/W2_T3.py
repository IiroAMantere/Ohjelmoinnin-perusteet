#A2_T3: String length and concatenation
#Make Python program, which prompts user to insert two words. Print the length of each word and then compound them together. Put single quotes around the compound word.

#Example program run:

#Program starting.
print("Program starting.")

#Insert first word: fire
First_word = input("insert first word: ")
#Insert second word: fighter
Second_word = input("Insert second word: ")
#1st word is 4 characters long.
print(f"1st word is {len(First_word)} characters long.")
#2nd word is 7 characters long.
print(f"2nd word is {Second_word} characters long.")
#Words together makes one closed compound 'firefighter'.
print(f"Words together makes one closed compound '{First_word}{Second_word}'.")
#Program ending.
print("Program ending")