<<<<<<< HEAD
import numpy as np


def area_of_triangle(coords: np.ndarray) -> float:
    double_t = coords[1:3].T - np.expand_dims(coords[0], 1)
    area_t = np.abs(np.linalg.det(double_t)) / 2
    return area_t


def center_of_mass(coords: np.ndarray) -> np.ndarray:
    return np.sum(coords, 0) / coords.shape[0]
=======
import numpy as np


def area_of_triangle(coords: np.ndarray) -> float:
    double_t = coords[1:3].T - np.expand_dims(coords[0], 1)
    area_t = np.abs(np.linalg.det(double_t)) / 2
    return area_t


def center_of_mass(coords: np.ndarray) -> np.ndarray:
    return np.sum(coords, 0) / coords.shape[0]
>>>>>>> 0c2441c35348cc2cb0d4bfa4f93dc736c7d002fd
