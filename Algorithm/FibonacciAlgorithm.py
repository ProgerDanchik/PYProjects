import time # Библиотека для вычисления времени работы функций
from matplotlib import pyplot as plt # Библиотека для работы с математическими графиками


# Функция поиска числа Фибоначчи через цикл обработки двух предыдущих чисел
def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(int(n) - 1):
        f0, f1 = f1, f0 + f1
    return f1


# Функция поиска числа Фибоначчи через рекурсию функции
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# Функция вычисления времени работы для реализации поиска числа Фибоначчи
def timed(f, *args, n_itter=100):
    acc = float("inf")
    for i in range(n_itter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


# Функция построения графика
def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)


x = int(input())

print(fib3(x))
print(timed(fib3, x))
compare([fib3], list(range(x)))
plt.show()
