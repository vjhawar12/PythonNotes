# a set is an unordered collection of unique immutable elements
my_set = {1, "this", 2, 3, 3}

print(my_set)

# sets cannot be sliced or indiced because they don't retain the order of elements

my_set.add(4)

my_set.update("a", "sentence")

print(my_set)

my_set.remove("a")
print(my_set)

