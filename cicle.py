#1
from ast import While


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