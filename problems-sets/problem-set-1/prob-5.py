# Label the program written in problem 4 with comments. 
#using os module
import os

def print_directory_contents(path):
    try:
        #getting the list of all files and directories
        directory_contents = os.listdir(path)
        print(f"Contents of '{path}':")
        
        # print the content
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

#Example usage
directory_path = "/New folder"  #current directory
print_directory_contents(directory_path)