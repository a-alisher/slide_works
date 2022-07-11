#1 С помощью Linux запишите в Файл все
# названия директорий из "/" - корневого каталога.
# Если у вас Windows, сделайте тоже самое)))
# Только с помощью команды dir.
# В итоге у вас на рабочем столе должен появиться файл directories.txt.
# Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.

with open('directories.txt', 'w') as f:
    f.write('''Applications
Bitrix24
Bitrix24-aiza.ozgorush@gmail.com@nkgarant.bitrix24.kz
Bitrix24-ualina25.09@gmail.com@o2development.bitrix24.kz
Desktop
Documents
Downloads
Google Drive
Library
Movies
Music
Pictures
Projects
Public
PycharmProjects
hello_world
setuptools-33.1.1.zip
''')
with open('directories.txt', 'r') as f:
    print(f.read())