# a generator is an easier way to implement an iterator 
# generators are functions that yield values
# generators are used when you're working with large streams of data that require lots of memory

def foo():
    for i in range(10):
        yield i
        
print(type(foo))

func = foo() 

print(type(func))

for i in func: 
    print(i)

def _range(start, end): 
    current = start
    while current < end: 
        yield current
        current += 1
        
func = _range(1, 10)
for i in func: 
    print(i)