def encrypt(message, k):
    #creates new empty variable to store new encrypted message
    new_message = ""
    
    #splits string into separate letters
    split_message = list(message)
    
    #loops through letters inside the list
    for i in split_message:
        #checks if letters are lower case
        if i.islower():
            #translate the letter according to the ASCII
            num_ascii = ord(i)
            
            #checks if code is equal to spaces and then adds the key value
            if num_ascii != 32:
                encrypted_ascii = (num_ascii + k) % 123
            if encrypted_ascii < 97:
                encrypted_ascii += 97
            encrypted_message = chr(encrypted_ascii)
        else: 
            encrypted_message = " "
        new_message += encrypted_message
    return new_message


def decrypt(message, k):
    new_message = ""
    split_message = list(message)
    for i in split_message:
        num_ascii = ord(i)
        if num_ascii != 32:
            encrypted_ascii = (num_ascii - k) % 123
            if encrypted_ascii < 97:
                loop = 97 - encrypted_ascii
                encrypted_ascii = 123 - loop 
            decrypted_message = chr(encrypted_ascii)
        else:
            decrypted_message = " "
        new_message += decrypted_message
    return new_message

message = "holidays are over"
k = 10

encrypted = encrypt(message, k)
decrypted = decrypt(encrypted, k)

print("Encrypted message is:" + encrypted)
print("Decrypted message is:" + decrypted)
