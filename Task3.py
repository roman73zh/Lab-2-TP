import json
import math
import time
import csv
import numpy as np
import os.path
import sys

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

dirpath = sys.argv[1]
for i in os.listdir(dirpath):
    if os.path.isfile(os.path.join(dirpath, i)):
        print(str(i) + ' имеет размер ' + str(convert_size(os.path.getsize(os.path.join(dirpath, i)))))
csvName = sys.argv[2]
lst = []
with open(dirpath+csvName, encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';')
    for i in reader:
        try:
            i[0] = int(i[0])
        except Exception:
            print("Ошибка приведения типа номера")
            i[0] = 0
        try:
            i[1] = time.strptime(i[1], "%d.%m.%Y-%H.%M")
        except Exception:
            print("Ошибка приведения типа даты")
            i[1] = time.strptime("01.01.1970-00.00", "%d.%m.%Y-%H.%M")
        try:
            i[2] = i[2] in ['true', '1', 't', 'y', 'yes', 'True', 'да', 'Да', 'yeah', '+']
        except Exception:
            print("Ошибка приведения типа логической переменной")
            i[2] = None
        lst.append(i)
data = {}
print("\nСортировка по номеру")
lst = sorted(lst, key=lambda entry: entry[0])
data["By_number"] = lst
for i in lst:
    print(f'Запись {i[0]}: {i[3]} {"зашел" if i[2] else "вышел"} {time.strftime("%d.%m.%Y в %H:%M", i[1])}')
print("\nСортировка по полу")
data["By_sex"] = lst
lst = sorted(lst, key=lambda entry: entry[3])
for i in lst:
    print(f'Запись {i[0]}: {i[3]} {"зашел" if i[2] else "вышел"} {time.strftime("%d.%m.%Y в %H:%M", i[1])}')
print("\nВывод зашедших")
data["Only_entered"] = lst
lst = sorted(lst, key=lambda entry: entry[3])
for i in [i for i in lst if i[2] == True]:
    print(f'Запись {i[0]}: {i[3]} {"зашел" if i[2] else "вышел"} {time.strftime("%d.%m.%Y в %H:%M", i[1])}')
with open(dirpath+"json/data.json", encoding='utf8', mode='w') as f:
    json.dump(data, f)
os.replace(dirpath+"json/data.json", dirpath+"json/.."+"/data.json")
os.remove(dirpath+csvName)