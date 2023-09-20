import os
import re
import json

# Specify the path to the folder containing .py files
folder_path = "../../odin_bundle/networks"

# Function to prettify JSON-like data within a Python file
def prettify_json_like_data_in_py_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            # Use regular expression to find JSON-like structures
            json_matches = re.findall(r'{[^}]*}', file_contents)
            for match in json_matches:
                try:
                    formatted_json = json.dumps(json.loads(match), indent=4)
                    file_contents = file_contents.replace(match, formatted_json)
                except json.JSONDecodeError:
                    continue
            with open(file_path, 'w', encoding='utf-8') as updated_file:
                updated_file.write(file_contents)
            print(f'JSON-like data in file {file_path} successfully prettified.')
    except Exception as error:
        print(f'An error occurred while prettifying JSON-like data in file {file_path}: {error}')

# Iterate through all files in the specified folder
for root, directories, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            prettify_json_like_data_in_py_file(file_path)
