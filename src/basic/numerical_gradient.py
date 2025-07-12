import numpy as np

def partial_derivative(f, x, i, h=1e-4):
    tmp = x[i]

    # f(x + h)
    x[i] = tmp + h
    fxh1 = f(x)
    # f(x - h)
    x[i] = tmp - h
    fxh2 = f(x)

    # 원래 값으로 복원
    x[i] = tmp

    # 편미분 계산
    return (fxh1 - fxh2) / (2 * h)

def numerical_gradient(f, x, h=1e-4):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        grad[i] = partial_derivative(f, x, i, h)

    return grad
