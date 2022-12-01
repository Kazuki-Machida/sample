import csv
from datetime import datetime
import os


def create_date_path(date):
    _date = date
    if type(date) == str:
        _date = __convert_str_to_iso_date(date)
    datePath = _date.strftime('%Y\\%m')
    return datePath

def __convert_str_to_iso_date(strDate):
    isoDate = datetime.fromisoformat(strDate)
    return  isoDate

def create_csv(elemList, path, title):
    os.makedirs(path, exist_ok=True)
    os.chmod(path, mode=0o777)
    csvName = path + title + ".csv"
    __fieldnames = list(elemList[0].keys())
    print(__fieldnames)
    try:
        with open(csvName, 'w') as f:
            writer = csv.DictWriter(f, fieldnames = __fieldnames)
            writer.writeheader()
            for index in range(len(elemList)):
                writer.writerow(elemList[index])
    except Exception as e:
        print(e)
        # os.rmdir(path)
    return
