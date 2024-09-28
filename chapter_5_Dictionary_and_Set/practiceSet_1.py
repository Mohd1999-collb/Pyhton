
def hello(a, b):
    print(a+b)

marks = {
    "Ram" : 50,
    "Shyam" : 60,
    "Gopal" : 70,
    "Ravi" : 80,
    "Anil" : 90,
    "Ramesh" : 55,
    "Suresh" : 75,
    "Mahesh" : 65,
    "Nikhil" : 85,
    "Priya" : 95,
    "Vijay" : 85,
    0 : 100,
    1.5 : 200,
    "list" : ["Cow", 'Cat', "Dog", "Elephant"],
    "tuple": ("Mca", "Mtech", "Bcomputer"),
    True : True,
    "greet" : hello
}

print(marks)
print(marks["Ram"]) # Returns the value for the specified key. If the key is not found, it returns the KeyError.

# Dictonary mathod
# print(marks.keys()) # Returns a view object that displays a list of all the keys in the dictionary.
# print(marks.values()) # Returns a view object that displays a list of all the values in the dictionary.
# print(marks.get("Rama", "Not found")) # Returns the value for the specified key. If the key is not found, it returns the default value (which is None if not provided).
# print(marks.items()) # Returns a view object that displays a list of key-value pairs (as tuples) in the dictionary.
# marks.update({"Ram" : 55, "Kunal" : 69})  # Updates the dictionary with elements from another dictionary or an iterable of key-value pairs or append the key in dictionary if the key is not found.

# print(marks.pop("Anil", 'Not Found')) # Removes the specified key and returns its value. If the key is not found, it returns the default value.
# print(marks.popitem()) # Removes and returns the last key-value pair as a tuple. This method raises a KeyError if the dictionary is empty.
# marks.clear() # Removes all items from the dictionary, leaving it empty.
# print(marks.setdefault("Ram Kumar", "99"))  # Returns the value of the key if it exists. If the key doesn't exist, it inserts the key with the default value and returns the default.

l = ['a', 'b', 'c', 'd', 'e', 'f']

# obj = dict.fromkeys(l, "Hello Talib") # Creates a new dictionary with keys from the specified iterable, and sets all values to the specified value (or None if no value is provided).
# print(obj)

# myDict = marks.copy() # Returns a shallow copy of the dictionary.
# print(myDict);

# print("Ram" in marks) # The in keyword checks if a key exists in the dictionary.

# del marks["Ram"] # The del statement removes a key-value pair from the dictionary.

# print(max(l)) # Find max  or min key 
# print(max(l.values())) # Find max  or min value 


words = {
    "Seb": "a sweet, edible fruit",
    "Kela": "a yellow, edible fruit",
    "Cherry": "a red, sour fruit",
    "Khajoor": "a sweet, berry fruit",
    "Anjir": "a purple, edible fruit",
    "Angoor": "a purple, edible fruit",
    "Kiwi": "a green, edible fruit",
    "Nimbu": "a yellow, edible fruit",
    "Aam": "a yellow, edible fruit",
    "Santra": "a orange, edible fruit",
    "Aadu": "a green, edible fruit",
    "Ber": "a purple, edible fruit",
}

word = input("Enter the key name : " )
print(words.get(word, "Not Found"))