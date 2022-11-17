from collections import deque 

# deques are like lists but faster to remove items from the front and the back. 
# lists are only fast to remove items from the end 
# cannot use slicing for deque

# creating an empty deque 
d = deque()

print(d)

# deques takes 2 arguments: an iterable and a size
d = deque([1, 2, 3], 5)
print(d)
    
d.append(4) # add at end
d.appendleft(0) # add at start

for i in d: # a deque's an iterble
    print(i)
    
d.append(6) # does not raise error if maxlen is exceeded, but will just not add the element


    

    