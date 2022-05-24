a = int(input("Введите номер дня недели "))
if a < 6 and a > 0:
    print('нет')
elif a > 5 and a < 8:
    print('да')
else:
    print("нет такого дня недели")