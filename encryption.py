def encode(original_message, X):
    encoded_message = ""
    for i in range(0, len(original_message)):
        encoded_char = ord(original_message[i])
        # check space
        if original_message[i] != " ":
            encoded_char = encoded_char + X
            if encoded_char > 90:
                encoded_char = encoded_char - 26
        encoded_message += chr(encoded_char)
    print(original_message)
    print(encoded_message)
    return encoded_message

def writeFile(message):
    f = open("encryption.txt", "w")
    f.write(message)
    f.close()
    
def decode(X):
    f = open("encryption.txt", "r")
    print(encode(f.read(), 26-X))
    f.close()

while True:
    print("1 - Encoded Text")
    print("2 - Write encoded text")
    print("3 - Decode")
    print("0 - Exit")
    choice = int(input("Please enter your option: "))

    if choice == 1:
        txt = input("Please enter the original text: ")
        X = int(input("Please enter the encryption key: "))
        output_text = encode(txt, X)
    elif choice == 2:
        writeFile(output_text)
    elif choice == 3:
        X = int(input("Please input the encryption key: "))
        decode(X)
    else:
        break