word1 = input("Введите первое слово ")
word2 = input("Введите второе слово ")

c=0

if len(word1) == len(word2):
    for i in word1:
        if word1.count(i) == word2.count(i):
            c+=1
        else:
            print("False")
            break
else:
    print("False")

if c == len(word1):
    print("True")