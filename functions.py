# def send_email(name, time, *args, **kwargs):
#     text = "Privet. Tebe zavtra na rabotu"
#     print(f'{name}, {text} к {time}')
#     print()
#
# send_email('Mirbek', 8)

# l = [0, 1, 2, 3]
#
#
# def reverse_list(list):
#     # length = len(list)
#     # middle_index = length % 2
#     # # first_half = list[:middle_index:-1]
#     # # second_half = list[middle_index:-1]
#     l1 = l[1::-1]
#     l2 = l[:-3:-1]
#     print(l1 + l2)
#
#
# reverse_list(l)





values = ("TURUSBEKOVA 109/1", 10, 1005, ["TABLES", "CHAIRS"], 23.00)

def my_func(val):
  try:
    set(val)
  except:
    return False
  else:
    return True

my_list = list(map(my_func, values))
print(my_list)

if all(my_list):
  print("Мы можем конвертировать")
else:
  print("Мы не можем")


dict = {'son': "njnjn"}
dict_2 = {'dad': 'njnjnjn'}
def sum_func(dict_1, dict_2):
    dict_1.update(dict_2)
    print(dict_1)

sum_func(dict, dict_2)