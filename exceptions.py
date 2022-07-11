# try:
#     k = "bla-bla" + 27
#     print("Вы ввели: ", k)
# except TypeError as te:
#     print("Type_Error")
#
# try:
#     k = "blabla"
#     print(k[10])
# except IndexError as ie:
#     print("Index Error")
# try:
#     a = 1
#     k = a + b
#     print(k)
# except NameError:
#     print("NameError")

# 2 exercise

at = 10
i = 15
wo = 20
try:
    for e in range(-at, at):
        print(wo / e)
        if at > 5:
            print(int("at" > '5'))
except IndentationError:
    print("IndentationError")
except NameError:
    print("NameError")
except SyntaxError:
    print("syntaxerror")
except ZeroDivisionError:
    print("ZERO Error")
