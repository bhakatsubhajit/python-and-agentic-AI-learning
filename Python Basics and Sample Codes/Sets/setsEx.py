numSets = {34,23,12,78}

print(type(numSets))

# sets are unordered, so we cannot access them using an index like we do with lists or tuples. 
# However, we can perform various operations on sets, such as adding or removing elements
# checking for membership, and performing set operations like union, intersection, and difference.

# print(numSets[2]) check above line to see the error message.
numSets.add(45)
print(numSets)
numSets.add(45)
print(numSets) # sets does not allow duplicate values so no changes in result.

numSets.discard(67) # discard method removes an element from the set if it is present. If the element is not present, it does nothing.

print(numSets)

#set operations

setA = {56, 22, 33, 11,90}
setB = {22, 11, 45, 67}

#union 
unionSet = setA.union(setB)

print(unionSet)

#intersection

interSet = setA.intersection(setB)
print(interSet)