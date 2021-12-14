import random


def generate_password(length, char, count_pass):
    passwords = []

    for i in range(count_pass):
        password = ''
        for j in range(length):
            password += random.choice(char)
        passwords.append(password)
    return passwords


DIGITS = "0123456789"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PUNCTUATION = "!#$%&*+-=?@^_"
chars = ''

print("Введите количество паролей для генерации:")
countPass = int(input())

print("Длина одного пароля: ")
lenPass = int(input())

print("Включать ли цифры?:(y/n)")
numPass = input()

print("Включать ли прописные буквы?:(y/n)")
lowPass = input()

print("Включать ли строчные буквы?:(y/n)")
upPass = input()

print("Включать ли символы?:(y/n)")
symPass = input()

print("Исключать ли неоднозначные символы il1Lo0O?:(y/n)")
crashPass = input()

if numPass == "y":
    chars += DIGITS
if upPass == "y":
    chars += UPPERCASE_LETTERS
if lowPass == "y":
    chars += LOWERCASE_LETTERS
if symPass == "y":
    chars += symPass
if crashPass == "y":
    for i in "il1Lo0O":
        chars.replace(i, '')

print(generate_password(lenPass, chars, countPass))
