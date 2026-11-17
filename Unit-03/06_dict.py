marks={                           #dictionary of student name and marks
    "Somya":100,
    "Himani":89,
    "Rohan":33
}
'''
print(marks)
print(type(marks))
print(marks["Somya"])   #values accessed using keys

marks["Rohan"]=56
print(marks["Rohan"])  #dictionary is mutable
'''
#dictionary methods
print(marks.items())  #returns all key:value pairs in the form of tuple
print(marks.keys())
print(marks.values())

marks.update({"Somya":99,"Renu":67})
print(marks)

print(marks.get("Somya"))  #if key doesn't exist--> gives None

print(marks.get("somya2")) #prints None
#print(marks["somya2"]) #returns error

print(len(marks))

new_marks=marks.copy()
print(new_marks)

print(marks.pop("Renu"))
marks.popitem() #removes last item
print(marks)