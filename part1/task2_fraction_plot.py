import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = 5 / (x ** 2 - 9)

# избегаем деления на ноль (x = ±3)
y[np.abs(x - 3) < 1e-5] = np.nan
y[np.abs(x + 3) < 1e-5] = np.nan

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='purple', label='f(x) = 5 / (x² - 9)')
plt.axvline(x=3, color='r', linestyle='--', label='x=3, асимптота')
plt.axvline(x=-3, color='r', linestyle='--', label='x=-3, асимптота')
plt.title("График функции f(x) = 5 / (x² - 9)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-5, 5)
plt.grid(True)
plt.legend()
plt.show()
