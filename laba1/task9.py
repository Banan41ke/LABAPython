ip = input("Введите IP-адрес (XXX.XXX.XXX.XXX): ")
parts = ip.split(".")

if len(parts) != 4:
    print("Некорректный IP")
else:
    if (parts[0].isdigit() and 0 <= int(parts[0]) <= 255 and
        parts[1].isdigit() and 0 <= int(parts[1]) <= 255 and
        parts[2].isdigit() and 0 <= int(parts[2]) <= 255 and
        parts[3].isdigit() and 0 <= int(parts[3]) <= 255):
        print("Корректный IP")
    else:
        print("Некорректный IP")

# ip = input("введите ip:")
# a = ip.split(".")
# c=0
# if len(a)==4:
#     for i in a:
#         if 0<=int(i) and int(i)<=255:
#             c+=1
#         else:
#             break
# else:
#     print("False")
# if c==4:
#     print("true")
# else:
#     print("False")

