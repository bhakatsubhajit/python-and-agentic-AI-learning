sentence = "Coding in Python is fun"

lowercaseText = sentence.lower()
count = 0
for i in lowercaseText:
    if  i == 'a' or i=="e" or i =="i" or i=="o" or i=="u":
        count = count+1
print("number of vowels in the text in loop :", count)
