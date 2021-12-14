from random import randint

compNum = randint(1, 100)

print("Введите число:")
userNum = int(input())
countNum = 0

while userNum != compNum:
    if userNum > compNum:
        print("Слишком много, попробуйте еще раз")
        countNum += 1
    else:
        print("Слишком мало, попробуйте еще раз")
        countNum += 1
    print("Введите число:")
    userNum = int(input())

print("Вы угадали, поздравляем!")
print("Сделанных попыток:", countNum)
