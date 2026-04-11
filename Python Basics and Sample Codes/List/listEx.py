# lists are ordered, mutable, and allow duplicate elements.
marks = [80,70, 45,65,20]
mixed = [10.09, 45, "Hello", True]
newList = [45,78,56]
print(marks[-1])
print(marks[3])
print(marks[2:4])

'''marks.append(85) # adds an element at the end of the list.
print(marks)'''
marks.pop() # removes the last element from the list.
print(marks)

marks.insert(2,46) # inserts an element at 2nd index.
print(marks)

marks.extend(newList) # adds all the elements of newList list to marks list.
print(marks)
print(marks.count(45)) # counts the number of occurrences of 45 in the list.


print(marks)
marks.sort() # sorts the list in ascending order.
print(marks)
marks.reverse() # reverses the order of the list.
print(marks)