import numpy as np
import matplotlib.pyplot as plt

savefig_path = ''   # path to the folder you wish to save the figures

def dipo_demo(a = 25, b = 15):
    fig = plt.figure()
    fig.set_size_inches(10, 10)
    dim = (1, 1)
    ax = plt.subplot2grid(dim, (0, 0), colspan=1, rowspan=1)
    ax.set_aspect('equal')  # make sure it is a circle on the graph
    ax.axis('off')          # remove axis
    thickness = 3
    theta_list = np.linspace(0, 2 * np.pi, 1000)
    theta_0 = 0.25 * np.pi      # theta_0 physical parameter
    left_plate_theta = np.linspace(-theta_0, theta_0, 500)
    right_plate_theta = np.linspace(np.pi - theta_0, np.pi + theta_0, 500)
    up_gap_theta = np.linspace(theta_0, np.pi - theta_0, 500)
    down_gap_theta = np.linspace(np.pi + theta_0, 2 * np.pi - theta_0, 500)
    beam_pipe_x = [a * np.cos(x) for x in theta_list]
    beam_pipe_y = [a * np.sin(x) for x in theta_list]
    left_plate_x = [b * np.cos(x) for x in left_plate_theta]
    left_plate_y = [b * np.sin(x) for x in left_plate_theta]
    right_plate_x = [b * np.cos(x) for x in right_plate_theta]
    right_plate_y = [b * np.sin(x) for x in right_plate_theta]

    up_gap_x = [b * np.cos(x) for x in up_gap_theta]
    up_gap_y = [b * np.sin(x) for x in up_gap_theta]
    down_gap_x = [b * np.cos(x) for x in down_gap_theta]
    down_gap_y = [b * np.sin(x) for x in down_gap_theta]

    ax.plot(beam_pipe_x, beam_pipe_y, color='black', linewidth=5)
    ax.plot(left_plate_x, left_plate_y, color='black', linewidth=10)
    ax.plot(right_plate_x, right_plate_y, color='black', linewidth=10)

    ax.plot([0, - b * np.cos(theta_0)], [0, b * np.sin(theta_0)], color='black', linestyle='dashed', alpha=0.5, linewidth=2)
    ax.plot([0, - b * np.cos(- theta_0)], [0, b * np.sin(- theta_0)], color='black', linestyle='dashed', alpha=0.5, linewidth=2)
    # ax.plot([0, b], [0, 0], color='black', linestyle='-.', alpha=0.5, linewidth=2)
    ax.plot([0, b * np.cos(theta_0 * 2.0 / 3.0)], [0, b * np.sin(theta_0 * 2.0 / 3.0)], color='black', linestyle='dashed', alpha=0.5, linewidth=2)
    ax.plot([0, a * np.cos(- theta_0 * 1.0 / 3.0)], [0, a * np.sin(- theta_0 * 1.0 / 3.0)], color='black', linestyle='dashed', alpha=0.5, linewidth=2)

    fontsize = 35
    ax.annotate('$2\\theta_0$', (-10, -0.5), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$-V_p$', (b * np.cos(theta_0) - 2, b * np.sin(theta_0) + 2), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$V_p$', (- b * np.cos(theta_0) - 1.5, b * np.sin(theta_0) + 2), fontsize=fontsize, fontname="Times New Roman")
    # ax.annotate('$V=0$', (a * np.cos(np.pi / 4.0) + 0.5, a * np.sin(np.pi / 4.0) + 0.5), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('beampipe', (a * np.cos(np.pi / 4.0) - 1, - (a * np.sin(np.pi / 4.0) + 5)), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('plates', (-4.5, -b), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('P$_1$', (b + 1, 0), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('P$_2$', (-b - 5.0, 0), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$a$', (20 * np.cos(- theta_0 * 1.0 / 3.0), 20 * np.sin(- theta_0 * 1.0 / 3.0) + 1), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$b$', (b / 2 * np.cos(np.pi / 4.0), b / 2 * np.sin(np.pi / 4.0) - 0.5), fontsize=fontsize, fontname="Times New Roman")
    # ax.annotate('$\\theta$', (6, 0.5), fontsize=fontsize)
    # plt.show()
    plt.savefig(savefig_path + 'dipole_demo.png', bbox_inches='tight')
    plt.close()


def quad_demo(a = 25, b = 15):
    fig = plt.figure()
    fig.set_size_inches(10, 10)
    dim = (1, 1)
    ax = plt.subplot2grid(dim, (0, 0), colspan=1, rowspan=1)
    ax.set_aspect('equal')
    ax.axis('off')
    theta_list = np.linspace(0, 2 * np.pi, 1000)
    theta_0 = 0.18 * np.pi
    left_plate_theta = np.linspace(-theta_0, theta_0, 500)
    right_plate_theta = np.linspace(np.pi - theta_0, np.pi + theta_0, 500)
    up_plate_theta = np.linspace(np.pi / 2.0 - theta_0, np.pi / 2.0 + theta_0, 500)
    down_plate_theta = np.linspace(np.pi * 3.0 / 2.0 - theta_0, np.pi * 3.0 / 2.0 + theta_0, 500)
    beam_pipe_x = [a * np.cos(x) for x in theta_list]
    beam_pipe_y = [a * np.sin(x) for x in theta_list]
    left_plate_x = [b * np.cos(x) for x in left_plate_theta]
    left_plate_y = [b * np.sin(x) for x in left_plate_theta]
    right_plate_x = [b * np.cos(x) for x in right_plate_theta]
    right_plate_y = [b * np.sin(x) for x in right_plate_theta]
    up_plate_x = [b * np.cos(x) for x in up_plate_theta]
    up_plate_y = [b * np.sin(x) for x in up_plate_theta]
    down_plate_x = [b * np.cos(x) for x in down_plate_theta]
    down_plate_y = [b * np.sin(x) for x in down_plate_theta]

    theta_tip_13 = np.linspace(- theta_0, np.pi - theta_0, 100)
    theta_tip_24 = np.linspace(- theta_0, np.pi - theta_0, 100)
    theta_tip_13_ud = np.linspace(theta_0 + np.pi / 2.0, np.pi + theta_0 + np.pi / 2.0, 100)
    theta_tip_24_ud = np.linspace(theta_0 + np.pi / 2.0, np.pi + theta_0 + np.pi / 2.0, 100)


    ax.plot(beam_pipe_x, beam_pipe_y, color='black', linewidth=5)
    ax.plot(left_plate_x, left_plate_y, color='black', linewidth=10)
    ax.plot(right_plate_x, right_plate_y, color='black', linewidth=10)
    ax.plot(up_plate_x, up_plate_y, color='black', linewidth=10)
    ax.plot(down_plate_x, down_plate_y, color='black', linewidth=10)


    ax.plot([0, - b * np.cos(theta_0)], [0, b * np.sin(theta_0)], color='black', linestyle='dashed', alpha=0.5, linewidth = 2)
    ax.plot([0, - b * np.cos(- theta_0)], [0, b * np.sin(- theta_0)], color='black', linestyle='dashed', alpha=0.5, linewidth = 2)
    ax.plot([0, b * np.cos(np.pi/2 - theta_0)], [0, b * np.sin(np.pi/2 - theta_0)], color='black', linestyle='dashed', alpha=0.5, linewidth = 2)
    ax.plot([0, - b * np.cos(np.pi/2 - theta_0)], [0, b * np.sin(np.pi/2 - theta_0)], color='black', linestyle='dashed', alpha=0.5, linewidth = 2)
    # ax.plot([0, b], [0, 0], color='black', linestyle='-.', alpha=0.5, linewidth = 2)
    # ax.plot([0, a * np.cos(0.5 * np.pi / 3.0)], [0, a * np.sin(0.5 * np.pi / 3.0)], color='black', linestyle='-.', alpha=0.5, linewidth = 2)
    ax.plot([0, a * np.cos(- theta_0 * 1.0 / 3.0)], [0, a * np.sin(- theta_0 * 1.0 / 3.0)], color='black', linestyle='dashed', alpha=0.5, linewidth=2)


    fontsize = 35
    ax.annotate('$2\\theta_0$', (-11.5, -0.5), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$2\\theta_0$', (-3, 7), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$- V_p$', (b + 1, 2), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('P$_1$', (b + 1, -2), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$V_p$  P$_2$', (-4.5, b + 1.7), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$- V_p$', (-b - 7.5, 2), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('P$_3$', (-b - 5.0, -2), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$V_p$  P$_4$', (-4.5, -b + 2), fontsize=fontsize, fontname="Times New Roman")
    # ax.annotate('$V=0$', (a * np.cos(np.pi / 4.0) + 0.5, a * np.sin(np.pi / 4.0) + 0.5), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('beampipe', (a * np.cos(np.pi / 4.0) - 1, - (a * np.sin(np.pi / 4.0) + 5)), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('plates', (-5, -b - 4), fontsize=fontsize, fontname="Times New Roman")
    # ax.annotate('$a$', (0.5, a / 2.0), fontsize=fontsize)
    ax.annotate('$a$', (5 * np.cos(- theta_0 * 1.0 / 3.0), 5 * np.sin(- theta_0 * 1.0 / 3.0) - 3), fontsize=fontsize, fontname="Times New Roman")
    ax.annotate('$b$', (b / 2 * np.cos(np.pi / 8.0) - 1, b / 2 * np.sin(np.pi / 8.0) + 2), fontsize=fontsize, fontname="Times New Roman")
    # ax.annotate('$\\theta$', (6, 1), fontsize=fontsize)
    # plt.show()
    plt.savefig(savefig_path + 'quad_demo.png', bbox_inches='tight')
    plt.close()