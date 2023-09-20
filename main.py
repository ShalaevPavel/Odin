import os
import json
import re

def prettify_json(json_str):
    try:
        parsed_json = json.loads(json_str)
        return json.dumps(parsed_json, indent=4)
    except ValueError:
        return json_str

def process_file(filepath, indent=""):
    with open(filepath, 'r') as file:
        content = file.read()

    # Regular expression to find JSON objects
    json_pattern = re.compile(r'({[^}]+})')

    # Search for and prettify JSON objects in the content
    content = json_pattern.sub(lambda match: prettify_json(match.group(0)), content)

    dependencies = []
    lines = content.split('\n')
    for line in lines:
        if "basename" in line:
            parts = line.split(":")
            if len(parts) == 2:
                basename = parts[1].strip().strip('"')
                dependencies.append(indent + prettify_json(basename))
                dependencies.extend(process_file(basename, indent + "\t"))

    return dependencies

def create_dependency_hierarchy(root_folder, output_file):
    with open(output_file, 'w') as result_file:
        for root, _, files in os.walk(root_folder):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    print(filepath)
                    dependencies = process_file(filepath)
                    result_file.write(filepath + '\n')
                    for dep in dependencies:
                        result_file.write(dep + '\n')


if __name__ == "__main__":
    root_folder = "../../odin_bundle/networks"  # Замените на путь к вашей файловой системе
    output_file = "dependency_hierarchy.txt"  # Имя файла для записи иерархии зависимостей
    create_dependency_hierarchy(root_folder, output_file)

