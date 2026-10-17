#practice questions

#1-store following words meanings in a python dictionary and print the dictionary
#{name: "Sudhanshu kumar"
# brand: "Ford","BMW", "Audi"}
dict ={
    "name": "Sudhanshu kumar",
    "brand": ["Ford","BMW", "Audi"],
}
print(dict) #prints the dictionary


#2- you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are required for the following subjects? Store the subjects in a set and print the total number of classrooms are needed by all students.

class_count = {
    "python","java","c++","javascript","java",
    "python","c++","c"
}

print(class_count) #prints the total number of classes in the set
print(len(class_count)) #prints the length of the set collection

#3-WAP to enter markes of 3 subjects fron the user and store them in a dictionary. start with an empty dictonary & add one by one . use subject name as key & marks as value.

marks = {}
x = int(input("enter phy :"))
marks.update({"phy": x})

x = int(input("enter math :"))
marks.update({"math": x})

x = int(input("enter chem :"))
marks.update({"chem": x})

print(marks)



