userinput = input('Please enter the message to caesar cipher: ')

def Cifer(userinput,shift_key):
    cipher = ''
    for char in userinput:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift_key - 65)%26 +65)
        else:
            cipher = cipher + chr((ord(char) + shift_key - 97)%26 +65)
    return cipher

shift_key= int(input("Enter the shift key: "))
print("The encripted message is: ", Cifer(userinput,shift_key))