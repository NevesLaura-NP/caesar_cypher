# Function that encrypts message variable
def encrypt(message, k):
    # Creates a new empty variable to store the new encrypted message
    new_message = ""
    
    # Splits string into separate letters
    split_message = list(message)
    
    # Loops through letters inside the list
    for i in split_message:
        # checks for upper case letter
        if i.isupper():          
            # Creates variable that turns letters into ASCII
            # Subtracts minimum ASCII for letters
            # Adds key value
            # Calculates the remainder of the amount of letters in the alphabet
            # Reinserts minimum to count ASCII letters
            encrypted_ascii = (ord(i) - 65 + k) % 26 + 65
            encrypted_message = chr(encrypted_ascii)
        # checks for lower case letter
        elif i.islower():
            encrypted_ascii = (ord(i) - 97 + k) % 26 + 97 
            # Translates message into letters according to ASCII
            encrypted_message = chr(encrypted_ascii)
        else: 
            encrypted_message = " "
        # Adds encrypted message value to the new_message variable
        new_message += encrypted_message
        
    return new_message

# Function that decrypts message variable
def decrypt(message, k):
    new_message = ""
    
    split_message = list(message)
    
    for i in split_message:
        if i.isupper():
            # Creates variable that turns letters into ASCII
            # Subtracts minimum ASCII for letters
            # Calculates the remainder of the amount of letters in the alphabet
            # Subtracts Key value
            # Reinserts minimum to count ASCII letters
            decrypted_ascii = (ord(i) - 65 - k) % 26 + 65
            decrypted_message = chr(decrypted_ascii)
        elif i.islower():
            decrypted_ascii = (ord(i) - 97 - k) % 26 + 97
            # Translates message into letters according to ASCII
            decrypted_message = chr(decrypted_ascii)
        else:
            decrypted_message = " "
        # Adds decrypted message value to new_message variable
        new_message += decrypted_message
    
    return new_message

message = "Hello Brand New World"
k = 1000000

encrypted = encrypt(message, k)
decrypted = decrypt(encrypted, k)

print("Your encrypted message is:", encrypted)
print("Your decrypted message is:", decrypted)
