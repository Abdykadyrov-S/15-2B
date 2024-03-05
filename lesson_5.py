"""
Модули - все файлы с расширением .py
"""

"""
Кастомные : Модули которые мы создаем сами ( lesson_1.py )
"""

"""
Встроенные: Модули которые встроены в язык python ( random, time, mathdatetime )
"""

# import time

# print("Код запуститься через 5 сек")

# time.sleep(5)

# print("Hello World!")

# start = time.time()

# n = 0

# while n < 7:
#     n += 1
#     # time.sleep(0.5)
#     print("Loading...")

# end = time.time()

# result = end - start
# print(result)

"""
Внешние : Модули которые нужно скачивать для исполльзования ( библиотеки или фреймворки )
"""

# pip - Пакетный менеджер python

from termcolor import cprint

print("Hello World!")

cprint("Hello World!", "red", "on_green")


"""
python -m venv venv

./venv/Scripts/activate

pip install 

pip freeze

pip uninstall

"""
