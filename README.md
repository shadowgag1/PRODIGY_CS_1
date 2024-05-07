The caesar_cipher function takes three arguments: message (the input message), shift (the shift value), and mode ('enc' or 'dec').
Inside the function, the shift value is adjusted to be within the range of 0-25 using the modulo operator shift = shift % 26.
The function iterates over each character in the message:

If the character is an alphabetic character, it is shifted based on the mode ('enc' or 'dec') using the formula chr((ord(char) + shift - 65) % 26 + 65) for encryption and chr((ord(char) - shift - 65) % 26 + 65) for decryption.
If the character is not an alphabetic character, it is kept as it is.


The shifted characters are concatenated to the result string.
The function returns the result string, which is the encrypted or decrypted message.
The user is prompted to enter the message, shift value, and mode ('enc' or 'dec').
The caesar_cipher function is called with the user input, and the encrypted or decrypted message is printed.

Here's an example usage:
Enter the message: HELLO WORLD
Enter the shift value: 3
Enter 'enc' to encrypt or 'dec' to decrypt: enc
Encrypted message: KHOOR ZRUOG
To decrypt the message, you would run the code again and enter 'dec' as the mode, along with the same shift value (3):
Enter the message: KHOOR ZRUOG
Enter the shift value: 3
Enter 'enc' to encrypt or 'dec' to decrypt: dec
Decrypted message: HELLO WORLD
Note: The Caesar Cipher is a simple substitution cipher and is not considered a secure encryption method for modern applications. It's primarily used for educational purposes or as a basic example of cryptography.
