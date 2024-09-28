# Adds a multiple element to the set.
# marks = {1, 2, 3, 4, 5, 6, 7, 8, 9} # Set

marks = set() # Empty set

# Adds a single element to the set.
marks.add(1)
marks.add("1")
marks.add(100)
marks.add(8)
marks.add(7)
marks.add(78)
marks.add(3)
marks.add(0)

# Set methods
# marks.remove(1) # Removes a specified element from the set. Raises a KeyError if the element is not found.
# marks.discard(0) # Removes a specified element from the set if it exists, and does nothing if the element is not found (no KeyError is raised).
# p = marks.pop() # Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
# print(p)
# marks.clear() # Removes all elements from the set, making it empty.

# result = marks.union({200, 1, 500, 3, 5}) # Returns a new set containing all the unique elements from the original set and the other sets.

# marks.update({2005}) # Adds elements from another set or iterable to the current set.

# result = marks.intersection({200, 1, 500, 3, 5}) # Returns a new set with elements that are common to the original set and all the other sets.

# marks.intersection_update({200, 1, 3}) # Updates the set, keeping only the elements found in both the original set and the other sets.

# result = marks.difference({200, 1, 500, 3, 5}) # Returns a new set with elements that are in the original set but not in the other sets.

set1 = set()

a  = int(input("Enter the first number : " ))
b  = int(input("Enter the second number : " ))
c = int(input("Enter the third number : " ))
d  = int(input("Enter the fourth number : "))
e = int(input("Enter the fifth number : "))
f = int(input("Enter the sixth number : "))
g = int(input("Enter the seventh number : "))
h = int(input("Enter the eighth number : "))
set1.add(a)
set1.add(b)
set1.add(c)
set1.add(d)
set1.add(e)
set1.add(f)
set1.add(g)
set1.add(h)
print(set1)  
print(len(set1)) 