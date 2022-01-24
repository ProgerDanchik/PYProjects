import pygal
from die import Die

# Создание кубика D6
die = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"

labels = []
for i in range(1, die.num_sides + 1):
    labels.append(str(i))

hist.x_labels = labels
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)
