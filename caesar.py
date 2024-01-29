# Function that encrypts message variable
def encrypt(message, k):
    # Creates a new empty variable to store the new encrypted message
    new_message = ""
    
    # Splits string into separate letters
    split_message = list(message)
    
    # Loops through letters inside the list
    for i in split_message:
        # Creates a variable that has the message translated into ASCII 
        num_ascii = ord(i)
        if i.isupper():          
            
            # Checks if code is not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII uppercase letters
            if num_ascii != 32:
                encrypted_ascii = (num_ascii + k) % 92
                if encrypted_ascii < 65:
                    encrypted_ascii += 65
                encrypted_message = chr(encrypted_ascii)
            # Adds space to where value 32 is 
            else:
                encrypted_message = " "
                
        elif i.islower():
            
            # Checks if code not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII lowercase letters
            if num_ascii != 32:
                encrypted_ascii = (num_ascii + k) % 123
                # Checks if value of ASCII is under 97 and if it is, adds 97
                if encrypted_ascii < 97:
                    encrypted_ascii += 97
                # Translates message into letters according to ASCII
                encrypted_message = chr(encrypted_ascii)
            # Adds space to where value 32 is 
            else:
                encrypted_message = " "
        # Adds empty space if input of message does not align with any letters
        else: 
            encrypted_message = " "
        # Adds encrypted message value to the new_message variable
        new_message += encrypted_message
    # Returns a new message
    return new_message

# Function that decrypts message variable
def decrypt(message, k):
    # Creates a new empty variable to store new encrypted message
    new_message = ""
    
    # Splits string into separate letters
    split_message = list(message)
    for i in split_message:
        # Creates a variable that has the message translated into ASCII 
        num_ascii = ord(i)
        # Checks if the letter is upper case
        if i.isupper():
            # Checks if code is not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII upper case letters
            if num_ascii != 32:
                decrypted_ascii = (num_ascii - k) % 92
                if decrypted_ascii < 65:
                    # If ASCII is lower than 65, it creates a variable that makes the counting loop back to counting only uppercase letters
                    loop = 65 - decrypted_ascii
                    decrypted_ascii = 123 - loop 
                # Translates message into letters according to ASCII
                decrypted_message = chr(decrypted_ascii)
            # Adds space to where value 32 is 
            else:
                decrypted_message = " "
        # Checks if the letter is lower case
        elif i.islower():
            # Checks if code is not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII upper case letters
            if num_ascii != 32:
                decrypted_ascii = (num_ascii - k) % 123
                # Checks if ASCII value is under 97
                if decrypted_ascii < 97:
                    # If ASCII is lower than 97, it creates a variable that makes the counting loop back to counting only lowercase letters
                    loop = 97 - decrypted_ascii
                    decrypted_ascii = 123 - loop 
                # Translates message into letters according to ASCII
                decrypted_message = chr(decrypted_ascii)
            # Adds space to where value 32 is 
            else:
                decrypted_message = " "
        # Adds empty space if input of message does not align with any letters
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
