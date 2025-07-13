import numpy as np
from mlp import MLP

# XOR 데이터
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

# 모델 생성
model = MLP(input_size=2, hidden_size=2, output_size=1)

# 학습 수행
losses = model.train(X, y, epochs=10000, lr=0.1)

# 예측
predictions = model.predict(X)

# 출력
print("입력:")
print(X)
print("\n정답:")
print(y)
print("\n예측:")
print(predictions)

# 최종 손실
print("\n최종 손실:", round(losses[-1], 4))

for i in range(4):
    assert predictions[i] == y[i]
