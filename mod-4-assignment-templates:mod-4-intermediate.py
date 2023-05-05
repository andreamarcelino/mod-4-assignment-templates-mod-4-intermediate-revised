'''Module 3: Individual Programming Assignment 1
Andrea Nicole Marcelino

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    if letter == " ":
        return " "
    
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = alphabet.index(letter)
        shifted_index = (index + shift) % len(alphabet)
        return alphabet[shifted_index]
# test
# print(shift_letter([input letter here], [input value here])) 

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_letters = {}
    for i in range(len(uppercase_alphabet)):
        shifted_letters[uppercase_alphabet[i]] = uppercase_alphabet[(i + shift) % len(uppercase_alphabet)]
    shifted_message = ""
    for uppercase_alphabet in message:
        if uppercase_alphabet == " ":
            shifted_message += " "
        else:
            shifted_message += shifted_letters[uppercase_alphabet]
    return shifted_message
# test
# message = [input message here]
# shift = [input value here]
# encrypted_message = caesar_cipher(message, shift)
# print(encrypted_message) 

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    if letter == " ":
        return " "
    letter_value = ord(letter) - ord("A")
    shift_value = ord(letter_shift) - ord("A")
    shifted_value = (letter_value + shift_value) % 26
    return chr(shifted_value + ord("A"))
# test
# print(shift_by_letter([input letter here], [input letter shift here]))

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    message = message.upper()
    key = key.upper()
    new_key = key
    while len(new_key) < len(message):
        new_key += key
    encrypted_message = ""
    for i in range(len(message)):
        if message[i] == " ":
            encrypted_message += " "
        else:
            shift_value = ord(new_key[i]) - ord("A")
            shifted_letter = chr((ord(message[i]) - ord("A") + shift_value) % 26 + ord("A"))
            encrypted_message += shifted_letter
    return encrypted_message
# test
# print(vigenere_cipher([input message here], [input key here]))
