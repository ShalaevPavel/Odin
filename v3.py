import os


# Функция для анализа содержимого Python файла и поиска зависимостей
def find_dependencies(file_path):
    dependencies = []
    with open(file_path, 'r') as file:
        for line in file:
            for keyword in ('Common', 'Gen3', 'Model3', 'ModelY', 'Tutorials'):
                if keyword in line:
                    parts = line.split('"')
                    if len(parts) >= 2:
                        dependency = parts[1]
                        dependencies.append(dependency)
    return dependencies


# Функция для создания иерархии зависимостей
def build_dependency_hierarchy(root_folder, output_file, indent=""):
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        if os.path.isdir(item_path):
            # Если это папка, рекурсивно вызываем функцию для нее
            build_dependency_hierarchy(item_path, output_file, indent + "\t")
        elif item.endswith('.py'):
            # Если это Python файл, анализируем его зависимости
            dependencies = find_dependencies(item_path)
            if dependencies:
                output_file.write(indent + item_path + '\n')
                for dependency in dependencies:
                    output_file.write(indent + "\t" + dependency + '\n')


# Главная функция
def main(root_folder, output_file_path):
    with open(output_file_path, 'w') as output_file:
        build_dependency_hierarchy(root_folder, output_file)


if __name__ == "__main__":
    root_folder = "../../odin_bundle/networks"  # Укажите путь к вашей корневой папке
    output_file_path = "result.txt"  # Укажите путь к результирующему файлу
    main(root_folder, output_file_path)
