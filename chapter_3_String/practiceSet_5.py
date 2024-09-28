letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
a = 'Harry is a good boy\nbut not a bad \'boy\''

print(letter)
print(len(a))

# String method
text = "hello world!"
text1 = "  Hello, World!  "
text2 = "apple,banana,cherry"
text3 = "HelloWorld"
text4 = "123456"
text5 = "hello world, hello GPT"
word = "amazing"


print(word[1 : 5 : 2])  # Give the substring from index 1 to index 4 but skip the 2 charcater of substring
print(text[1 : 5])  # Give the substring from index 1 to index 4
print(text.lower());
print(text.upper());
print(text1.strip()); #Removes leading and trailing whitespace.
print(text2.split(",")); #Splits a string into a list based on a delimiter.
print(text.find("World")); #Returns the index of the first occurrence of a substring, or -1 if not found.
print(text.startswith("Hello")); #Checks if a string starts with the specified substring.
print(text.endswith("!")); #Checks if a string ends with the specified substring.
print(text3.isalpha()); #Returns True if all characters in the string are alphabetic.
print(text4.isdigit()); #Returns True if all characters in the string are digit.
print(text.capitalize()); #Capitalizes the first letter of the string.
print(text.title()); #Capitalizes the first letter of every word in the string.
print(text5.count("hello")); #Returns the number of occurrences of a substring..   