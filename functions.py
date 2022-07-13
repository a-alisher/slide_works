# def send_email(name, time, *args, **kwargs):
#     text = "Privet. Tebe zavtra na rabotu"
#     print(f'{name}, {text} к {time}')
#     print()
#
# send_email('Mirbek', 8)

l = [0, 1, 2, 3]


def reverse_list(list):
    # length = len(list)
    # middle_index = length % 2
    # # first_half = list[middle_index:-1]
    # # second_half = list[middle_index:-1]
    l1 = l[1::-1]
    l2 = l[:-3:-1]
    print(l1 + l2)


reverse_list(l)