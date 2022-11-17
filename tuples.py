# a tuple is an immutable list

tup = (1, 2, 3)

tup1 = (1, )

# tuples can be sliced, iterated, and only modified if the element inside is mutable 
# you can also have nesteed tuples

tup2 = (1, 2, [3, 4])
tup2[2][0] = "three"

print(tup2)

# tuples are faster for iterating than lists are
