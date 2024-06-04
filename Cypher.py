def generate_cipher_key(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates and keep order
    key += ''.join([char for char in alphabet if char not in key])
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def decrypt_pair(a, b, matrix):
    row1, col1, row2, col2 = -1, -1, -1, -1
    for i in range(5):
        if a in matrix[i]:
            row1, col1 = i, matrix[i].index(a)
        if b in matrix[i]:
            row2, col2 = i, matrix[i].index(b)
    if row1 == row2:  # Same row
        a_dec = matrix[row1][(col1 - 1) % 5]
        b_dec = matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        a_dec = matrix[(row1 - 1) % 5][col1]
        b_dec = matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle swap
        a_dec = matrix[row1][col2]
        b_dec = matrix[row2][col1]
    return a_dec + b_dec

def decrypt_message(message, key):
    message = ''.join(filter(str.isalpha, message.upper()))  # Clean and prepare the message
    matrix = generate_cipher_key(key)
    print(matrix)
    decrypted_text = ""
    for i in range(0, len(message), 2):
        decrypted_text += decrypt_pair(message[i], message[i+1], matrix)
    return decrypted_text.replace('X', '')

if __name__ == "__main__":
    import sys
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = decrypt_message(encrypted_message, key)
    print(decrypted_message)