import numpy as np

# 활성화 함수는 뉴런의 출력값을 비선형적으로 변환해주는 함수
# 대표적으로 sigmoid, relu, tanh 등이 있음
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

class Neuron:
    def __init__(self, input_size):
        self.w = np.random.randn(input_size)  # symmetry problem 해결을 위한 정규분포 난수
        self.b = 0.0  # 바이어스 초기화

    def forward(self, x):
        z = np.dot(self.w, x) + self.b
        return sigmoid(z)

neuron = Neuron(input_size=3)
# 입력 벡터
x = np.array([0.5, -0.2, 0.1])
output = neuron.forward(x)

print(f"input: {x}\noutput: {output}")
