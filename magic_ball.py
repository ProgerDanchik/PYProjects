import random


def choice():
    compNum = random.randint(0, len(answers) - 1)
    return answers[compNum]


answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input()

print("Привет,", name)

while True:
    print("Задай мне вопрос")
    q = input()
    print(choice())

    print("Хочешь продолжить? (y/n)")
    a = input()
    if a == "y":
        print("Продолжаем...")
    elif a == "n":
        print("Возвращайся если возникнут вопросы!")
        break
