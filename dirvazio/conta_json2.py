import os
import json

# Set the root directory
root_directory = "/tmp/ValeTeste"

# Initialize an empty dictionary to hold the subdirectory counts
subdir_counts = {}

# Walk through all directories in the root directory
for subdir, dirs, files in os.walk(root_directory):
    # Get the count of files in this subdirectory
    file_count = len(files)
    # Add the count to the dictionary, keyed by subdirectory name
    subdir_counts[subdir] = file_count

# Convert the dictionary to a list of dictionaries, with each dictionary containing a subdirectory name and file count
subdir_counts_list = [{"{#DIRNAME}": subdir, "{#DIRLEN}": file_count} for subdir, file_count in subdir_counts.items()]

# Convert the list to JSON
json_data = json.dumps(subdir_counts_list)

# Write the JSON data to a file
with open("subdir_counts.json", "w") as f:
    f.write(json_data)
