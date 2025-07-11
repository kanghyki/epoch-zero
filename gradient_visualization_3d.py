
import numpy as np
import matplotlib.pyplot as plt

# 함수 정의
def f(x, y):
    return x**2 + y**2

# 그래디언트 정의
def grad_f(x, y):
    return 2*x, 2*y

# 좌표 생성
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 그래디언트 벡터 계산
U, V = grad_f(X, Y)

# 3D 곡면과 벡터 필드 시각화
fig = plt.figure(figsize=(14, 6))

# 곡면 시각화
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax1.set_title('Surface: z = x² + y²')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

# 평면에서의 기울기 벡터 시각화
ax2 = fig.add_subplot(1, 2, 2)
contours = ax2.contour(X, Y, Z, levels=20)
ax2.quiver(X, Y, U, V, color='r')
ax2.set_title('Gradient Vectors on x-y Plane')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.grid(True)
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()
