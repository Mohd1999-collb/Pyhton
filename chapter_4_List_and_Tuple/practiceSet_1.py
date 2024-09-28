# Python List

# firstFruit = input("Enter first fruit name : " )
# secondFruit = input("Enter second fruit name : " )
# thirdFruit = input("Enter third fruit name : " )
# fourthFruit = input("Enter fourth fruit name : " )
# fifthFruit = input("Enter fifth fruit name : " )
# sixthFruit = input("Enter sixth fruit name : " )
# seventhFruit = input("Enter seventh fruit name : " )

# fruits = [firstFruit, secondFruit, thirdFruit, fourthFruit, fifthFruit, sixthFruit, seventhFruit]
# print("Fruit lists arr : ", fruits)

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# List methods 
print(type(fruits))
print(fruits[0 : 5])
print(fruits[5])
fruits.append("cake") # Adds an item to the end of the list.
fruits.insert(2, "litchi") # Inserts an item at a specific position in the list.
fruits.remove("apple") # Removes the first occurrence of an item from the list.
print(fruits.pop(3)) #  Removes and returns the item at the given index. If no index is specified, it removes the last item.
# fruits.clear(); # Removes all items from the list.
print(fruits.index("cherry")) # Returns the index of the first occurrence of an item.
print(fruits.count("cherry")) # Returns the number of occurrences of an item in the list.
fruits.sort() # Sorts the list in ascending order. 
fruits.sort(reverse=True) # pass the reverse=True argument to sort in descending order.
fruits.reverse() # Reverses the order of the list in place.
# copied_list = fruits.copy() # Returns a shallow copy of the list.
print(len(fruits))  
copied_list = [2, 3, 5]
print(sum(copied_list))  
print(max(copied_list))  
print(min(copied_list))  