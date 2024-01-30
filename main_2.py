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
from helpers.shared.make_uniq_arr import make_uniq_arr_2
from helpers.shared.time_lambda import time_lambda

service = Service(executable_path="C:\webdrivers\geckodriver.exe",
                  service_args=['--marionette-port', '2828', '--connect-existing'])
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

make_current_dir()

start_time = datetime.now()
channel_names = get_arr_from_txt_file(file_path=result_out_path, file_name='channel_names')
done_channel_names = get_arr_from_txt_file(file_path=result_tmp_path, file_name='done_2')

print(Fore.RED + f'START' + Fore.RESET)


for i, channel_name in enumerate(channel_names):
    if channel_name in done_channel_names:
        print(Fore.YELLOW + f'Данные {channel_name} уже есть' + Fore.RESET)
        continue

    tgstat_ads_url = f'https://tgstat.ru/quotes/{channel_name}/list/m-2401'
    driver.get(tgstat_ads_url)

    while True:
        time.sleep(5)
        try:
            element_button_more = driver.find_element(By.XPATH, "//*[contains(text(), 'Показать больше')]")
            if not element_button_more:
                break
            else:
                print('-')
                element_button_more.location_once_scrolled_into_view
                element_button_more.click()
        except:
            break


    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    form = soup.find("form", id="quotes-list-form")

    if form:
        li_ar = form.find_all("li")

        if li_ar:

            for li in li_ar:
                a_arr = li.find_all("a")

                if a_arr:
                    a_first = a_arr[0]
                    a_first_href = a_first.get("href")
                    a_first_href_split = a_first_href.split('/')
                    link = a_first_href_split[-2]
                    print(link)
                    add_more_line_in_txt_file(line=link, folder_path=result_out_path, file_name='channel_names_2')

    add_more_line_in_txt_file(line=channel_name, folder_path=result_tmp_path, file_name='done_2')
    print(Fore.RED + f'{i}, {channel_name}' + Fore.RESET, flush=True)

make_uniq_arr_2()

time_lambda(start_time=start_time)
