import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Новый блуждания строятся до тех пор, пока программа остается активной
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Назначение размера области просмотра
    plt.figure(figsize=(16, 9))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Выделение первой и последней точки
    plt.scatter(0, 0, c='green', edgecolors='none', s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)

    # Удаление осей
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
