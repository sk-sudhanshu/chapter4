#Methods in sets...

setmethods = set()
setmethods.add(1)#adds an integer to the set
setmethods.add("banana")#adds a string to the set
setmethods.add((1,2,3))#adds a tuple to the set

print(setmethods) #prints the set collection


clearset = {1,2,3,4,5}
clearset.clear() #clears all elements from the set
print("clearset:", clearset) #prints the cleared set


removeset = {1,2,3,4,5}
removeset.remove(3) #removes the specified element from the set
print("the removed set is:", removeset) #prints the set after removing the specified element

popset = {1,2,3,4,5}
popset.pop() #removes and returns an arbitrary element from the set
print("the popped set is:", popset) #prints the set after popping an arbitrary element

#important methods in sets
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
 
print("union of set1 and set2 is:", set1.union(set2)) #returns the union of two sets
print("intersection of set1 and set2 is:", set1.intersection(set2)) #