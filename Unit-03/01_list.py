'''
colors=["orange","grapes","banana"]
print(colors[2])

colors[0]="kiwi"
print(colors)  # unlike strings, lists are mutable 

values=[0,"somya",True]  #list can store multiple datatypes
print(values)

print(values[0:2])  #list slicing
'''

#list methods

names=["Somya","Bhumi","Manisha","Himesh","Isha"]
names.append("Himani")  #adds the element at the end of the list
print(names)

names.sort() #arranges data in ascending order
print(names)

names.reverse()
print(names)

names.insert(2,"Ramesh")  #inserts element at specific index
print(names)

print(names.pop(2))  #removes an element at specific index and returns the value
print(names)

names.remove("Himani")  #removes a particular element of the list
print(names)

print(names.index("Somya")) #returns index of the element
