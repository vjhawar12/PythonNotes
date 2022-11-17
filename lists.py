# python lists are mutable, ordered, and allow duplicates

lis = ["one", "two", "three", "four"]

# remove by index in list
del lis[1]

# remove by element
lis.remove("four")

print(lis) 

# add elements to list
lis.append("five")
lis.extend(["six", "seven"])
print(lis)	
lis.insert(1, "random")

print(lis)

# slicing allows you to access part of a list between a given range
lis[1:3] = ["THREE", "FIVE"]
lis = lis[1:3]
print(lis)

# creating nested lists
lis = [
	[0, 1], [2, 3], [4, 5],
 	[6, 7], [8, 9], [10, 11],
	[12, 13], [14, 15], [16, 17],
]

for i in lis: 
    for j in i:
        print(j, end=", ")
    print()