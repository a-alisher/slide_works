def main_func(func):
    def younger_func():
        x = func()
        print('Я старшая функция!')
        return x
    return younger_func


@main_func
def dec_func():
    return 'Я младшая функция!'

print(dec_func())