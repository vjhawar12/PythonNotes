# an iterable can be looped over / iterated with an iterator 
# iterables need to have  __iter__() 
# iterators are objects with state. they remember the position during iteration
# iterators can also get the next value using the __next__() method that they contain

lis = [1, 2, 3, 4, 5]

iterator = iter(lis) # getting the iterator of list object
print(dir(lis)) # since lis has an __iter__() it's an iterable
print(dir(iterator)) # since iterator has both __iter__() and __next__() its both iterable and an iterator

class Range: # creating custom range class 
    def __init__(self, start, end): 
        self.current = start
        self.end = end 
        
    def __iter__(self): # returning instance of class which is an iterator because it has __next__()
        return self
    
    def __next__(self): # defining __next__() method which makes this class an iterator
        if self.current > self.end: 
            raise StopIteration
        
        temp = self.current
        self.current += 1
        return temp
    
ten = Range(0, 10)

for i in ten: 
    print(i)
    
