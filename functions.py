# def send_email(name, time, *args, **kwargs):
#     text = "Privet. Tebe zavtra na rabotu"
#     print(f'{name}, {text} к {time}')
#     print()
#
# send_email('Mirbek', 8)

l = [0, 1, 2, 3]
def reverse_list(list):
    l1 = l[1::-1]
    l2 = l[:-3:-1]
    print(l1 + l2)


reverse_list(l)