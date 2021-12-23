# -*- coding: utf-8 -*-
"""LAB3_Q2_Transposition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uml13SsHtWstcz_m0CM_2nKzvD3Rp2wF
"""

import numpy as np
import string

Plaintext= 'Attack postponed until two am'
Columns= 7
Key= [4 ,3, 1 ,2 ,5 ,6 ,7]

Plaintext = Plaintext.lower()
Plaintext=Plaintext.replace(" ","")

Plaintext_Array = [char for char in Plaintext ]
Plaintext_Array= np.array(Plaintext_Array)

Size_Array=(int(len(Plaintext_Array)/Columns))

for i in range (122-Size_Array+1,123):
  Plaintext_Array=np.append(Plaintext_Array,chr(i))

Plaintext_Array

Plaintext_Array=Plaintext_Array.reshape(4,7)

Cypher_Text = []

for i in range (len(Key)):
  col = Key[i] -1
  Cypher_Text=np.append(Cypher_Text,Plaintext_Array[:,col])

Cypher_Text

Cypher_Text_string=""
for element in Cypher_Text:
  Cypher_Text_string+=element

Cypher_Text_string