s = input("Введите текст разделяя слова пробелами: ")
s = s.lower()
a = s.split()
a1 = set(a)
l = {}

for i in a1:
    l[i] = a.count(i)
print(l)