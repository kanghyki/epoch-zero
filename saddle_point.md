## 안장점(Saddle Point)란?

> **최대도 아니고 최소도 아닌**,
> 한 방향으로는 최솟값처럼 보이고
> 다른 방향으로는 최댓값처럼 보이는 지점
> 변수 하나를 고정 시키고 나머지 값을 생각해보자

말 안장처럼 가운데는 움푹 들어가 있고, 좌우는 올라와 있는 모습이라
영어로 **Saddle Point**(안장점)이라고 불림

## 경사하강법에선 왜 문제가 될까?

### 1. 기울기가 0인 지점인데

→ 최솟값이 아님

### 2. 그래서 경사하강법이

→ 그 자리에 머무르거나 이상한 방향으로 튈 수도 있음

## 수학적으로

안장점은 기울기(gradient)가 0인 **임계점**이지만,
헷세 행렬(Hessian)을 보면 **음수/양수 고윳값이 섞여 있음**
→ 즉, **볼록(convex)하지 않다**는 뜻

---

## 요약 정리

| 구분            | 설명                                                 |
| --------------- | ---------------------------------------------------- |
| 정의            | 기울기 0인 지점이지만 최소/최대가 아닌 점            |
| 예시            | $f(x, y) = x^2 - y^2$의 (0, 0)                       |
| 경사하강법 영향 | 수렴이 잘 안 되고 튈 수 있음                         |
| 왜 중요한가?    | LLM 학습 같은 고차원 공간에서도 안장점이 수없이 많음 |

## 어떻게 해결할까?

딥러닝에서는 이 문제를 해결하기 위해:

-   Momentum (이전 기울기의 관성)
-   Adam (적응형 학습률)
-   2차 미분 정보(Hessian)를 고려한 방법

같은 기법들을 써서 안장점이나 평평한 구간도 잘 빠져나가도록 도와줌
