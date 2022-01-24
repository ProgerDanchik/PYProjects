import pygal
from die import Die

# Создание двух кубиков
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в список
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов
frequencies = []
labels = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    labels.append(str(value))
    frequencies.append(frequency)

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = labels
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file('dice_visual.svg')
