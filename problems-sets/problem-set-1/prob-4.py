""" Write a python program to print the contents of a directory using the os module.
Search online for the function which does that."""
import os

def print_directory_contents(path):
    try:
        
        directory_contents = os.listdir(path)
        print(f"Contents of '{path}':")
        
        
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied for accessing '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = "/New folder"  
print_directory_contents(directory_path)
