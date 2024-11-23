import os

def write_dir_structure(path, file, indent=0):
    # List all files and directories in the given path
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        
        # Skip the 'node_modules' and 'venv' directories
        if 'node_modules' in entry or 'venv' in entry:
            continue
        
        # Write the current entry with indentation to the file
        file.write('  ' * indent + entry + '\n')
        
        # If it's a directory, recursively call this function
        if os.path.isdir(entry_path):
            write_dir_structure(entry_path, file, indent + 1)

# Set the root directory (current directory)
root_dir = os.getcwd()

# Open the file in write mode
with open("directory_structure.txt", "w") as file:
    # Write the directory structure starting from the root directory
    write_dir_structure(root_dir, file)

print("Directory structure has been written to 'directory_structure.txt'")
