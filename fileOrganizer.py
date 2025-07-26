import os

# Define the directory to organize. Files within this directory will be renamed.
dir = './test'

# Get a list of all file and directory names within the specified directory.
contents = os.listdir(dir)

# Iterate through each item (file/folder) in the directory, starting enumeration from 1.
for i,item in enumerate(contents , start=1):
    # Extract the file extension by splitting the item name at the dot and taking the second part.
    extensions = item.split('.')[1]
    # Rename the file: construct the new path with a sequential number and original extension.
    # The f-string is used for easy formatting of the new file name.
    os.rename(f"./{dir}/{item}", f"./{dir}/{i}.{extensions}")
    
# Print a confirmation message once all files have been processed.
print("the files have been organized")
