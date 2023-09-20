import os
import re

# Путь к корневой папке с вашей файловой системой
root_folder = '../../odin_bundle/networks'

# Список префиксов
prefixes = ['Common', 'Gen3', 'Model3', 'ModelY', 'Tutorials']

# Функция для поиска слов, начинающихся с заданных префиксов
def find_words_with_prefixes(file_path, prefixes):
    found_words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        for prefix in prefixes:
            # Используем регулярное выражение для поиска слов с заданным префиксом
            matches = re.findall(rf'\b{prefix}\S*\b', text)

            found_words.extend(matches)
    return found_words

# Функция для обхода файловой системы и записи результатов в результирующий файл
def search_files_and_write_results(root_folder, prefixes, output_file):
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for foldername, subfolders, filenames in os.walk(root_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                found_words = find_words_with_prefixes(file_path, prefixes)
                if found_words:
                    # Записываем имя файла в результирующий файл
                    result_file.write(file_path[6:] + '/' + filename + '\n')

                    # Записываем найденные слова с отступами
                    for word in found_words:
                        result_file.write('    ' + word + '\n')

                    # Добавляем пустую строку между файлами
                    result_file.write('\n')

# Имя результирующего файла
output_file = 'resultv4.txt'

# Вызываем функцию для поиска и записи результатов
search_files_and_write_results(root_folder, prefixes, output_file)

print('Поиск завершен. Результаты записаны в', output_file)
