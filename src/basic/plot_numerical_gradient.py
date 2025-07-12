import numpy as np
import matplotlib.pyplot as plt

# 함수 정의
def f(x):
    return x[0]**2 + x[1]**2

# 기울기 정의
def grad_f(x):
    return np.array([2*x[0], 2*x[1]])

# 시작점과 학습률
start = np.array([3.0, 4.0])
lr = 0.1
steps = 10

# 점 기록용 리스트
path = [start.copy()]

# 경사상승 (gradient ascent): 반대 방향이면 descent
x = start.copy()
for _ in range(steps):
    x = x + lr * grad_f(x)  # ascent (증가 방향)
    path.append(x.copy())

# 경로를 x, y로 나누기
path = np.array(path)
px, py = path[:, 0], path[:, 1]

# 배경용 등고선 데이터
x_vals = np.linspace(-1, 10, 100)
y_vals = np.linspace(-1, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X**2 + Y**2

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=30, cmap='gray')
plt.plot(px, py, 'o-', color='red', label='Gradient Ascent Path')
plt.quiver(px[:-1], py[:-1],
           px[1:] - px[:-1], py[1:] - py[:-1],
           angles='xy', scale_units='xy', scale=1, color='blue', width=0.005)
plt.title("Gradient Ascent on $f(x, y) = x^2 + y^2$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
