def ceaser_cipher(message, shift, mode):
    '''
    For message and shift inputs
    '''
    result = ""

    shift = shift % 26
    for char in message:
        if char.isalpha():
            if mode == "enc":
                result += chr((ord(char) + shift - 65) %26 + 65)
            else:
                result += chr((ord(char) - shift - 65) %26 - 65)
        else:
            result += char
    return result



#For User Input

message = input("Enter your Message: ").upper()
shift = int(input("Enter the value to shift: "))
mode = input("Enter 'enc' to encrypt or 'dec' to decrypt the message: ")

if mode.lower() == 'enc':
    encrypted_message = ceaser_cipher(message, shift, mode.lower())
    print(f"Encrypted Message: {encrypted_message}")
elif mode.lower() == 'dec':
    decrypted_message = ceaser_cipher(message, shift, mode.lower())
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("Invalid mode")
    