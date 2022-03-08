###############################################################################################
# Project Name: Morse Code Translator
# Developer: Will Donin | 03/07/2022
#
# File: translator.py
#
# Language: Python | 3.10v
###############################################################################################

CODE_DICT = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
}


# The class MorseCode creates new CodeDict objects and stores on itself.
class MorseCodeTranslator:
    def __init__(self):
        self.codes = []
        self.reverse_codes = []
        self.keys = []
        self.reverse_keys = []
        self.create_codes(CODE_DICT)

    def create_codes(self, code_dict):
        """This method takes a dictionary and transform into CodeDict objects. It also creates a key array.
        Please note that will be created codes and keys as reverse codes and reverse keys as well."""
        for key, value in code_dict.items():

            # Creates the normal key:value pairs and keys.
            new_code = CodeDict(key=key, value=value)
            self.keys.append(key)
            self.codes.append(new_code)

            # Creates the reversed key:value pairs and keys.
            new_code = CodeDict(key=value, value=key)
            self.reverse_keys.append(value)
            self.reverse_codes.append(new_code)

    def find_code(self, char: str, reverse=False) -> str:
        """This method takes a string and returns the correct morse code. If you need to get the reverse code, you need
        to set the reverse variable to True. Return empty if code not found."""
        keys = self.keys
        codes = self.codes
        space = " "

        if reverse:
            # If decoding, keys become values and values become keys.
            keys = self.reverse_keys
            codes = self.reverse_codes
            space = ""

        if char in keys:
            # If the character exists inside the codes/reverse_codes then it returns its translated value.
            code = codes[keys.index(char)].value
            return code + space
        else:
            # If character not found, returns an empty string.
            return ""

    def get_message(self, phrase: str, decode=False, separator="-") -> None:
        """This method takes a phrase, and it automatically transforms into a mose code string. If you need the
         translation make sure you set decode to True."""

        # In order to get the correct code value the string needs to be formatted accordingly.
        if not decode:
            # For encode, separates words by dash character.
            phrase = phrase.replace(" ", separator)
            word_spacing = "  "

        else:
            # For decode, it needs to transform 3 spaces into one dash,
            # then split the morse code into a list of codes.
            phrase = phrase.replace("   ", f" {separator} ").split()
            word_spacing = " "

        # Use list comprehension to create list of translated values.
        codes_list = [word_spacing if char == separator else self.find_code(char, reverse=decode) for char in phrase]

        # Transform the list into a string with title casing and prints the string on the console.
        morse_code = "".join(codes_list).title()
        return print(morse_code)


# The class CodeDict build morse code objects with key:value pairs.
class CodeDict:
    def __init__(self, key: str, value: str):
        self.key = key.lower()
        self.value = value
