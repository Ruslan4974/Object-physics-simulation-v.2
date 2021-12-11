import matplotlib.pyplot as plt
import numpy as np

def main():
    v0 = 3.0  #скорость
    eta = 0.5  #случайный угол отклонения (в радианах)
    L = 20  #размер области
    R = 1 #радиус взаимодействия
    dt = 0.2  #фаза
    Nt = 200  #количество фаз
    N = 400  #количество частиц
    plotRealTime = True

    np.random.seed(10)

    #положения частицы
    x = np.random.rand(N, 1) * L
    y = np.random.rand(N, 1) * L

    #скорость частицы
    theta = 2 * np.pi * np.random.rand(N, 1)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    #Подготовить фигуру
    fig = plt.figure(figsize=(4, 4), dpi=80)
    ax = plt.gca()

    for i in range(Nt):
        #движение
        x += vx * dt
        y += vy * dt

        #Область демонстрации (постоянное генерирование новых в окне показа)
        x = x % L
        y = y % L

        #найти средний угол соседей в диапазоне R
        mean_theta = theta
        for b in range(N):
            neighbors = (x - x[b]) ** 2 + (y - y[b]) ** 2 < R ** 2
            sx = np.sum(np.cos(theta[neighbors]))
            sy = np.sum(np.sin(theta[neighbors]))
            mean_theta[b] = np.arctan2(sy, sx)

        #Динамичность модели
        #добавление случайного отклонения
        theta = mean_theta + eta * (np.random.rand(N, 1) - 0.5)

        #изменение скорости
        vx = v0 * np.cos(theta)
        vy = v0 * np.sin(theta)

        if plotRealTime or (i == Nt - 1):
            plt.cla()
            plt.quiver(x, y, vx, vy)
            ax.set(xlim=(0, L), ylim=(0, L))
            ax.set_aspect('equal')
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            plt.pause(0.001)

    plt.show()
    return 0
if __name__ == "__main__":
    main()