from datetime import datetime
import math


from colorama import Fore


def time_lambda(start_time):
    lambda_ = datetime.now() - start_time
    lambda_sec = lambda_.total_seconds()
    lambda_sec_out = f'{math.ceil(lambda_sec)} секунд' if lambda_sec < 60 else f'{math.ceil(lambda_sec / 60)} минут'

    print(Fore.BLUE + f'\n время выполнения - {lambda_sec_out}' + Fore.RESET)
