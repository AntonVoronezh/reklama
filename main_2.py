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

    tgstat_ads_url = f'https://tgstat.ru/channel/{channel_name}/stat/ads-efficiency'
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

    form = soup.find("form", id="eff-list-form")
    ul = form.find("ul")
    li_ar = ul.find_all("li")

    for li in li_ar:
        div_row = li.find("div", class_="row")

        if div_row is not None:
            div_children = div_row.findChildren("div", recursive=False)

            first_div = div_children[0]
            link = first_div.find("a")

            href = link.get("href").replace('https://tgstat.ru/channel/','').replace('https://tgstat.com/ru/channel/','')
            add_more_line_in_txt_file(line=href, folder_path=result_out_path, file_name='channel_names_2')
            print(href)

    add_more_line_in_txt_file(line=channel_name, folder_path=result_tmp_path, file_name='done_2')
    print(Fore.RED + f'{i}, {channel_name}' + Fore.RESET, flush=True)

make_uniq_arr_2()

time_lambda(start_time=start_time)
