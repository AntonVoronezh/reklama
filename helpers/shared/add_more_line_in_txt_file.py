import os


def add_more_line_in_txt_file(line, folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)

    with open(f'{file_path}.txt', 'a+', encoding='utf-8') as f:
        f.write(f"{line}\n")
        f.close()