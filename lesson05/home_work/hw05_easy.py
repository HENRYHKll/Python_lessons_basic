# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil
print('Создаю 9 папок, понеслась')
for i in range(1, 10):
    try:
        os.mkdir('dir_' + str(i))
        print('Папка dir_' + str(i) + " готова")
    except FileExistsError:
        print('Такая директория (dir_' + str(i) + ") уже существует")
# удаляем дирректории 1-9
print('да что ты  будешь делать, теперь удаляем?')
del_d = input('Точно удалить? да/нет - ')
if del_d  == 'да':
    for i in range(1, 10):
        os.rmdir('dir_' + str(i))
        print("dir_" + str(i) + " больше нет(")
else:
    print("НУ и правильно ;)")
    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
print('Список фалов и папок в текущей директории')
for i in os.listdir():

    print(i)
    
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import shutil
os.path.realpath(__file__)
name = str(__file__)
print('Оригинальный файл : ', name)
n_f_name = (name + '.copy')
new_f = shutil.copy(__file__, n_f_name)
print('реплика : ', new_f) 
