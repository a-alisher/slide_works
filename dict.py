#1
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['drinks'] = 'Coca-Cola', 'Sprite', 'Fanta'
# print(menu)

#2

# for x in range(3):
#     info = {}
#     name = input('Введите свое имя ')
#     password = input('Введите свой пароль ')  
#     info[name] = password
#     print(info)

#3
# for x in range(5):
#     spec = {}
#     name_user = input('Введите свое имя ')
#     speciality = input('Введите свою Профессию ')
#     spec[name_user] = speciality
#     print(f"Здравствуйте, {name_user}. У Вас прекрасная профессия - {speciality}")

#4
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh-barmak'] = 130
# menu['lagman'] = 135
# del menu['borsh']
# print(menu)

#5

south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
cnt = 1
country = {}
for i in set(south_american_countries):
    country[cnt] = i
    cnt += 1
print(country)
