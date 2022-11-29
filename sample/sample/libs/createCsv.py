import csv
from datetime import datetime
import os


def create_date_path(date):
    _date= date
    if type(date) == str:
        _date = __convert_str_to_iso_date(date)
    datePath = _date.strftime('%Y\\%m')
    return datePath

def __convert_str_to_iso_date(strDate):
    isoDate = datetime.fromisoformat(strDate)
    return  isoDate

def create_csv(chatList, path):
    os.makedirs(path, exist_ok=True)
    os.chmod(path, mode=0x777)
    try:
        with open(path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames = chatList.keys())
            writer.writeheader()
            writer.writerow(chatList)
    except Exception as e:
        print(e)
        # os.rmdir(path)
    return