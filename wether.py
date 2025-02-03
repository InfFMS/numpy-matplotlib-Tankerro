# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import random
import matplotlib.pyplot as plt
import numpy as np
import math

fig, axs = plt.subplots(1, 2, figsize=(10,4))

Days_temp = []
T=-60
for i in range(0,365):
    Days_temp.append(19.5*math.sin((i + T)/360*2*math.pi) + random.randint(-3, 3)+12.5)

Days_temp = np.array(Days_temp)
Average = np.average(Days_temp)

for i in range(0,365):
    Days_temp[i] = int(Days_temp[i])


Days_temp_bp = list(set(Days_temp))
Temp_counts = []
for i in range(0, len(Days_temp_bp)):
    Temp_counts.append(list(Days_temp).count(Days_temp_bp[i]))

colors = ['red' if val >= 5 else 'blue' for val in Days_temp]

axs[0].plot(np.arange(1, 366), Days_temp)
axs[0].bar(np.arange(1, 366), Days_temp, color=colors)
axs[0].set_title("Погода")
axs[0].set_xlabel("День")
axs[0].set_ylabel("Температура")

axs[1].bar(Days_temp_bp, Temp_counts, color="green")
axs[1].set_title("Дни по температуре")
axs[1].set_xlabel("Температура")
axs[1].set_ylabel("Кол-во дней")
plt.show()

