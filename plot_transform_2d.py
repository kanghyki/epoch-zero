import matplotlib.pyplot as plt
import transform_2d as t2d
import numpy as np

t = t2d.Transformer2D()
v = (2, 2)
rv = t.transform(v, r=90)
sv = t.transform(v, s=(3, 3))
tv = t.transform(v, t=(3, -1))
tfv = t.transform(v, r = 90, s = (2, 2), t = (1, 1))

def to_int_tuple(t: tuple[float, float], *, tol: float = 1e-8) -> tuple[int, int]:
    a, b = t
    a_rounded = round(a)
    b_rounded = round(b)

    if abs(a - a_rounded) >= tol:
        raise ValueError(f"{a} is not close enough to an integer")
    if abs(b - b_rounded) >= tol:
        raise ValueError(f"{b} is not close enough to an integer")

    return (int(a_rounded), int(b_rounded))

vectors = {
    f'Original {to_int_tuple(v)}': {
        'vec': v,
        'color': '#1f77b4' # 파랑
    },
    f'CCW Rotated 90° {to_int_tuple(rv)}': {
        'vec': rv,
        'color': '#d62728' # 빨강
    },
    f'Scaled 3x {to_int_tuple(sv)}': {
        'vec': sv,
        'color': '#ff7f0e' # 주황
    },
    f'Translated {to_int_tuple(tv)}': {
        'vec': tv,
        'color': '#9467bd' # 보라
    },
    f'Transformed {to_int_tuple(tfv)}': {
        'vec': tfv,
        'color': '#83c092' # 민트
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
