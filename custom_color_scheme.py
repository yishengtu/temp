'''
Yisheng Tu, Tanaji Sen, Jean-Francois Ostiguy
'''

import gitDipole as gd
import gitQuadrupole as qq
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from matplotlib.colors import LinearSegmentedColormap


def dipole_example():
    a = 25  # radius of beampipe
    b = 20  # radius of the kicker plates
    theta_0 = 0.4*np.pi

    # create a dipole object instance
    dipole = gd.dipole(a = a, b = b, theta_0 = theta_0, mode='odd')

    # print out the characteristic impedance
    # dipole.get_characteristic_impedance(thickness=8, kf_even=5, kf_geo=5.5)     # using customized fitting value
    dipole.get_characteristic_impedance(thickness=8)    # using default fitting value

    # setup 2D-scan parameters
    x = np.linspace(-a, a, 50)  # change here to change the resolution!
    y = np.linspace(-a, a, 50)  # change here to change the resolution!
    x, y = np.meshgrid(x, y)
    x0 = np.concatenate(x)
    y0 = np.concatenate(y)

    # calculate the potential at all points on the 2D-scan
    num_of_pt = len(x[0])
    z_list = [dipole.phi_xy(xx, yy, number_of_item=200) for xx, yy in zip(x0, y0)]
    z = [z_list[i:i + num_of_pt] for i in range(0, len(z_list) - 1, num_of_pt)]

    # plot the figure, setup the plot parameters
    fig = plt.figure()
    fig.set_size_inches(12, 10)
    dim = (2, 2)
    ax1 = plt.subplot2grid(dim, (0, 0), colspan=2, rowspan=2)

    # make 2D-pseudocolor plot
    trial_cmap_list = [#(148./255., 0./255., 211./255.),
                       #(75./255., 0./255., 130./255.),
                       (0./255., 0./255., 255./255.),
                       (0./255., 255./255., 0./255.),
                       (255./255., 255./255., 0/255.),
                       (255./255., 127./255., 0/255.),
                       (148. / 255., 0. / 255., 211. / 255.)]
                       # (255/255., 0/255., 0/255.)]
    # n_bins = [3, 6, 10, 100]
    trial_cmap = LinearSegmentedColormap.from_list('mycmap', trial_cmap_list) #, N=n_bins)
    c = ax1.pcolor(x, y, z, cmap=trial_cmap, norm=colors.Normalize(vmin=-1, vmax=1))

    # adjust colorbar
    cbar = fig.colorbar(c, ax=ax1)
    cbar.ax.set_yticklabels([round(x, 4) for x in cbar.get_ticks()], fontsize = 20)

    # adjust aspect ratio
    ax1.set_aspect('equal')
    plt.show()


dipole_example()
