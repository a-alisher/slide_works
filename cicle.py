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
