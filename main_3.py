import time
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from get_path import make_current_dir, result_out_path, result_tmp_path
from helpers.shared.add_more_line_in_txt_file import add_more_line_in_txt_file
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file
from helpers.shared.make_uniq_arr import make_uniq_arr_3
from helpers.shared.time_lambda import time_lambda

service = Service(executable_path="C:\webdrivers\geckodriver.exe",
                  service_args=['--marionette-port', '2828', '--connect-existing'])
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

make_current_dir()

start_time = datetime.now()
channel_names = get_arr_from_txt_file(file_path=result_out_path, file_name='channel_names_2_uniq')
done_channel_names = get_arr_from_txt_file(file_path=result_tmp_path, file_name='done_3')

print(Fore.RED + f'START' + Fore.RESET)


for i, channel_name in enumerate(channel_names):
    if channel_name in done_channel_names:
        print(Fore.YELLOW + f'Данные {channel_name} уже есть' + Fore.RESET)
        continue

    tgstat_page_url = f'https://tgstat.ru/channel/{channel_name}'
    driver.get(tgstat_page_url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    div = soup.find("div",class_="col-12 col-sm-7 col-md-8 col-lg-6")

    if div:

        links = div.find_all('a')

        for link in links:
            href = link.get("href")

            if 'https://t.me/' in href:
                href_replaced = link.get("href").replace('https://t.me/', '')
                href_replaced_with = f'@{href_replaced}'

                if channel_name not in href_replaced:
                    if href_replaced not in channel_name:
                        print(href_replaced_with)
                        add_more_line_in_txt_file(line=href_replaced_with, folder_path=result_out_path, file_name='channel_names_3')





    time.sleep(1)
    add_more_line_in_txt_file(line=channel_name, folder_path=result_tmp_path, file_name='done_3')
    print(Fore.RED + f'{i}, {channel_name}' + Fore.RESET, flush=True)

make_uniq_arr_3()

time_lambda(start_time=start_time)
