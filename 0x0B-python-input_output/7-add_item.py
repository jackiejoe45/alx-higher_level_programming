#!/usr/bin/python3
import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# File name to save the JSON data
filename = "add_item.json"

# Initialize an empty list or load existing data
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
