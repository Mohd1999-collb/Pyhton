
import os

# Opens a file and returns a file object. You can specify the mode in which the file is opened (e.g., read, write, append, etc.).
f = open('chapter_9_File_Handling/file.txt', "r")

# data = f.read()  # Reads the entire content of the file as a string.

# File handling methods

# content = f.readline() # Reads a single line from the file.
content = f.readlines() # Reads all lines in a file and returns them as a list of strings.

# f1 = open('chapter_9_File_Handling/writeFile.txt', "w") 
# f1.write("Hello, world...........") # Writes a string to the file. If the file does not exist, it will be created. If it exists, the content will be overwritten (in write mode).

lines = ["Hello\n", "Word\n", "Goood\n"]
# f1.writelines(lines) # Writes a list of strings to the file.

# f1.seek(2) # Moves the file cursor to a specified position. Useful for reading or writing at a specific location in the file.
# position = f1.tell() # Returns the current position of the file cursor.

# The with statement ensures that files are properly opened and closed. It is a more Pythonic way of handling files since you don’t need to explicitly close the file.

with open("chapter_9_File_Handling/newWriteFile.txt", "r") as f2 :
    content = f2.read()
    print(content)


# os Module Methods --> You can use the os module to perform operations like checking if a file exists, removing a file, or renaming it.

# (a) Check if a file exists

# if os.path.exists("chapter_9_File_Handling/writeFile.txt") :
#     print("File exists.")
# else :
#     print("File does not exist.")


# (b) Remove a file
# os.remove("chapter_9_File_Handling/writeFile.txt")

# (c) Rename a file 
# os.rename('chapter_9_File_Handling/writeFile.txt', 'chapter_9_File_Handling/newWriteFile.txt')

# (d) Get file size
# file_size = os.path.getsize('chapter_9_File_Handling/newWriteFile.txt')  # Returns file size in bytes
# print(f"File size: {file_size} bytes")

# If you want to add content to an existing file without overwriting its data, use the append mode 'a'.
# with open('chapter_9_File_Handling/newWriteFile.txt', 'a') as file:
#     file.write("\nThis is an appended line.")


with open('chapter_9_File_Handling/poem.txt', 'r') as text :
    lines = text.read()
    if "twinkle" in lines:
        print("The word 'twinkles' is found in the poem.")
    else :
        print("The word 'twinkles' is not found in the poem.") 

# f.close()


