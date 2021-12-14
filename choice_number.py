import random


def is_valid(num, over):
    return num.isdigit() and 1 <= int(num) <= over


def createRandNum(s):
    return random.randint(1, s)


print("Добро пожаловать в числовую угадайку")
print("Укажите правую границу для генерации числа:")
cn = int(input())

compNum = createRandNum(cn)

countUser = 0

while True:
    n = input()

    if not is_valid(n, cn):
        print("А может быть все-таки введем целое число от 1 до", cn, "?")
        continue
    else:
        n = int(n)

    if n < compNum:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        countUser += 1
    elif n > compNum:
        print("Ваше число больше загаданного, попробуйте еще разок")
        countUser += 1
    else:
        print("Вы угадали, поздравляем!")
        print("Количество сделанных Вами попыток:", countUser)
        print("Хотите еще раз сыграть?(y/n)")
        choice = input()
        if choice == "y":
            print("Отлично! Играем еще раз")
            compNum = createRandNum(cn)
            continue
        else:
            print("Хорошо! Тогда закругляемся")
            break


print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
