num = 5
result =[]
for i in range(1,11):
    result.append(num*i)

print(result)


# using list comprehension
resultNew = [5*i for i in range(1,11)]
print(resultNew)