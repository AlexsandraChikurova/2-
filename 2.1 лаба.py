def parol():
    a = input("введите пароль: ")
    b = input("введите пароль ещё раз: ")
    if len(a) < 5 or len(b) < 5:
        print("проверьте длину пароля")
    else:
        if a.isdigit() and b.isdigit():
            if a == b:
                print("пароли совпадают")
            else:
                print("пароли не совпадают")
        else:
            print("пароль должен состоять только из цифр")
def poezd():
    a = int(input("mecto "))
    if a <= 0 or a > 54:
        print("Неверный номер места")
    elif a % 8 == 1 or a % 8 == 4:
        print("Нижнее место")
    elif a % 8 == 7 or a % 8 == 2 or a % 8 == 5 or a % 8 == 8:
        print("Боковое место")
    elif a % 8 == 3 or a % 8 == 6:
        print("Верхнее место")
    else:
        print("Неверный номер места")
def year():
    g = int(input("введите год "))
    if g % 4 == 0:
        if g % 100 == 0:
            if g % 400 == 0:
                print(f"Год {g} - високосный")
            else:
                print("Это год не високосный")
        else:
            print(f"Год {g} - високосный")
    else:
        print("Это год не високосный")
def color():
    color=input("введите цвет: ")
    color2=input("введите цвет: ")
    if ((color == "красный" and color2== "синий") or (color == "синий" and color2 == "красный")):
        print("фиолетовый")
    elif ((color == "красный" and color2== "желтый") or (color == "желтый" and color2 == "красный")):
        print("оранжевый")
    elif ((color == "синий" and color2 == "желтый") or (color == "желтый" and color2 == "синий")):
        print("зеленый")
    else:
        print("проверь цвета")
while True:
    choice=input("\n1-проверить пароль \n2-выбор места в плацкарде \n3-определения года \n4-получения цвета \n")
    match choice:
        case "1":
            parol()
        case "2":
            poezd()
        case "3":
            year()
        case "4":
            color()
    if choice=="0":
        break