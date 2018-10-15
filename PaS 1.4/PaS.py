def ask_user():
    print("Площадь или периметр[S/P]")
    choise = input()
    if choise == "S":
        return "S"
    elif choise == "P":
        return "P"
    else:
        return "Ошибка"
def kv_or_pr():
    print("Чей периметр находим?[PR/KV]")
    choise2 = input()
    if choise2 == "PR":
        return "PR"
    elif choise2 == "KV":
        return "KV"
    else:
        return "Ошибка"
while 1 == 1:
    answer = ask_user()
    answer2 = kv_or_pr()
    if answer == "P":
        userInput2 = answer2
        if userInput2 == "KV":
            print("Какая длина одной стороны?")
            userInput3 = float(input())
            if userInput3 <= 0:
                print("Длина не может быть равна нулю или меньше чем ноль.")
                continue

            else:
                P = float(userInput3*4)
                print("P="+str(P))
                break

        elif userInput2 == "PR":
            print("Какая длина одной стороны?")
            userInput3 = float(input())
            print("Какая длина второй стороны?")
            userInput4 = float(input())
            if userInput3 <= 0 or userInput4 <= 0:
                print("Длина или ширина не может быть равна нулю или меньше чем ноль.")
                continue

            else:
                P = float(userInput3*2 + userInput4*2)
                print("P="+str(P))
                break

        else:
            print("Не верное значение")
            continue

    elif answer == "S":
        userInput5 = answer2
        if userInput5 == "KV":
            print("Какая длина одной стороны?")
            userInput3 = float(input())
            if userInput3 <= 0:
                print("Длина не может быть равна нулю или меньше чем ноль.")
                continue

            else:
                S = float(userInput3**2)
                print("S="+str(S))
                break

        elif userInput5 == "PR":
            print("Какая длина одной стороны?")
            userInput3 = float(input())
            print("Какая длина второй стороны?")
            userInput4 = float(input())
            if userInput3 <= 0 or userInput4 <= 0:
                print("Длина или ширина не может быть равна нулю или меньше чем ноль.")
                continue

            else:
                S = float(userInput3*userInput4)
                print("S="+str(S))
                break
        else:
            print("Не верное значение(KV-квадрат, PR-прямоугольник)")
            continue

    else:
        print("Не верное значение")
        continue
    break

