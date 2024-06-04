def CreateMatrix(key, omitted_let):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    #Cleans key
    cleaned_key = ''
    for letter in key:
        if letter not in cleaned_key:
            cleaned_key += letter.upper()
            
    PF_Matrix = []
    alphabet = alphabet.replace(omitted_let.upper(), "")

    while len(PF_Matrix) < 5:
        current_row = []
        while len(current_row) < 5:
            if len(cleaned_key) > 0:
                current_row.append(cleaned_key[0])
                alphabet = alphabet.replace(cleaned_key[0], "")
                cleaned_key = cleaned_key[1:]
            else:
                current_row.append(alphabet[0])
                alphabet = alphabet[1:]
        PF_Matrix.append(current_row)
    
    return PF_Matrix

def Decrypt(matrix, message, omitted_let):
    
    # cleans message to ensure no spaces, special characters, or omitted letter gets passed through the decrypt process. 
    clean_message = ''
    for letter in message:
        if letter.upper() == omitted_let.upper():
            print(f'Error: your decrypted string contains the omitted letter {omitted_let}')
            return False
        elif letter.isalpha():
            clean_message += letter.upper()

    decrypt_message = ''
    while len(clean_message) > 0:

        if len(clean_message) == 1:
            print('The lenght of your encrypted message is not even, the last letter will be omitted')
            break

        # Finds matrix location for first two letters of clean_message
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == clean_message[0]:
                    row1 = i
                    col1 = j
                if matrix[i][j] == clean_message[1]:
                    row2 = i
                    col2 = j

        # In the same row
        if row1 == row2:
            decrypt_message += matrix[row1][(col1 - 1) % 5]
            decrypt_message += matrix[row2][(col2 - 1) % 5]
        # In the same column
        elif col1 == col2:
            decrypt_message += matrix[(row1 - 1) % 5][col1]
            decrypt_message += matrix[(row2 - 1) % 5][col2]
        else:
            decrypt_message += matrix[row1][col2]
            decrypt_message += matrix[row2][col1]
            
        clean_message = clean_message[2:] #Deletes first two letters

    #cleans X values from decrypted message
    decrypt_message = decrypt_message.replace('X', '', decrypt_message.count('X'))

    return decrypt_message

# For an excersize I also created the function to encrypt messages, it was only used for testing
def Encrypt(matrix, message, omitted_let):
    
    # cleans message to ensure no spaces, special characters, or omitted letter gets passed through the encrypt process.
    clean_message = ''
    for letter in message:
        if letter.upper() == omitted_let.upper():
            print(f'Error: your string contains the omitted letter {omitted_let}')
            return False
        elif letter.isalpha():
            clean_message += letter.upper()

    encrypt_message = ''
    while len(clean_message) > 0:

        if len(clean_message) == 1:
            clean_message += 'X' #Adds X to end if message is odd
        if clean_message[0] == clean_message[1]:
            clean_message = clean_message[0] + 'X' + clean_message[1:] # Splits pairs with X

        # Finds matrix location for first two letters of clean_message
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == clean_message[0]:
                    row1 = i
                    col1 = j
                if matrix[i][j] == clean_message[1]:
                    row2 = i
                    col2 = j

        # In the same row
        if row1 == row2:
            encrypt_message += matrix[row1][(col1 + 1) % 5]
            encrypt_message += matrix[row2][(col2 + 1) % 5]
        # In the same column
        elif col1 == col2:
            encrypt_message += matrix[(row1 + 1) % 5][col1]
            encrypt_message += matrix[(row2 + 1) % 5][col2]
        else:
            encrypt_message += matrix[row1][col2]
            encrypt_message += matrix[row2][col1]
            
        clean_message = clean_message[2:] #Deletes first two letters

    return encrypt_message
            
    
def main():
    omitted_let = 'J'
    key = 'SUPERSPY'
    # message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    message = 'FOKFRCQOIRFY'
    mess_to_encrypt = 'i like donkeys'
    matrix = CreateMatrix(key, omitted_let)

    print(Decrypt(matrix, message, omitted_let))
    # print(Encrypt(matrix, mess_to_encrypt, omitted_let))

main()

# Assumptions: This uses the the Playfair cipher version which omitts a letter to form a 5x5 matrix. In this case its the J, if the omitted letter is used the decyption is cancelled
# All encrypted messages are even, if the encrypted message is odd the last letter of the message is omitted
# only upper case alphabetical characters will be passed into the decryption function, to handle other cases a cleaning process was done to the message
