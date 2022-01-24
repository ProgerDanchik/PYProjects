from die import Die
import pygal


# Создание объектов кубиков
d8_1 = Die(8)
d8_2 = Die(8)

# Моделирование бросков кубика и сохранение результата в список
results = []
for roll in range(1000):
    result = d8_1.roll() + d8_2.roll()
    results.append(result)

# Анализ результатов
frequencies = []
labels = []
max_result = d8_1.num_sides + d8_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    labels.append(str(value))
    frequencies.append(frequency)

# Визуализация данных
hist = pygal.Bar()

hist.title = "Results of rolling a D8"
hist.x_labels = labels
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add("D8 + D8", frequencies)
hist.render_to_file('d8_visual.svg')
