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

# at = 10
# i = 15
# wo = 20
# try:
#     for e in range(-at, at):
#         print(wo / e)
#         if at > 5:
#             print(int("at" > '5'))
# except IndentationError:
#     print("IndentationError")
# except NameError:
#     print("NameError")
# except SyntaxError:
#     print("syntaxerror")
# except ZeroDivisionError:
#     print("ZERO Error")

# 3 exercise
# lst = []
# try:
#     for i in range(10):
#         lst.append(i)
#         a = list(reversed(lst))
#         sls_obj = slice('0','8')
#         print([sls_obj])
# except IndentationError:
#     print("IndentationError")
# except NameError:
#     print("NameError")
# except SyntaxError:
#     print("syntaxerror")
# except ZeroDivisionError:
#     print("ZERO Error")


# Перенесите к себе код #3 и
# исправьте все ошибки, сделайте так чтобы код работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.4 exercise:

a = (0)
b = 1
numbers = []
try:
    while b > a:
        numbers += b
        b += 1
except NameError:
    print("NameError")
except SyntaxError:
    print("SyntaxError")
except ValueError:
    print("ValueError")
except IndentationError:
    print("IndentationError")
except TypeError:
    print("TypeError")
