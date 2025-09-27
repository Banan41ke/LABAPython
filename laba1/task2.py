# s = input("Введите строку на англ: ")
# s1 = "eyuioa"
# s2=""
# for i in range(len(s)):
#     if s[i] in s1:
#         continue
#     else:
#         s2+=s[i]
# print(s2)

text = input("Введите строку на англ: ")

vowels = 'aeiouAEIOU'
translation_table = str.maketrans('', '', vowels)

result = text.translate(translation_table)
print(result)