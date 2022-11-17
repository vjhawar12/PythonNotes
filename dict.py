# dictionaries are python's implementation of a map: a key:value pair
# a dictionary is ordered, changeable, and unique
# key values must be hashable; they must have a constant hash value (a numeric identifier of an object)
# a hash value is the value returned after calling the hash function

# primitive data types (strings, integers, float, complex, boolean, bytes, classes, functions) are all hashable 
# e.g. 

# lists and dictionaries are not hashable

# print(hash(10.2))

# def foo(): 
#     pass 

# print(hash(foo))

# class Class:
#     pass

# print(hash(Class))

# tuples may or may not be hashable

# how to make a dictionary 

dict = {
	1 : "one",
	2 : "two",
	3 : "three"
}

keys = dict.keys()
for i in keys: 
    print(i)

values = dict.values()
for i in values:
    print(i)
    
if 1 in dict.keys():
    print('yes')
else:
    print("no")
    
if "two" in dict.values():
    print('yes')
else:
    print("no")
    

# cannot have a list or dict as a key in a dictoinary because it's not hashable 
# if tuples have mutable values then you can use a tuple as a key in dictoinary

dict = {
	(1, 2, 3) : 2, 
	(4, 5, 6) : 5,
	(7, 8, 9) : 8
}

print(dict)

