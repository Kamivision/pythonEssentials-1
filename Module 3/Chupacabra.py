# The break statement is used to exit/terminate a loop.

# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

# Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.
print("""
**********************************************
* Greetings player! You've Entered the Realm *
* of a Beast from Spanish Mythology. Only by *
* Guessing it's name will you be set free... *
**********************************************
""")


secret_word = "chupacabra"
#prompt user to enter a word
word = input("Enter a word: ")

#create while loop that continually asks for a word until the secret word is entered.
while True:
    if word == secret_word:
        break
    word = input("Enter a word: ")
    
#create an exit message for when the user finds the secret word.
print("You've successfully escaped the loop.")