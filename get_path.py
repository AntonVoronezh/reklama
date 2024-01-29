import os
import shutil

result_folder_name = '1results'
tmp_folder_name = 'tmp'
out_folder_name = 'out'


realpath = os.path.dirname(os.path.realpath(__file__))
result_path = os.path.join(realpath, result_folder_name)
result_tmp_path = os.path.join(result_path, tmp_folder_name)
result_out_path = os.path.join(result_path, out_folder_name)


def make_current_dir():
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
    if not os.path.isdir(result_tmp_path):
        os.mkdir(result_tmp_path)
    if not os.path.isdir(result_out_path):
        os.mkdir(result_out_path)


def clear_tmp_dir():
    if os.path.isdir(result_tmp_path):
        shutil.rmtree(result_tmp_path)
        os.mkdir(result_tmp_path)
    if os.path.isdir(result_out_path):
        shutil.rmtree(result_out_path)
        os.mkdir(result_out_path)







