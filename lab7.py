# Чамкина Александра R3135 ISU-334638
# 8 вариант:	data2.csv	4	x∈(-3п;3п); y=cos(x); z=x/sin(x)

import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
import random

# Cравнение времени выполнения
#-----------------------------------------------------------------------------------------------------------------------

a = []                                     # Создание массивов в 1 миллион элементов,
b = []                                     # заполненных случайными значениями от 1 до миллиона
for i in range(1000000):
    a.append(random.randint(1, 1000000))
    b.append(random.randint(1, 1000000))
ac = np.array(a)
bc = np.array(b)

comp = []
start1 = perf_counter()                    # Вычисление времени перемножения стандартных списков
for i in range(1000000):
    comp.append(ac[i]*bc[i])
end1 = perf_counter() - start1

start2 = perf_counter()                    # Вычисление времени перемножения массивов NumPy
np.multiply(ac, bc)
end2 = perf_counter() - start2

print(f'Время поэлементного перемножения стандартных списков - {end1}\n'
      f'Время перемножения массивов NumPy - {end2}\n'
      f'Перемножение массивов NumPy было проведено на {end1 - end2} быстрее')

# Построение гистограммы
#-----------------------------------------------------------------------------------------------------------------------

data = np.genfromtxt('data2.csv', delimiter=',')  # Получение данных из файла
hist = np.array(data[:, 3])[1:]

plt.hist(hist, 30)                         # Построение первой нормальной гистограммы
plt.title('Гистограмма')
plt.xlabel('ph')
plt.ylabel('Частота')
plt.grid()
plt.show()

plt.hist(hist, 30, density=True)           # Построение второй нормализованной гистограммы
plt.title('Нормализованная гистограмма')
plt.xlabel('ph')
plt.ylabel('Частота')
plt.grid()
plt.show()

print(f'Cреднеквадратичное отклонение - {np.std(hist)}')  # Выод среднеквадратичного отклонения

# Построение трехмерного графика x∈(-3п;3п); y=cos(x); z=x/sin(x)
#-----------------------------------------------------------------------------------------------------------------------

x = np.linspace(-3*np.pi, 3*np.pi, 50)     # Составление функции
y = np.cos(x)
z = x/np.sin(x)

fig = plt.figure()                         # Построение трехмерного графика
ax = fig.add_subplot(projection='3d')
plt.title('y=cos(x)   z=x/sin(x)\n x∈(-3п;3п)')
ax.plot(x, y, z)
plt.show()