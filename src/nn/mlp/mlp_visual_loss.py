import matplotlib.pyplot as plt
import numpy as np
from mlp import MLP

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

structures = {
    "A (2-2-1)": [2, 2, 1],
    "B (2-4-1)": [2, 4, 1],
    "C (2-4-4-1)": [2, 4, 4, 1],
    "D (2-8-8-1)": [2, 8, 8, 1],
}

for name, layers in structures.items():
    print(f"\n===== 구조: {name} =====")
    mlp = MLP(layers)
    losses = mlp.train(X, y, epochs=10000, lr=0.1)
    print(f"최종 손실: {losses[-1]:.4f}")
    plt.plot(losses, label=name)

plt.title("구조별 손실 감소 비교")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.legend()
plt.grid(True)
plt.show()
