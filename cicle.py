#1
from ast import While
from operator import index, indexOf


lang1 = "Rust"
languages = ['go', 'java', 'php', 'python', 'ruby', 'javascript']

for i in languages:
    if i == lang1:
        print("This Languages is in list")

#2
languages = ['go', 'java', 'php', 'python', 'ruby', 'javascript']
for i in languages:
    print(i)
    if i == 'php':
        break
#3
x = 7
for i in range(5):
    x = x * 7
    print(x)

#4

languages = ['go', 'java', 'php', 'python', 'ruby', 'javascript']
x = -1
for i in languages:
    x+=1
    print(x, i)

#5

for i in range(0, 11, 1):
    print(i)
for i in (range(8, -1, -1)):
    i+=1
    print(i)