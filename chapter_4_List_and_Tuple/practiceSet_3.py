# Python Tuple

t1 = (1, 2, 3, "Hello", True); # tuple with multiple  elements and data types
t2 = (1,) # tuple with multiple elements
t3 = (1, 2, 3, 4, 5, 4, 7, 5); # tuple with same elements and data types
t4 = (1, 2, 3, 4, 5); # tuple with same elements and data types

print(t3[5]) # Give the element at given index
print(t3.count(5)) # Returns the number of occurrences of an item in the tuple.
print(t3.index(5)) # Returns the index of the first occurrence of an item in the tuple.
print(len(t3)) # Returns the number of items in the tuple.
print(min(t3)) # Returns the smallest element in the tuple (works only with numeric or comparable data)..
print(max(t3)) # Returns the largest element in the tuple (works only with numeric or comparable data)..
print(sum(t3)) # Returns the sum of elements in the tuple (works only with numeric values).
print(5 in t3) # in operator: Checks if an element exists in the tuple.
print(t3 + t4) # + (tuple concatenation): Concatenates two or more tuples.
print(t3 * 2) # * (tuple repetition): Repeats the tuple elements a specified number of times.
a, b, c, d, e = t1 #  Tuple unpacking: Assigns values from the tuple to multiple variables.
print(a, b, c, d, e)
print(sorted(t3)) # sorted(tuple): Returns a sorted list of the tuple’s elements (since tuples are immutable, sorting returns a list).


