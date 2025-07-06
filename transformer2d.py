from typing import Optional
import numpy as np

Vector2D = tuple[float, float]

class Transformer2D:
    def transform(self, vector: Vector2D, r: Optional[float] = None, s: Optional[Vector2D] = None, t: Optional[Vector2D] = None) -> tuple[float, float]:
        v = np.append(np.array(vector), 1)
        R = self.__rotation_matrix(0)
        S = self.__scale_matrix((1, 1))
        T = self.__translation_matrix((0, 0))
        if r:
            R = self.__rotation_matrix(r)
        if s:
            S = self.__scale_matrix(s)
        if t:
            T = self.__translation_matrix(t)

        return tuple((T @ S @ R @ v)[:2])

    def __rotation_matrix(self, deg: float) -> np.ndarray:
        rad = np.deg2rad(deg)
        return np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad),  np.cos(rad), 0],
            [0          ,  0          , 1]
            ])

    def __scale_matrix(self, s: Vector2D) -> np.ndarray:
        return np.array([
            [s[0], 0   , 0],
            [0   , s[1], 0],
            [0   , 0   , 1]
            ])

    def __translation_matrix(self, offset: Vector2D) -> np.ndarray:
        return np.array([
            [1, 0, offset[0]],
            [0, 1, offset[1]],
            [0, 0, 1        ]
            ])
