import os

# Specify the directory path
directory_path = 'C:/Users/lenovo/Desktop/AccioJob/Assesment/Python'

# List the contents of the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of the directory '{directory_path}':")
    print(contents)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access the directory '{directory_path}'.")
