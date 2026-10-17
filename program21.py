#4-Figure out a way to store 9 & 9.0 as separate values in the set (you can take help of built-in data types)

#first soluction
values = {9 , "9.0"}
print(values)
#second soluction
second = {
    ("float",9.0),
    ("int",9)
}
print(second)