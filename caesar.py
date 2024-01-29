# Function that encrypts message variable
def encrypt(message, k):
    # Creates a new empty variable to store the new encrypted message
    new_message = ""
    
    # Splits string into separate letters
    split_message = list(message)
    
    # Loops through letters inside the list
    for i in split_message:
        # Creates a variable that has the message translated into ASCII 
        if i.isupper():          
            #creates variable that turns letters into ASCII then checks for the uppercase limit
            encrypted_ascii = (ord(i) + k) % 94 
            if encrypted_ascii < 65:
                encrypted_ascii += 65
            encrypted_message = chr(encrypted_ascii)
        elif i.islower():
            #creates variable that turns letters into ASCII then checks for the lowercase limit
            encrypted_ascii = (ord(i) + k) % 123 
            # Checks if value of ASCII is under 97 and if it is, adds 97
            if encrypted_ascii < 97:
                encrypted_ascii += 97
            # Translates message into letters according to ASCII
            encrypted_message = chr(encrypted_ascii)
        else: 
            encrypted_message = " "
        # Adds encrypted message value to the new_message variable
        new_message += encrypted_message
        
    return new_message

# Function that decrypts message variable
def decrypt(message, k):
    # Creates a new empty variable to store new decrypted message
    new_message = ""
    
    # Splits string into separate letters
    split_message = list(message)
    for i in split_message:
        # Checks if the letter is upper case
        if i.isupper():
            #creates variable that turns letters into ASCII then checks for the uppercase limit
            decrypted_ascii = (ord(i) - k ) % 92 
            if decrypted_ascii < 65:
                # If ASCII is lower than 65, it creates a variable that makes the counting loop back to counting only uppercase letters
                loop = 65 - decrypted_ascii
                decrypted_ascii = 123 - loop 
            # Translates message into letters according to ASCII
            decrypted_message = chr(decrypted_ascii)
        # Checks if the letter is lower case
        elif i.islower():
           #creates variable that turns letters into ASCII then checks for the lowercase limit
            decrypted_ascii = (ord(i) - k) % 123
            # Checks if ASCII value is under 97
            if decrypted_ascii < 97:
                # If ASCII is lower than 97, it creates a variable that makes the counting loop back to counting only lowercase letters
                loop = 97 - decrypted_ascii
                decrypted_ascii = 123 - loop 
            # Translates message into letters according to ASCII
            decrypted_message = chr(decrypted_ascii)
        else:
            decrypted_message = " "
        # Adds decrypted message value to new_message variable
        new_message += decrypted_message
    
    return new_message

message = "Holidays are over"
k = 10

encrypted = encrypt(message, k)
decrypted = decrypt(encrypted, k)

print("Your encrypted code is:", encrypted)
print("Your decrypted code is:", decrypted)
