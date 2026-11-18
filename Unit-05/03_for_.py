for i in range(1,6):
    print(i)

for i in range(1,6,2):     #(start,stop,step)
    print(i)

#display items of list one by one
list1=["Somya","Manisha","Himesh","Bhumi","Isha"]
for l in list1:
    print(l)
#tuple
tup1=(9,8,6,0)
for t in tup1:
    print(t)
#string
name="Somya"
for n in name:
    print(n)

#for with else
l=[1,4,5]
for i in l:
    print(i)
else:
    print("done") #printed whenloop exhausts