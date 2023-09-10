import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(r'D:\Codes\python\labNA2\dataset_2.txt', delimiter=',', dtype=None)

dates = [d[0] for d in data]
visitors = [d[1] for d in data]


missing_indices = []
for i in range(len(visitors)):
    if np.isnan(visitors[i]):
        missing_indices.append(i)

for index in missing_indices:
    left_index = index - 1
    right_index = index + 1

    while np.isnan(visitors[left_index]):
        left_index -= 1

    while np.isnan(visitors[right_index]):
        right_index += 1

    left_value = visitors[left_index]
    right_value = visitors[right_index]
    interval = right_index - left_index

    for i in range(interval - 1):
        visitors[left_index + 1 + i] = left_value + (right_value - left_value) / interval * (i + 1)


plt.plot(dates, visitors, label='Interpolated')
plt.plot(dates, visitors, 'o', label='Original')
plt.xlabel('Date')
plt.ylabel('Number of Visitors')
plt.xticks(rotation=90)
plt.legend()
plt.show()