import numpy as np
import matplotlib.pyplot as plt

# Генерація послідовності
n = 110
sequence = np.random.random(n)
print(sequence)

# 1.1. Оцінка математичного сподівання
mean_estimate = np.mean(sequence)
print(f"1.1. Оцінка математичного сподівання: {mean_estimate:.4f}")

# 1.2. Оцінка дисперсії
variance_estimate = np.var(sequence)
print(f"1.2. Оцінка дисперсії: {variance_estimate:.4f}")

# 1.3. Побудова частотної таблиці
L = 10
hist, bin_edges = np.histogram(sequence, bins=L)
relative_freq = hist / n

print("\n1.3. Частотна таблиця:")
print("Інтервал | Кількість СВ | Відносна частота")
for i in range(L):
    print(f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f} | {hist[i]} | {relative_freq[i]:.4f}")

# 1.4. Побудова гістограми
plt.figure(figsize=(10, 6))
plt.hist(sequence, bins=L, density=True, alpha=0.7, color='b')
plt.title("Гістограма розподілу псевдовипадкових чисел")
plt.xlabel("Значення")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

# 2. Моделювання дискретної випадкової величини
xi = [3, 5, 8, 14, 27, 29, 35]
pi = [0.02, 0.07, 0.1, 0.19, 0.19, 0.2, 0.23]

discrete_rv = np.random.choice(xi, size=n, p=pi)

print(discrete_rv)
# 2.1. Оцінка математичного сподівання ДВВ
discrete_mean = np.mean(discrete_rv)
print(f"\n2.1. Оцінка математичного сподівання ДВВ: {discrete_mean:.4f}")

# 2.2. Оцінка дисперсії ДВВ
discrete_variance = np.var(discrete_rv)
print(f"2.2. Оцінка дисперсії ДВВ: {discrete_variance:.4f}")

# 2.3. Побудова частотної таблиці для ДВВ
unique, counts = np.unique(discrete_rv, return_counts=True)
discrete_freq = dict(zip(unique, counts))

print("\n2.3. Частотна таблиця для ДВВ:")
print("Значення | Кількість | Відносна частота")
for value, count in discrete_freq.items():
    print(f"{value} | {count} | {count/n:.4f}")

# 2.4. Побудова гістограми для ДВВ
plt.figure(figsize=(10, 6))
plt.hist(discrete_rv, bins=len(xi), density=True, alpha=0.7, color='g')
plt.title("Гістограма розподілу дискретної випадкової величини")
plt.xlabel("Значення")
plt.ylabel("Частота")
plt.xticks(xi)
plt.grid(True)
plt.show()