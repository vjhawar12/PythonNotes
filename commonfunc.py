class A: 
    b = 11
    def __init__(self):
    	self.a = 10
    
obj = A()

# getattr() determines whether or not an object has a given attribute
print(getattr(obj, "a"))
print(getattr(A, "b"))
try:
	print(getattr(obj, "c"))
except AttributeError: 
    print('no such field')

# join() concatenates multipes strings
string = "".join(["this", " ", "is"])
print(string)

# max/min() determines the max/min of >= 2 objects
# for strings its alphabetic and for iterables its objects 

print(max(10, 12))
print(min("a", "b"))

obj = A()
obj.a = 12

obj2 = A()
obj2.a = 15 

# you can use custom comparator function
val = max([obj, obj2], key=lambda x: x.a)

print(type(val))

 