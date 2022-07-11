try:
    k = "bla-bla" + 27
    print("Вы ввели: ", k)
except TypeError as te:
    print("Type_Error")

try:
    k = "blabla"
    print(k[10])
except IndexError as ie:
    print("Index Error")
try:
    a = 1
    k = a + b
    print(k)
except NameError:
    print("NameError")
