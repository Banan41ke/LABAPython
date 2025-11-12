import matplotlib.pyplot as plt

# создаём холст
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# --- Тело панды (белое) ---
body = plt.Circle((0, -0.5), 1.3, color='white', ec='black', lw=2)
ax.add_patch(body)

# --- Голова (белая) ---
head = plt.Circle((0, 0.8), 1, color='white', ec='black', lw=2)
ax.add_patch(head)

# --- Уши (чёрные) ---
left_ear = plt.Circle((-0.7, 1.7), 0.35, color='black')
right_ear = plt.Circle((0.7, 1.7), 0.35, color='black')
ax.add_patch(left_ear)
ax.add_patch(right_ear)

# --- Глазные пятна ---
left_eye_patch = plt.Circle((-0.4, 1.0), 0.25, color='black')
right_eye_patch = plt.Circle((0.4, 1.0), 0.25, color='black')
ax.add_patch(left_eye_patch)
ax.add_patch(right_eye_patch)

# --- Глаза (белые круги внутри чёрных пятен) ---
left_eye = plt.Circle((-0.4, 1.05), 0.1, color='white')
right_eye = plt.Circle((0.4, 1.05), 0.1, color='white')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# --- Зрачки ---
ax.plot(-0.4, 1.05, 'ko', markersize=6)
ax.plot(0.4, 1.05, 'ko', markersize=6)

# --- Нос ---
ax.plot(0, 0.8, marker='o', color='black', markersize=8)

# --- Рот ---
ax.plot([-0.15, 0, 0.15], [0.65, 0.55, 0.65], 'k-', lw=2)

# --- Лапы ---
left_arm = plt.Circle((-0.9, 0.2), 0.4, color='black')
right_arm = plt.Circle((0.9, 0.2), 0.4, color='black')
left_leg = plt.Circle((-0.6, -1.2), 0.4, color='black')
right_leg = plt.Circle((0.6, -1.2), 0.4, color='black')
ax.add_patch(left_arm)
ax.add_patch(right_arm)
ax.add_patch(left_leg)
ax.add_patch(right_leg)

# --- Настройки отображения ---
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 2.2)
plt.title("Моя панда", fontsize=14)
plt.show()
