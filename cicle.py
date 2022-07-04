#1

# lang1 = "Rust"
# languages = ['go', 'java', 'php', 'python', 'ruby', 'javascript']

# for i in languages:
#     if i == lang1:
#         print("This Languages is in list")

# #2
# languages = ['go', 'java', 'php', 'python', 'ruby', 'javascript']
# for i in languages:
#     print(i)
#     if i == 'php':
#         break
# #3
# x = 7
# for i in range(5):
#     x = x * 7
#     print(x)

# #4

# languages = ['go', 'java', 'php', 'python', 'ruby', 'javascript']
# x = -1
# for i in languages:
#     x+=1
#     print(x, i)

# #5

# # for i in range(0, 11, 1):
# #     print(i)
# # for i in (range(8, -1, -1)):
# #     i+=1
# #     print(i)





# numbers = []
# reverse_numbers = []
# for i in range(1,11):
#     numbers.append(i)
#     reverse_numbers = numbers + numbers[-2:-11:-1]
#     print(reverse_numbers)

#6
# names = ['Максат', 'Лязат', "Данияр", "Айбек", "Атай", "Салават", "Адинай", "Жоомарт", "Алымбек",
# "Эрмек", "Дастан", "Бекмамат", "Аслан"]
# len_names = len(names)
# print(len_names)
# for i in range(0,1):
#     names_1 = names[2:13:2]
#     print(names_1)

#7
names = ['Максат', 'Лязат', "Данияр", "Айбек", "Атай", "Салават", "Адинай", "Жоомарт", "Алымбек",
"Эрмек", "Дастан", "Бекмамат", "Аслан"]
for i in range(1):
    print(names[2::2])
