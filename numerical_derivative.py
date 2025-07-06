# 함수 f(x)에서의 수치 미분 계산
def numerical_derivative(f, x, h=1e-4):
    return (f(x + h) - f(x - h)) / (2 * h)
