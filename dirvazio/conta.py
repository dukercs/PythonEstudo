import os

# define the root directory
root_directory = '/tmp/ValeTeste'

# create an empty dictionary to store subdirectory names and file counts
subdir_counts = {}

# walk through the directory structure
for dirpath, dirnames, filenames in os.walk(root_directory):
    # count the number of files in the current directory
    file_count = len(filenames)
    # add the file count to the appropriate subdirectory in the dictionary
    subdir_counts[dirpath] = file_count

# print the subdirectory names and file counts
for subdir, count in subdir_counts.items():
    print(f"{subdir}: {count}")
