import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import open3d as o3d


def rotate_xy_tm(O):
    tm = np.array([
        [math.cos(O), -math.sin(O), 0],
        [math.sin(O), math.cos(O), 0],
        [0, 0, 1]
        ])

    return tm

def rotate_yz_tm(O):
    tm = np.array([
        [1, 0 , 0],
        [0, math.cos(O), -math.sin(O)],
        [0, math.sin(O), math.cos(O)]
    ])

    return tm

def rotate_xz_tm(O):
    tm = np.array([
        [math.cos(O), 0, -math.sin(O)],
        [0, 1, 0],
        [math.sin(O), 0, math.cos(O)]
    ])

    return tm

def rotate_xy(X, O):
    tm = np.array([
        [math.cos(O), -math.sin(O), 0],
        [math.sin(O), math.cos(O), 0],
        [0, 0, 1]
        ])

    print("RotateXY matrix:\n", tm)
    return tm.dot(X)

def rotate_yz(X, O):
    tm = np.array([
        [1, 0 , 0],
        [0, math.cos(O), -math.sin(O)],
        [0, math.sin(O), math.cos(O)]
    ])

    print("RotateYZ matrix:\n", tm)
    return tm.dot(X)

def rotate_xz(X, O):
    tm = np.array([
        [math.cos(O), 0, -math.sin(O)],
        [0, 1, 0],
        [math.sin(O), 0, math.cos(O)]
    ])

    print("RotateXZ matrix:\n", tm)
    return tm.dot(X)

def read_off(filename: str):
    with open(filename, 'r') as f:
        # Перевіряємо, чи перший рядок починається з OFF
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')

        # Зчитуємо кількість вершин, граней та ребер (третє значення часто ігнорується)
        n_verts, n_faces, _ = map(int, f.readline().strip().split())

        # Зчитуємо координати всіх вершин (x, y, z)
        verts = [list(map(float, f.readline().strip().split())) for _ in range(n_verts)]

        # Зчитуємо грані: перше число у рядку - кількість вершин грані (ігноруємо), далі індекси
        faces = [list(map(int, f.readline().strip().split()[1:])) for _ in range(n_faces)]

    # Повертаємо вершини у вигляді масиву NumPy та список граней
    return np.array(verts), faces


def visualize_off(vertices, faces):
    mesh = o3d.geometry.TriangleMesh()                  # створюємо трикутну сітку
    mesh.vertices = o3d.utility.Vector3dVector(vertices)  # завантажуємо вершини
    mesh.triangles = o3d.utility.Vector3iVector(faces)    # завантажуємо індекси граней
    mesh.compute_vertex_normals()                         # рахуємо нормалі для коректного відображення

    o3d.visualization.draw_geometries([mesh])             # відкриваємо інтерактивне вікно

def part2_task3_hardcoded(vertices, faces):
    vertices = vertices.T
    visualize_off(rotate_xy(vertices, np.deg2rad(60)).T, faces)
    visualize_off(rotate_xz(vertices, np.deg2rad(30)).T, faces)
    visualize_off(rotate_yz(vertices, np.deg2rad(60)).T, faces)



def part2_task4_hardcoded(vertices, faces):
    vertices = vertices.T

    visualize_off(rotate_yz(rotate_xz(rotate_xy(vertices, np.deg2rad(60)),np.deg2rad(30)),np.deg2rad(45)).T, faces)
    print("\nYZ * XZ * XY:\n",rotate_yz_tm(45) @ rotate_xz_tm(30) @ rotate_xy_tm(60) ,"\n")

    visualize_off(rotate_yz(rotate_xy(rotate_xz(vertices, np.deg2rad(30)),np.deg2rad(60)),np.deg2rad(45)).T, faces)
    print("\nYZ * XY * XZ:\n",rotate_yz_tm(45) @ rotate_xy_tm(60) @ rotate_xz_tm(30) ,"\n")

    visualize_off(rotate_xy(rotate_xz(rotate_yz(vertices, np.deg2rad(45)),np.deg2rad(30)),np.deg2rad(60)).T, faces)
    print("\nXY * XZ * YZ:\n",rotate_xy_tm(60)  @ rotate_xz_tm(30) @ rotate_yz_tm(45),"\n")


if __name__ == "__main__":
    vertices, faces = read_off("airplane_0640.off")
    visualize_off(vertices, faces)

    part2_task3_hardcoded(vertices, faces)
    part2_task4_hardcoded(vertices, faces)


