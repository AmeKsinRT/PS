def a():
    while True:
        try:
            print("Какая длинна одной стороны?")
            a = float(input("Число: "))
            break
        except ValueError:
            print("Не верное значение")
            continue
    return(a)

def b():
    while True:
        try:
            print("Какая длинна второй стороны?")
            b = float(input())
            break
        except ValueError:
            print("Не верное значение")
            continue
    return(b)

def ask_user():
    while True:
        print("Площадь или периметр[S/P]")
        choise = str(input())
        if choise == "S":
            return "S"
        elif choise == "P":
            return "P"
        else:
            print("Не верное значение [S/P]")
            continue

def kv_or_pr():
    while True:
        print("Чей периметр находим?[PR/KV]")
        choise2 = input()
        if choise2 == "PR":
            return "PR"
        elif choise2 == "KV":
            return "KV"
        else:
            print("Не верное значение [PR/KV]")
            continue
while True:
    askuser = ask_user()
    a = a()
    kvorpr = kv_or_pr()
    if askuser == "S":
        if kvorpr == "KV":
            S = a**2
            print(str(S))
            break
        if kvorpr == "PR":
            b = b()
            S = b*a
            print(str(S))
            break
    elif askuser == "P":
        if kvorpr == "KV":
            P = a*4
            print(str(P))
            break
        if kvorpr == "PR":
            b = b()
            P = 2*b + 2*a
            print(str(P))
            break
