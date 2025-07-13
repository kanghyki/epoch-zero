import matplotlib.pyplot as plt
import numpy as np
from mlp import MLP
import activation as act
import loss

plt.rcParams['font.family'] = 'AppleGothic'

np.random.seed(42)
# XOR 데이터
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

def plot_decision_boundary(model, X, y, ax, title):
    x_min, x_max = X[:, 0].min() - 0.2, X[:, 0].max() + 0.2
    y_min, y_max = X[:, 1].min() - 0.2, X[:, 1].max() + 0.2
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 200),
        np.linspace(y_min, y_max, 200)
    )
    grid = np.c_[xx.ravel(), yy.ravel()]
    preds = model.predict(grid).reshape(xx.shape)

    ax.contourf(xx, yy, preds, levels=[0, 0.5, 1], alpha=0.6, cmap="RdBu")
    ax.scatter(X[:, 0], X[:, 1], c=y.flatten(), cmap="binary", edgecolors='k', s=80)
    ax.set_title(title)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks([])
    ax.set_yticks([])

# 모델들 정의
structures = {
    "A. SLP (2-1)": [2, 1],
    "B. MLP-1 (2-2-1)": [2, 2, 1],
    "C. MLP-2 (2-4-4-1)": [2, 4, 4, 1]
}

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (name, layers) in zip(axes, structures.items()):
    model = MLP(layers, act.sigmoid, act.sigmoid_grad, loss.mse, loss.mse_grad)
    model.train(X, y, epochs=100000, lr=0.1)
    plot_decision_boundary(model, X, y, ax, name)

plt.suptitle("은닉층 유무/깊이에 따른 결정 경계 비교", fontsize=14)
plt.tight_layout()
plt.show()
