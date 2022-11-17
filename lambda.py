# a lambda function is a condensed function 

def isOdd(num): 
    return num % 2 == 1

print(isOdd(int(input())))

#x is the argument, after the colon is the function statement, and the adjacent set of brackets are what refers to x
print((lambda x: x % 2 == 1)(int(input())))

# lambdas can be passed into functions
def foo(func, x): 
    func(x)
    
foo(lambda x: print(x), 12)

