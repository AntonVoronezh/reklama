import os


def get_arr_from_txt_file(file_path, file_name):
    file_path_def = os.path.join(file_path, f'{file_name}.txt')
    links_arr = []

    if os.path.exists(file_path_def):
        with open(file_path_def, encoding='utf-8') as file:
            for el in file:
                links_arr.append(el.strip())

    return links_arr