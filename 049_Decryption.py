key = input()
keyvalue={}
for i in range(len(key)):
    keyvalue[key[i]] = chr(i+97)
encryptedmessage = input()
decryptedmessage=""
for letter in encryptedmessage:
    if letter == " ":
        decryptedmessage+= " "
    else:
        decryptedmessage+=keyvalue.get(letter)
print("Decrypted text: "+ decryptedmessage)