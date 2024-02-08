from get_path import result_out_path
from helpers.shared.add_more_line_in_txt_file import add_more_line_in_txt_file
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file


def make_uniq_arr_1():
    arr = get_arr_from_txt_file(file_path=result_out_path, file_name='channel_names_1')
    new_arr = []

    for elem in arr:
        if elem not in new_arr:
            new_arr.append(elem)
            add_more_line_in_txt_file(line=elem, folder_path=result_out_path, file_name='channel_names_1_uniq')

    return new_arr


def make_uniq_arr_2():
    arr = get_arr_from_txt_file(file_path=result_out_path, file_name='channel_names_2')
    new_arr = []
    links_arr = []

    for elem in arr:
        link = elem.split('***')[0]

        if link not in links_arr:
            if elem not in new_arr:
                links_arr.append(link)
                new_arr.append(elem)
                add_more_line_in_txt_file(line=elem, folder_path=result_out_path, file_name='channel_names_2_uniq')

    return new_arr


def make_uniq_arr_3():
    arr = get_arr_from_txt_file(file_path=result_out_path, file_name='channel_names_3')
    new_arr = []

    for elem in arr:
        if elem not in new_arr:
            lower = elem.lower()
            if 'bot' not in lower:
                new_arr.append(elem)
                add_more_line_in_txt_file(line=elem, folder_path=result_out_path, file_name='channel_names_3_uniq')

    return new_arr
