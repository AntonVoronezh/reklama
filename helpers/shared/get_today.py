from datetime import datetime


def get_today():
    current_date = datetime.today()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    return f'{day}-{month}-{year}'
