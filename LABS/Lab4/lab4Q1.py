# -*- coding: utf-8 -*-
"""Lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k7uAY5rpSYMWq9V3dkTcCwmDG2pQ-6jj
"""

PlainText = input("Please enter the plain text: ")

Key = 'XMCKL'

Key_Ascii_array = [0 for i in range (len(PlainText))]
for i in range(len(Key)):
  Key_Ascii_array[i] = ord(Key[i])

PlainText_Ascii_array = [ 0 for i in range (len(PlainText))]

for i in range(len(PlainText)):
  PlainText_Ascii_array[i] = ord(PlainText[i])
  #PlainText_Ascii_array[i] = bin(ord(PlainText)).replace("0b","")

PlainText_Ascii_array

Key_Ascii_array

#Encription
Cipher_Text_array= [0 for i in range (len(PlainText))]
for i in range(len(PlainText)):
  Cipher_Text_array[i] = chr(PlainText_Ascii_array[i] ^ Key_Ascii_array[i])

Cipher_Text_array

Decript_Text_Array = [0 for i in range (len(PlainText))]
for i in range(len(PlainText)):
  Decript_Text_Array[i] = chr(ord(Cipher_Text_array[i]) ^ Key_Ascii_array[i]);

Decript_Text_Array

PlainText = input("Please enter the plain text: ")

Key = 'XMCKL'
Key
Key_Ascii_array = [0 for i in range (len(PlainText))]
for i in range(len(Key)):
  Key_Ascii_array[i] = ord(Key[i])

PlainText_Ascii_array = [ 0 for i in range (len(PlainText))]

for i in range(len(PlainText)):
  PlainText_Ascii_array[i] = ord(PlainText[i])
  #PlainText_Ascii_array[i] = bin(ord(PlainText)).replace("0b","")

PlainText_Ascii_array

Key_Ascii_array

#Encription
Cipher_Text_array= [0 for i in range (len(PlainText))]
for i in range(len(PlainText)):
  Cipher_Text_array[i] = chr(PlainText_Ascii_array[i] ^ Key_Ascii_array[i])

Cipher_Text_array

Decript_Text_Array = [0 for i in range (len(PlainText))]
for i in range(len(PlainText)):
  Decript_Text_Array[i] = chr(ord(Cipher_Text_array[i]) ^ Key_Ascii_array[i]);

Decript_Text_Array