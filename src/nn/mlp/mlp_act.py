import numpy as np
import matplotlib.pyplot as plt
from mlp import MLP
import activation as act
import warnings
plt.rcParams['font.family'] = 'AppleGothic'
warnings.filterwarnings("ignore", category=UserWarning)

X = np.array([
    [0, 0], [0, 1], [1, 0], [1, 1]
])
y = np.array([
    [0], [1], [1], [0]
])

activation_fns = {
    "Sigmoid": (act.sigmoid, act.sigmoid_grad),
    "Tanh": (act.tanh, act.tanh_grad),
    "ReLU": (act.relu, act.relu_grad),
    "Leaky ReLU": (act.leaky_relu, act.leaky_relu_grad),
    "ELU": (act.elu, act.elu_grad),
    "GELU": (act.gelu, act.gelu_grad),
}

for name, (activation, activation_grad) in activation_fns.items():
    print(f"\n▶ 활성 함수: {name}")
    mlp = MLP([2, 4, 1], activation, activation_grad)
    losses = mlp.train(X, y, epochs=100000, lr=0.1)
    print(f"최종 손실: {losses[-1]:.4f}")
    plt.plot(losses, label=name)

plt.title("활성 함수별 손실 감소 비교")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
