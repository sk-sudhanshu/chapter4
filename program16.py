#dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.


dict ={
    "name": "Sudhanshu kumar",
    "brand": "Ford",
    "model_name": "Mustang",
    "year": 1964,
    12: "you store integer value in dictionary",
    23.2: "you store float value in dictionary",
}

print(dict["brand"]) #accessing value using key
print(dict["name"]) #accessing value using key
print(dict["model_name"]) #accessing value using key
print(dict[12]) #accessing value using key
print(dict[23.2]) #accessing value using key

dict["year"] = "2020" #updating value using key
print(dict["year"]) #accessing updated value using key

dict["color"] = "red" #adding new key-value pair
print(dict["color"]) #accessing value using key

empty_dict = {} #empty dictionary
empty_dict["name"] = "Sudhanshu kumar" #adding new key-value pair
print(empty_dict)


#nested dictionary

student = {
      "Name": "Sudhanshu kumar",
      "subjects": {
          "Maths": 80,
          "Science": 90,
          "English": 85
      }                   #the value of the key "subjects" is another dictionary
}

print(student["Name"]) #accessing value using key
print(student["subjects"]) #accessing value of nested dictionary using key 
print(student["subjects"]["Science"]) #accessing value of nested dictionary using key

