# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

map = []
for i in range(0, 8, 2):
    map.append([1,0,1,0,1,0,1,0])
    map.append([0,1,0,1,0,1,0,1])


map = np.array(map)
map = map.astype("float64")
queen_pos = np.random.randint(0,7, 2)
print(queen_pos)
circle = plt.Circle((queen_pos[0], queen_pos[1]), 0.5, edgecolor='black', facecolor='red')
ax.add_patch(circle)

map[:, queen_pos[0]]= 0.8
map[queen_pos[1], :]= 0.8
i = queen_pos[0]+1
j = queen_pos[1]+1
while i <= 7 and j <= 7:
    map[j][i] = 0.8
    i += 1
    j += 1

i = queen_pos[0]-1
j = queen_pos[1]+1
while i >= 0 and j <= 7:
    map[j][i] = 0.8
    i -= 1
    j += 1

i = queen_pos[0]-1
j = queen_pos[1]-1
while i >= 0 and j >= 0:
    map[j][i] = 0.8
    i -= 1
    j -= 1

i = queen_pos[0]+1
j = queen_pos[1]-1
while i <=7 and j >= 0:
    map[j][i] = 0.8
    i += 1
    j -= 1

plt.imshow(map, cmap="hot_r")
plt.xticks([0,1,2,3,4,5,6,7], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
plt.yticks([0,1,2,3,4,5,6,7], ["1","2","3","4","5","6","7","8"])
plt.title("Chess")
plt.show()