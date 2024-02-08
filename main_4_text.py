import time
from datetime import datetime
from random import choice
import random

import pyrogram as pyrogram
from bs4 import BeautifulSoup
from colorama import Fore
import requests
import fake_useragent
from get_path import result_out_path
from helpers.shared.add_more_line_in_txt_file import add_more_line_in_txt_file

from helpers.shared.get_arr_from_txt_file import get_arr_from_txt_file

app = pyrogram.Client("my_account")

start_time = datetime.now()
channel_names = get_arr_from_txt_file(file_path=result_out_path, file_name='channel_names_3_uniq')

print(Fore.RED + f'START' + Fore.RESET)

ua = fake_useragent.UserAgent()
fake_ua = {'user-agent': ua.random}

limit = 25

count = 0

for i, elem in enumerate(channel_names):
    if count >= limit:
        break


    slip_arr = list(range(3, 6))
    elem_split = elem.split('***')

    kto_link = elem_split[0].replace("@", "")
    kto_data = elem_split[1]
    kto_title = elem_split[2]

    gde_link = elem_split[3].replace("@", "")
    gde_title = elem_split[4]

    kto_person = elem_split[5].replace("@", "")

    kto_person_sended = get_arr_from_txt_file(file_path=result_out_path, file_name='kto_person_sended')
    if kto_person in kto_person_sended:
        print(Fore.YELLOW + f'@{kto_person} уже отправляли' + Fore.RESET)
        continue


    response = requests.get(url=f'https://t.me/{kto_person}', headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find("div", class_="tgme_page_title")
    # print(title.text)

    if title is None:
        continue

    name = title.text.strip().split(' ')[0]

    a_1 = [f'{name}, привет!', f'Привет {name}!', f'{name}, добрый день!', f'Добрый день {name}!']
    a_2 = ['Обратил внимание', 'Заметил', 'Увидел', 'Подсмотрел', 'Подсказали']
    a_3 = ['интересный', 'увлекательный', 'занимательный', 'заслуживающий внимания', 'достойный внимания']
    a_4 = ['недавно', 'не так давно', 'на днях', 'несколько дней назад', f'{kto_data}']
    a_4_ = [f'«{kto_title}»', f'«{kto_link}»', f'"{kto_title}"', f'"{kto_link}"', f'``{kto_title}``']
    a_5_ = ['рекламировался', 'размещал рекламу', 'продвигался', 'крутил рекламу']
    a_5 = ['канале', 'ресурсе', 'источнике', f'канале "{gde_title}"', f'канале "{gde_link}"']
    a_6 = ['теме', 'тематике', 'направлению']

    a_7 = ['зашло', 'понравилось', 'зацепило']
    a_8 = ['устроил приток', 'понравилось количество', 'подошло количество']
    a_9 = ['предлагаю', 'прошу', 'рекомендую', 'советую']
    a_10 = ['аналогичные', 'похожие', 'такие же', 'подобные']
    a_11 = ['каналы', 'ресурсы', 'источники']
    a_12 = ['рекламы', 'размещения рекламы', 'размещения', 'рекламироавния']
    a_13 = ['✈️', '🛩️', '🛫', '🛬', '🚠', '🚁', '🚢', '🛳️', '🚗', ]


    a_rek = ['Тревел Фишки (trevel_fishki)', 'ЗА БУГРОМ (za_bugromm)', 'Погнали в отпуск (pognali_v_otpusk)']
    random.shuffle(a_rek)

    text = f'''{choice(a_1)} 🖐️

    {choice(a_2)}, что ваш {choice(a_3)} канал {choice(a_4_)} {choice(a_4)} {choice(a_5_)} на {choice(a_5)} по {choice(a_6)} путешествия.
    
    Eсли вам {choice(a_7)} и {choice(a_8)} подписчиков, {choice(a_9)} рассмотреть  {choice(a_10)}  {choice(a_11)} для {choice(a_12)}:

    - {choice(a_13)} {a_rek[0]}
    - {choice(a_13)} {a_rek[1]}
    - {choice(a_13)} {a_rek[2]}
    '''

    with app:
        try:
            app.send_message(f'@{kto_person}', text)
            add_more_line_in_txt_file(line=kto_person, folder_path=result_out_path, file_name='kto_person_sended')
        except:
            print('Ошибка отправки')
            pass

    print(f'{i}, @{kto_person}', flush=True)

    count = count + 1

    rand_sleep = choice(slip_arr) * 60
    time.sleep(rand_sleep)

    # print(text, flush=True)
    # print(f'{i}-------------', flush=True)
