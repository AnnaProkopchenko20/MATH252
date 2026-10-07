import math
import matplotlib.pyplot as plt
import numpy as np

def stretch(X,a,b):
    tm = np.array([
        [a,0],
        [0,b]
    ])

    print("Stretch matrix:\n", tm)
    return tm.dot(X)

def shear(X,a,b):
    tm = np.array([
        [1,a],
        [b,1]
    ])

    print("Shear matrix:\n", tm)
    return tm.dot(X)

def reflection(X,a,b):
    tm = np.array([
        [pow(a,2) - pow(b,2), 2*a*b],
        [2*a*b, pow(b,2) - pow(a,2)]
    ]).dot(1 / (pow(a,2) + pow(b,2)))

    print("Reflection matrix:\n", tm)
    return tm.dot(X)

def rotation(X,O):
    tm = np.array([
        [math.cos(O), -math.sin(O)],
        [math.sin(O), math.cos(O)]
    ])

    print("Rotation matrix:\n", tm)
    return tm.dot(X)

def print_2d(X, title):
    xs, ys = X[0], X[1]
    fig, ax = plt.subplots(figsize=(6, 6))  # create figure + axes
    ax.fill(xs, ys, color="gray", alpha=0.6)  # filled silhouette
    ax.plot(xs, ys, color="black", lw=0.8)  # outline (optional)
    ax.set_aspect("equal")  # keep proportions, no stretching
    ax.axhline(0, color="lightgray")  # x-axis
    ax.axvline(0, color="lightgray")  # y-axis
    ax.grid(True, alpha=0.3)
    ax.set_title(title)
    plt.show()  # display the window

LYNX = np.array([
    [209.70, 368.42], [157.63, 332.16], [118.82, 284.21], [80.95, 224.56], [43.08, 244.44], [20.36, 266.67],
    [-4.26, 293.57], [2.37, 263.16], [-20.36, 292.40], [-39.29, 299.42], [-21.30, 259.65],
    [-50.65, 267.84], [-39.29, 242.11], [-55.38, 240.94], [-100.83, 300.58], [-149.11, 345.03], [-172.78, 361.40],
    [-189.82, 300.58], [-192.66, 225.73], [-181.30, 145.03], [-168.05, 104.09], [-184.14, 66.67],
    [-186.98, 31.58], [-183.20, 3.51], [-208.76, -4.68], [-197.40, -29.24], [-182.25, -44.44], [-203.08, -43.27],
    [-172.78, -92.40], [-131.12, -126.32], [-101.78, -147.37], [-74.32, -163.74], [-110.30, -224.56],
    [-143.43, -287.72], [-161.42, -240.94], [-282.60, -221.05], [-388.64, -205.85], [-370.65, -301.75],
    [-339.41, -397.66], [18.46, -397.66], [345.09, -400.00], [359.29, -378.95], [367.81, -342.69], [346.98,-362.57],
    [363.08, -302.92], [357.40, -243.27], [348.88, -266.67], [336.57, -201.17], [290.18, -135.67],
    [240.00, -118.13], [258.93, -164.91], [257.99, -228.07], [252.31, -271.35], [256.09, -333.33],
    [247.57, -359.06], [230.53, -307.60], [194.56, -238.60], [160.47, -181.29], [120.71, -149.71],
    [165.21, -132.16], [201.18, -100.58], [183.20, -99.42], [221.07, -73.68], [253.25, -24.56], [222.01, -23.39],
    [251.36, -1.17], [262.72, 24.56], [234.32, 25.73], [214.44, 42.11], [202.13, 60.82], [220.12, 101.75],
    [234.32, 160.23], [240.00, 230.41], [232.43, 316.96]
])


def part1_task1_hardcoded():
    lynx = LYNX.T
    print_2d(lynx, "Original")
    print_2d(stretch(lynx, 1.6, 0.5), "Stretch (1.6, 0.5)")
    print_2d(shear(lynx, 0.8, 0), "Shear (0.8, 0): horizontal lean")
    print_2d(shear(lynx, 0, 0.6), "Shear (0, 0.6): vertical lean")
    print_2d(reflection(lynx, 1, 2), "Reflection about the line y = 2x")
    print_2d(reflection(lynx, 1, 0), "Reflection about the x-axis")
    print_2d(rotation(lynx, np.deg2rad(60)), "Rotation 60°")
    print_2d(rotation(lynx, np.deg2rad(-90)), "Rotation -90° (clockwise)")
    print_2d(stretch(lynx, -1, 1), "Stretch (-1, 1): a negative factor flips x")

def part1_task2_hardcoded():
    lynx = LYNX.T
    th = np.deg2rad(40)

    print_2d(rotation(shear(stretch(lynx, 1.6, 0.5), 0.8, 0.3), th),
             "Stretch -> Shear -> Rotation")

    print_2d(shear(rotation(stretch(lynx, 1.6, 0.5), th), 0.8, 0.3),
             "Stretch -> Rotation -> Shear")

    print_2d(rotation(stretch(shear(lynx, 0.8, 0.3), 1.6, 0.5), th),
             "Shear -> Stretch -> Rotation")

    print_2d(stretch(rotation(shear(lynx, 0.8, 0.3), th), 1.6, 0.5),
             "Shear -> Rotation -> Stretch")

    print_2d(shear(stretch(rotation(lynx, th), 1.6, 0.5), 0.8, 0.3),
             "Rotation -> Stretch -> Shear")

    print_2d(stretch(shear(rotation(lynx, th), 0.8, 0.3), 1.6, 0.5),
             "Rotation -> Shear -> Stretch")

if __name__ == "__main__":
    part1_task1_hardcoded()
    part1_task2_hardcoded()
