#Methods in dictionaries

dict ={
    "name": "Sudhanshu kumar",
    "brand": "Ford",
    "model_name": "Mustang",
    "year": 1964,
    12: "you store integer value in dictionary",
    23.2: "you store float value in dictionary",
}

print(dict.keys()) #returns all the keys in the dictionary
print(dict.values()) #returns all the values in the dictionary
print(dict.items()) #returns all the key-value pairs in the dictionary
print(len(dict)) #returns the number of key-value pairs in the dictionary
pairs = list(dict.items())
print(pairs[1]) #accessing the second key-value pair in the dictionary

print(dict.get("name")) #returns the value of the specified key
print(dict.update({"year": 2020})) #updates the value of the specified key
print(dict) #prints the updated dictionary
