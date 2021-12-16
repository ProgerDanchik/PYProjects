print('Программа шифровки / дешифровки текста по методу Цезаря')
k = int(input('Введите шаг сдвига для шифровки ( >0 ) или дешифровки ( <0 ) '))
en_alph = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
ru_alph = [chr(i) for i in range(1040, 1104)]


def cezar(text):
    if txt[0] in en_alph:
        alphabet = en_alph
        len_alph = 26
    else:
        alphabet = ru_alph
        len_alph = 32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                print(alphabet[(alphabet.index(text[i]) + k) % len_alph], end='')
            else:
                print(alphabet[(alphabet.index(text[i]) + k) % len_alph + len_alph], end='')
        else:
            print(text[i], end='')


txt = input('Введите текст: ')
cezar(txt)
