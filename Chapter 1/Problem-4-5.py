import os

# Specify the path of the directory (you can also use '.' for current directory)
directory_path = '.'

# Get the list of entries in the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory was not found.")
except PermissionError:
    print("You do not have permission to access this directory.")
