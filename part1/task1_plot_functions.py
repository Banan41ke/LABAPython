import numpy as np
import matplotlib.pyplot as plt

# диапазон x от -360 до 360 градусов
x_deg = np.linspace(-360, 360, 720)
x_rad = np.radians(x_deg)  # переводим в радианы

# вычисляем функции
f = np.exp(np.cos(x_rad)) + np.log(np.cos(0.6 * x_rad) ** 2 + 1) * np.sin(x_rad)
h = -np.log((np.cos(x_rad) + np.sin(x_rad)) ** 2 + 2.5) + 10

# построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x_deg, f, label="f(x) = e^(cos x) + ln(cos²(0.6x)+1)*sin x", color='blue')
plt.plot(x_deg, h, label="h(x) = -ln((cos x+sin x)²+2.5)+10", color='red')

plt.title("Графики функций f(x) и h(x)")
plt.xlabel("x (в градусах)")
plt.ylabel("Значение функции")
plt.legend()
plt.grid(True)
plt.show()
