import string
key = 'DKVQFIBJWPESCXHTMYAUOLRGZN'
#key = input("Please enter the 26 letter key: ")
User_input = input("Please enter the message: ")
cipher = ""

for c in User_input:
    if c in string.ascii_lowercase:
        index = ord(c) - ord('a')
        cipher = cipher + key[index]
    elif c in string.ascii_uppercase:
        index = ord(c) - ord('A')
        cipher = cipher + key[index]
    else:
        cipher = cipher + c
print("Original Input: " , User_input)
print("Cipher text ", cipher)