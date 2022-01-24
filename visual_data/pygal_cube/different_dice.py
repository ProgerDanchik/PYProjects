from die import Die
import pygal

# Создание кубиков D6 и D10
die_1 = Die()
die_2 = Die(13)

# Моделирование серии бросков и сохранение их результата в список
results = []
for roll_num in range(50000):
    result = die_1.roll() * die_2.roll()
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


hist.title = "Results if rolling a D6 and a D10 50,000 times"
hist.x_labels = labels
hist._x_title = "Result"
hist._y_title = "Frequency of Result"
hist.add("D6 + D10", frequencies)
hist.render_to_file('dice_visual.svg')
