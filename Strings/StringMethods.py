sample ="hello world"    # Strings are immutable

num = len(sample)
# print(num)

# print(sample.upper(), sample)
# print(sample.capitalize())
# print(sample.title())

sampleTxt =" hello world " 

# print(sampleTxt.strip())
# print(sampleTxt.lstrip())
# print(sampleTxt.rstrip())

# sampleTextNew = sampleTxt.strip()
# print(sampleTextNew.find("ello")) # returns the first index of the occurence in the string
# print(sampleTextNew.replace("ello", "i")) # replaces the string

# fruitNames = "Apple,Banana,Orange"

# print(fruitNames.split(",")) # returns the fruit names a list
# print(type(fruitNames.split(",")))

# print(",".join(fruitNames.split(",")))

text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False