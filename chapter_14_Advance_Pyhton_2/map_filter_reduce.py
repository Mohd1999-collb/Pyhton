from functools import reduce
l = [1, 2, 3, 4, 5]

taransform = lambda x:x+2

# map 

result = map(taransform, l)

print(list(result)) # Output: [3, 4, 5, 6, 7]

# filter

result = filter(lambda x: x % 2 == 0, l)

print(list(result)) # Output: [2, 4]

# reduce


result = reduce(lambda x, y: x+y, l)

print(result) # Output: 15
