import time
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from get_path import make_current_dir, result_path, result_out_path
from helpers.shared.add_more_line_in_txt_file import add_more_line_in_txt_file
from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file
from helpers.shared.time_lambda import time_lambda

service = Service(executable_path="C:\webdrivers\geckodriver.exe",
                  service_args=['--marionette-port', '2828', '--connect-existing'])
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

make_current_dir()

start_time = datetime.now()
words = get_arr_from_txt_file(file_path=result_path, file_name='tema')

print(Fore.RED + f'START' + Fore.RESET)

tgstat_search_url = 'https://tgstat.ru/channels/search'


for i, word in enumerate(words):
    driver.get(tgstat_search_url)

    # тема
    element_input = driver.find_element(By.XPATH, "//input[@placeholder='Тематика канала']")
    element_input.send_keys(word)
    time.sleep(1)

    element_ul = driver.find_element(By.CSS_SELECTOR, "ul#select2-categories-results")
    element_li = element_ul.find_element(By.TAG_NAME, "LI")
    element_li.click()


    # подписчиков от
    element_input = driver.find_element(By.XPATH, "//input[@id='participantscountfrom']")
    element_input.send_keys(f"2000")
    # подписчиков до
    element_input = driver.find_element(By.XPATH, "//input[@id='participantscountto']")
    element_input.send_keys(f"10000000")



    element_button = driver.find_element(By.XPATH, "//button[@id='search-form-submit-btn']")
    element_button.location_once_scrolled_into_view
    element_button.click()

    time.sleep(2)

    while True:
        time.sleep(2)
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

    links = soup.find_all("a", class_="text-body")

    for link in links:
        href = link.get("href").replace('https://tgstat.ru/channel/','').replace('https://tgstat.ru/chat/','')
        add_more_line_in_txt_file(line=href, folder_path=result_out_path, file_name='channel_names_1')
        print(href)

    print(Fore.RED + f'{i}, {word}' + Fore.RESET, flush=True)

time_lambda(start_time=start_time)
