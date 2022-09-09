#Jag pluggar på Nackademin
#Qhn wsbnnhy we Uhjrhkltpu
text = input("Text to encode: ")
s = int(input("Key to use: "))
result = ""
for i in range(len(text)):
        char = text[i]
  
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
            
print(result)