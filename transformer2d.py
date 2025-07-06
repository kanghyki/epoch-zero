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
