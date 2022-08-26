
def EncryptMessage(message, key):
    encryptedMessage = ""
    for i in range(len(message)):
        encryptedMessage += chr(ord(message[i]) + key)
    return encryptedMessage
  
def CreateKey(message, key):
    encryptedMessage = ""
    for i in range(len(message)):
        encryptedMessage += chr(ord(message[i]) + key)
    return encryptedMessage

def DecryptMessage(encryptedMessage, key):
    decryptedMessage = ""
    for i in range(len(encryptedMessage)):
        decryptedMessage += chr(ord(encryptedMessage[i]) - key)
    return decryptedMessage

def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))
    encryptedMessage = EncryptMessage(message, key)
    print("Encrypted message:", encryptedMessage)
    decryptedMessage = DecryptMessage(encryptedMessage, key)
    print("Decrypted message:", decryptedMessage)
    key = CreateKey(message, key)
    print("Key:", key)


main()
