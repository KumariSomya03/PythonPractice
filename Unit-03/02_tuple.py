'''
a=(1,2,5,6)
print(type(a))

b=(1)
print(type(b))  #returns int

c=(1,)  #single element tuple
print(type(c))  #returns tuple

t=(1,67,"Somya",True) #tuple can store multiple datatype values
#t[0]=False ---->generates error (tuple is immutable)

'''
#tuple methods
tup=(1,34,"Somya",True,"orange")
num=tup.count(34)  #counts the occurenece of element in a tuple
print(num)

i=tup.index("Somya")
print(i)

n=len(tup)
print(n)

new_tup=tup*3  #repetition
print(new_tup)

print(3 in tup)  #membership

print(tup[0:4])  #tuple slicing