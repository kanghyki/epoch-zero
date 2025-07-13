import matplotlib.pyplot as plt
import numpy as np
from mlp import MLP
import activation as act
import loss

plt.rcParams['font.family'] = 'AppleGothic'

# XOR 데이터
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("MLP 실험 통합 시각화", fontsize=16)

# 1. 활성 함수별 손실
activation_fns = {
    "Sigmoid": (act.sigmoid, act.sigmoid_grad),
    "Tanh": (act.tanh, act.tanh_grad),
    "ReLU": (act.relu, act.relu_grad),
    "Leaky ReLU": (act.leaky_relu, act.leaky_relu_grad),
    "ELU": (act.elu, act.elu_grad),
    "GELU": (act.gelu, act.gelu_grad),
}
for name, (a_fn, a_grad) in activation_fns.items():
    model = MLP([2, 4, 1], a_fn, a_grad, loss.mse, loss.mse_grad)
    losses = model.train(X, y, epochs=5000, lr=0.1)
    axes[0,0].plot(losses, label=name)
axes[0,0].set_title("① 활성 함수별 손실")
axes[0,0].set_xlabel("Epoch")
axes[0,0].set_ylabel("Loss")
axes[0,0].legend()
axes[0,0].grid(True)

# 2. 손실 함수별 학습
loss_fns = {
    "MSE": (loss.mse, loss.mse_grad),
    "Binary Cross Entropy": (loss.binary_cross_entropy, loss.binary_cross_entropy_grad),
    "Huber Loss": (loss.huber, loss.huber_grad)
}
for name, (l_fn, l_grad) in loss_fns.items():
    model = MLP([2, 4, 1], act.sigmoid, act.sigmoid_grad, l_fn, l_grad)
    losses = model.train(X, y, epochs=5000, lr=0.1)
    axes[0,1].plot(losses, label=name)
axes[0,1].set_title("② 손실 함수별 손실")
axes[0,1].set_xlabel("Epoch")
axes[0,1].set_ylabel("Loss")
axes[0,1].legend()
axes[0,1].grid(True)

# 3. 구조별 손실 그래프
structures = {
    "2-2-1": [2,2,1],
    "2-4-1": [2,4,1],
    "2-4-4-1": [2,4,4,1],
    "2-8-8-1": [2,8,8,1],
}
for name, layers in structures.items():
    model = MLP(layers, act.sigmoid, act.sigmoid_grad, loss.mse, loss.mse_grad)
    losses = model.train(X, y, epochs=5000, lr=0.1)
    axes[1,0].plot(losses, label=name)
axes[1,0].set_title("③ 구조별 손실")
axes[1,0].set_xlabel("Epoch")
axes[1,0].set_ylabel("Loss")
axes[1,0].legend()
axes[1,0].grid(True)

# 4. MLP 뉴런 구조 시각화
def draw_network(ax, layer_sizes):
    v_spacing = 1
    h_spacing = 2
    neuron_positions = []
    for layer_idx, num_neurons in enumerate(layer_sizes):
        x = layer_idx * h_spacing
        top = v_spacing * (num_neurons - 1) / 2
        positions = [(x, top - i * v_spacing) for i in range(num_neurons)]
        neuron_positions.append(positions)

    # 뉴런
    for layer in neuron_positions:
        for (x, y) in layer:
            circle = plt.Circle((x, y), 0.3, color='skyblue', ec='k')
            ax.add_patch(circle)

    # 연결선
    for l1, l2 in zip(neuron_positions[:-1], neuron_positions[1:]):
        for (x1, y1) in l1:
            for (x2, y2) in l2:
                ax.plot([x1, x2], [y1, y2], color='gray', lw=0.5)

    ax.set_xlim(-1, len(layer_sizes)*2)
    ax.set_ylim(-5, 5)
    ax.axis('off')

axes[1,1].set_title("④ MLP 구조: [2, 4, 4, 4, 4, 1]")
draw_network(axes[1,1], [2, 4, 4, 4, 4, 1])

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
