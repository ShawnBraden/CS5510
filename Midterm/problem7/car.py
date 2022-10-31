"""

Car model for Hybrid A* path planning

author: Zheng Zh (@Zhengzh)

"""

import sys
import pathlib
import math
root_dir = pathlib.Path(__file__).parent.parent.parent
sys.path.append(str(root_dir))

from math import cos, sin, tan, pi

import matplotlib.pyplot as plt
import numpy as np

from angle import rot_mat_2d

# WB = 3.0  # rear to front wheel
# W = 2.0  # width of car
L = 40.0 * 0.0254 # rear to front wheel in inches
W = 33.0 * 0.0254  # width of car in iches
LF = L  # distance from rear to vehicle front end
LB = 0  # distance from rear to vehicle back end
MAX_STEER = 0.6  # [rad] maximum steering angle

BUBBLE_DIST = (LF - LB) / 2.0  # distance from rear to center of vehicle.
BUBBLE_R = np.hypot((LF + LB) / 2.0, W / 2.0)  # bubble radius

# vehicle rectangle vertices
VRX = [LF, LF, -LB, -LB, LF]
VRY = [W / 2, -W / 2, -W / 2, W / 2, W / 2]


def check_car_collision(x_list, y_list, yaw_list, ox, oy, kd_tree):
    for i_x, i_y, i_yaw in zip(x_list, y_list, yaw_list):
        cx = i_x + BUBBLE_DIST * cos(i_yaw)
        cy = i_y + BUBBLE_DIST * sin(i_yaw)

        ids = kd_tree.query_ball_point([cx, cy], BUBBLE_R)

        if not ids:
            continue

        if not rectangle_check(i_x, i_y, i_yaw,
                               [ox[i] for i in ids], [oy[i] for i in ids]):
            return False  # collision

    return True  # no collision


def rectangle_check(x, y, yaw, ox, oy):
    # transform obstacles to base link frame
    rot = rot_mat_2d(yaw)
    for iox, ioy in zip(ox, oy):
        tx = iox - x
        ty = ioy - y
        converted_xy = np.stack([tx, ty]).T @ rot
        rx, ry = converted_xy[0], converted_xy[1]

        if not (rx > LF or rx < -LB or ry > W / 2.0 or ry < -W / 2.0):
            return False  # no collision

    return True  # collision


def plot_arrow(x, y, yaw, length=1.0, width=0.5, fc="r", ec="k"):
    """Plot arrow."""
    if not isinstance(x, float):
        for (i_x, i_y, i_yaw) in zip(x, y, yaw):
            plot_arrow(i_x, i_y, i_yaw)
    else:
        plt.arrow(x, y, length * cos(yaw), length * sin(yaw),
                  fc=fc, ec=ec, head_width=width, head_length=width, alpha=0.4)


def plot_car(x, y, yaw):
    car_color = '-k'
    c, s = cos(yaw), sin(yaw)
    rot = rot_mat_2d(-yaw)
    car_outline_x, car_outline_y = [], []
    for rx, ry in zip(VRX, VRY):
        converted_xy = np.stack([rx, ry]).T @ rot
        car_outline_x.append(converted_xy[0]+x)
        car_outline_y.append(converted_xy[1]+y)

    arrow_x, arrow_y, arrow_yaw = c * 1.5 + x, s * 1.5 + y, yaw
    plot_arrow(arrow_x, arrow_y, arrow_yaw)

    plt.plot(car_outline_x, car_outline_y, car_color)


def pi_2_pi(angle):
    return (angle + pi) % (2 * pi) - pi


def move(x, y, yaw, distance, steer, L=L):
    # x += distance * cos(yaw)
    # y += distance * sin(yaw)
    # yaw += pi_2_pi(distance * tan(steer) / L)  # distance/2
    # return x, y, yaw
    
    if (yaw > 0):
        v_right = 0.01
        v_left = 0.5
    else:
        v_right = 0.5
        v_left = 0.01

    x_now = x - (0.5 * (v_right + v_left) * (math.sin(yaw)) * distance)
    y_now = y + (0.5 * (v_right + v_left) * (math.cos(yaw)) * distance)
    theata_Now = yaw + (L * (v_right - v_left) * distance)

    return x_now, y_now, theata_Now


def main():
    x, y, yaw = 0., 0., 1.
    plt.axis('equal')
    plot_car(x, y, yaw)
    plt.show()


if __name__ == '__main__':
    main()