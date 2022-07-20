import random
import os
import sys
from my_module import x
print(x)


#2 lesson
list = []
count = 0
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# while True:
#     count += 1
#     list.append(random.choice(names))
#     if count >= 4:
#         break
# print(list)

# for x in range(4):
#     list.append(random.choice(names))
# print(list)

list_names = [(random.choice(names)) for x in range(4)]
print(list_names)

#3 lesson
print(os.name)
print(sys.platform)

#4 lesson
print(sys.argv)
print(sys.executable)
print(sys.path)


