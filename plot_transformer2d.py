import matplotlib.pyplot as plt
import transformer2d as t2d
import numpy as np

t = t2d.Transformer2D()
v = np.array([2, 2])

vectors = {
    'Original (2, 2)': {
        'vec': v,
        'color': '#1f77b4' # 파랑
    },
    'CCW Rotated 90° (-2, 2)': {
        'vec': t.rotate(v, 90),
        'color': '#d62728' # 빨강
    },
    'Scaled 3x (6, 6)': {
        'vec': t.scale(v, 3),
        'color': '#ff7f0e' # 주황
    },
    'Translated (3, -1)': {
        'vec': t.translate(v, np.array([3, -1])),
        'color': '#9467bd' # 보라
    },
}

plt.figure(figsize=(7, 7))
ax = plt.gca()
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', linewidth=0.3, color='gray')

for label, data in vectors.items():
    vec = data['vec']
    color = data['color']

    plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color=color, width=0.005)
    plt.scatter(*vec, color=color, s=50, edgecolor='black', zorder=5)
    plt.text(*(vec + np.array([0.3, 0.3])), label, fontsize=9, color=color)

plt.xlabel('X', fontsize=11)
plt.ylabel('Y', fontsize=11)
plt.title("Vector Transformations", fontsize=15, weight='bold')

plt.tight_layout()
plt.show()
