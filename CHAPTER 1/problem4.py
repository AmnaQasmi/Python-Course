""" write a python program to print a contents of a directory using the os module search online for the function which does that ? """
import os

def list_directory_contents(path):
    try:
        # Get the list of all files and directories in the specified directory
        # use the os module to list the directory content .
        contents = os.listdir(path)
        # both of below code are use to print the contents of the directory 
        # ye 1 way hai to write
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
            # aur ye 2 way hai to write
            # print (constents)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path of the directory you want to list
directory_path = "/"

# Call the function to list the directory contents
list_directory_contents(directory_path)

