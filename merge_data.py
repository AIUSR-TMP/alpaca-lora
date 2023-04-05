import json
import os


def load_json_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except Exception:
        with open(file_name, 'r', encoding='utf-8') as file:
            ds = []
            data = file.readlines()
            for text in data:
                ds.append(eval(text))
    return data


def convert_to_target_format(data):
    result = []

    for entry in data:
        result.append(entry)

    return result


input_folder = './Data/Mixed/'
files = os.listdir(input_folder)

merged_data = []

for file in files:
    if file.endswith('.json'):
        file_path = os.path.join(input_folder, file)
        print(file_path)
        data = load_json_from_file(file_path)
        merged_data.extend(data)

converted_data = convert_to_target_format(merged_data)

with open(os.path.join(input_folder, 'mixed.json'), "w", encoding='utf-8') as file:
    file.write(json.dumps(converted_data, ensure_ascii=False))
