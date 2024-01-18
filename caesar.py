#function that encrypts message variable
def encrypt(message, k):
    #creates new empty variable to store new encrypted message
    new_message = ""
    
    #splits string into separate letters
    split_message = list(message)
    
    #loops through letters inside the list
    for i in split_message:
        #creates variable that has message translated into ASCII 
        num_ascii = ord(i)
        if i.isupper():          
            
            # checks if code is not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII upper case letters
            if num_ascii != 32:
                encrypted_ascii = (num_ascii + k) % 91
                if encrypted_ascii < 65:
                    encrypted_ascii += 65
                encrypted_message = chr(encrypted_ascii)
            #adds space to where value 32 is 
            else:
                encrypted_message = " "
                
        elif i.islower():
            
            # checks if code not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII lower case letters
            if num_ascii != 32:
                encrypted_ascii = (num_ascii + k) % 123
                #checks if value of ASCII is under 97 and if it is adds 97
                if encrypted_ascii < 97:
                    encrypted_ascii += 97
                #translates massage into letters according to ASCII
                encrypted_message = chr(encrypted_ascii)
            #adds space to where value 32 is 
            else:
                encrypted_message = " "
        # adds empty space if input of message does not align with any letters
        else: 
            encrypted_message = " "
        # adds encrypte message value to new_message variable
        new_message += encrypted_message
    # returns a new message
    return new_message

#function that decrypts message variable
def decrypt(message, k):
    #creates new empty variable to store new encrypted message
    new_message = ""
    
    #splits string into separate letters
    split_message = list(message)
    for i in split_message:
        #creates variable that has message translated into ASCII 
        num_ascii = ord(i)
        #checks if the letter is upper case
        if i.isupper():
            # checks if code is not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII upper case letters
            if num_ascii != 32:
                decrypted_ascii = (num_ascii - k) % 91
                if decrypted_ascii < 65:
                    #if ASCCI is lower than 65 it creates a variable which makes the counting loop back to counting only upper case letters
                    loop = 65 - decrypted_ascii
                    decrypted_ascii = 123 - loop 
                #translates massage into letters according to ASCII
                decrypted_message = chr(decrypted_ascii)
            #adds space to where value 32 is 
            else:
                decrypted_message = " "
        #checks if the letter is lower case
        elif i.islower():
            # checks if code is not equal to spaces and then adds the key value while verifying for the highest value possible for ASCII upper case letters
            if num_ascii != 32:
                decrypted_ascii = (num_ascii - k) % 123
                #checks if ASCII value is under 97
                if decrypted_ascii < 97:
                    #if ASCCI is lower than 97 it creates a variable which makes the counting loop back to counting only lower case letters
                    loop = 97 - decrypted_ascii
                    decrypted_ascii = 123 - loop 
                #translates massage into letters according to ASCII
                decrypted_message = chr(decrypted_ascii)
            #adds space to where value 32 is 
            else:
                decrypted_message = " "
        # adds empty space if input of message does not align with any letters
        else:
            decrypted_message = " "
        # adds decrypted message value to new_message variable
        new_message += decrypted_message
    
    return new_message

message = "Holidays are over"
k = 10

encrypted = encrypt(message, k)
decrypted = decrypt(encrypted, k)

print("Encrypted message is:" + encrypted)
print("Decrypted message is:" + decrypted)
