import numpy as np

class Transformer2D:
    def __init__(self):
        pass

    def rotate(self, vector: np.ndarray, deg: float, clockwise: bool = False) -> np.ndarray:
        if clockwise:
            deg = -deg
        rad = np.deg2rad(deg)
        mat = np.array([
            [np.cos(rad), -np.sin(rad)],
            [np.sin(rad),  np.cos(rad)]
        ])
        return mat @ vector

    def scale(self, vector: np.ndarray, factor: float) -> np.ndarray:
        return vector * factor

    def translate(self, vector: np.ndarray, offset: np.ndarray) -> np.ndarray:
        return vector + offset

    def transform(self, vector: tuple[float, float], rotation: float, scale: tuple[float, float], translation: tuple[float, float]) -> np.ndarray:
        v = np.append(np.array(vector), 1)
        R = self.__rotation_matrix(rotation)
        S = self.__scale_matrix(np.array(scale))
        T = self.__translation_matrix(np.array(translation))

        return (T @ S @ R @ v)[:2]

    def __rotation_matrix(self, deg: float) -> np.ndarray:
        rad = np.deg2rad(deg)
        return np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad),  np.cos(rad), 0],
            [0          ,  0          , 1]
            ])

    def __scale_matrix(self, s: np.ndarray) -> np.ndarray:
        return np.array([
            [s[0], 0   , 0],
            [0   , s[1], 0],
            [0   , 0   , 1]
            ])

    def __translation_matrix(self, offset: np.ndarray) -> np.ndarray:
        return np.array([
            [1, 0, offset[0]],
            [0, 1, offset[1]],
            [0, 0, 1        ]
            ])
