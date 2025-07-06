import numpy as np

class Transformer2D:
    def __init__(self):
        pass

    def rotate(self, vector: np.ndarray, deg: float, clockwise: bool = False) -> np.ndarray:
        if clockwise:
            deg = -deg
        v = np.append(np.array(vector), 1)
        R = self.__rotation_matrix(deg)

        return (R @ v)[:2]

    def scale(self, vector: tuple[float, float], factor: tuple[float, float]) -> np.ndarray:
        v = np.append(np.array(vector), 1)
        S = self.__scale_matrix(factor)

        return (S @ v)[:2]

    def translate(self, vector: tuple[float, float], offset: tuple[float, float]) -> np.ndarray:
        v = np.append(np.array(vector), 1)
        T = self.__translation_matrix(offset)

        return (T @ v)[:2]

    def transform(self, vector: tuple[float, float], rotation: float, scale: tuple[float, float], translation: tuple[float, float]) -> np.ndarray:
        v = np.append(np.array(vector), 1)
        R = self.__rotation_matrix(rotation)
        S = self.__scale_matrix(scale)
        T = self.__translation_matrix(translation)

        return (T @ S @ R @ v)[:2]

    def __rotation_matrix(self, deg: float) -> np.ndarray:
        rad = np.deg2rad(deg)
        return np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad),  np.cos(rad), 0],
            [0          ,  0          , 1]
            ])

    def __scale_matrix(self, s: tuple[float, float]) -> np.ndarray:
        return np.array([
            [s[0], 0   , 0],
            [0   , s[1], 0],
            [0   , 0   , 1]
            ])

    def __translation_matrix(self, offset: tuple[float, float]) -> np.ndarray:
        return np.array([
            [1, 0, offset[0]],
            [0, 1, offset[1]],
            [0, 0, 1        ]
            ])
