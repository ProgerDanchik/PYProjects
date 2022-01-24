from die import Die
import pygal


# Создание трех кубиков D6
d6_1 = Die()
d6_2 = Die()
d6_3 = Die()

# Моделирование серии бросков и сохранение их результата в список
results = []
for roll_num in range(5000):
    result = d6_1.roll() + d6_2.roll() + d6_3.roll()
    results.append(result)

# Анализ результатов
frequencies = []
labels = []
max_result = d6_1.num_sides + d6_2.num_sides + d6_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    labels.append(str(value))
    frequencies.append(frequency)

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling a D6(3) 5000 times"
hist.x_labels = labels
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('d6_3_visual.svg')
