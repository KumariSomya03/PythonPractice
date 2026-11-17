'''
s={1,5,6} #set
d={} #empty dictionary
e=set() #empty set

s1={1,3,3,4,4} 
print(s1)  #doesn't store duplicate values

#set methods
s1.add(56)
print(s1)  #insert at beginning

#sets are unindexed

print(len(s1))

s1.remove(3)
print(s)

s1.pop()
print(s1)  #removes a random element

'''
s={18,'18'}
print(s)

#SET OPERATIONS
s1={1,4,5,6,7}
s2={6,7,8,9,0}

print(s1.union(s2))
print(s2.intersection(s2))
print(s1.isdisjoint(s2)) 
print(s1.difference(s2))
print(s1-s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))