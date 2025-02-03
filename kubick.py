# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.

import matplotlib.pyplot as plt
import numpy as np

values = np.random.randint(1, 7, 1000)

values_unsorted = values

max_len=1
Len = 1
for j in range(1, len(values_unsorted)):
    if values_unsorted[j] == values_unsorted[j-1]:
        Len += 1
    elif Len > max_len:
        max_len = Len
        Len = 1
    else:
        Len = 1

plt.text(1, -15,f"Макс длина последовательности {max_len}")


name = ["1", "2", "3", "4", "5", "6"]

values.sort()
values = list(values)
counts = []

for i in range(0,6):
    counts.append(values.count(i+1))

for i in range(0,len(counts)):
    plt.text(i, counts[i], f"{counts[i]/10}%")

sorted_values = []

plt.bar(name, counts)

plt.title("Кубик")

plt.xlabel("Число")
plt.ylabel("Кол-во")

plt.show()
