###############################################################################################
# Project Name: Morse Code Translator
# Developer: Will Donin | 03/07/2022
#
# File: main.py
#
# Language: Python | 3.10v
###############################################################################################
from translator import MorseCodeTranslator

# ---------------------------------------- VARIABLES ---------------------------------------- #
is_on = True

# -------------------------------------- INITIALIZERS --------------------------------------- #
# First we initialize our morse code translator.
translator = MorseCodeTranslator()


# ------------------------------------- USER INTERFACE -------------------------------------- #
logo1 = "\n_  _ ____ ____ ____ ____    ____ ____ ___  ____\n"
logo2 = '|\/| |  | |__/ [__  |___    |    |  | |  \ |___\n'
logo3 = "|  | |__| |  \ ___] |___    |___ |__| |__/ |___\n"


print(logo1 + logo2 + logo3)
print("################################################")
print("\n Welcome to the morse code translator 1000 ")
print(" -----------------------------------------------")
print("                 🧾 RULES 🧾")
print("  1 - Type 'decode' or 'encode' to start.")
print("  2 - Use 3 spaces between words when decoding.")
print("  3 - Use 1 space between words when encoding.")
print("  4 - Only A-Z and 0-9 characters allowed.")
print("  5 - Type 'off' to power down the machine.")
print("\n################################################\n")

while is_on:

    # Ask user if they would like to encode or decode messages.
    question = input("Would you like to encode or decode messages? ").lower()

    if question == "decode":
        # Ask the user which morse code they would like to decode.
        phrase = input("What's the morse code? ").lower()
        translator.get_message(phrase=phrase, decode=True)

    elif question == "encode":
        # Ask the user which phrase they would like to encode.
        phrase = input("What's the phrase to encode? ").lower()
        translator.get_message(phrase=phrase, decode=False)
    elif question == "off":
        # Turns off the translator.
        is_on = False
        print("Machine is turning off...")
    else:
        # Invalid answer.
        print("Not a valid answer. Please try again.")
