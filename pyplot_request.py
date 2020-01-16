import numpy as np
import matplotlib.pyplot as plt


def fig16a():
    theta, X11, X12, X14, X1num  = np.loadtxt('H:\\Fermilab\\pyplotplots\\X1_soln_r8.txt', skiprows=1).T   # fig16a

    fig = plt.figure()
    fig.set_size_inches(10, 7)
    dim = (12, 12)
    ax0_1 = plt.subplot2grid(dim, (0, 0), colspan=12, rowspan=12)  # absolute
    ax0_1.plot([x for x in theta], X11, color='blue', label='$X_1^{(1)}$', linestyle = '-', linewidth = 5)
    ax0_1.plot([x for x in theta], X12, color='red', label='$X_1^{(2)}$', linestyle = '-', linewidth = 5)
    ax0_1.plot([x for x in theta], X1num, color='black', label='$X_1^{(num)}$', linestyle = '-', linewidth = 5)
    ax0_1.set_xlabel('$\\theta_0/\\pi$ [rad]', fontsize=20, fontname="Times New Roman")
    ax0_1.set_ylabel('$X_1$', fontsize=20, fontname="Times New Roman")
    ax0_1.set_xticklabels([round(x, 4) for x in ax0_1.get_xticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.set_yticklabels([round(x, 4) for x in ax0_1.get_yticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.minorticks_on()
    ax0_1.yaxis.set_ticks_position('both')
    ax0_1.xaxis.set_ticks_position('both')
    ax0_1.tick_params(which='major', direction='in', length=6, width=1.2)
    ax0_1.tick_params(which='minor', direction='in', length=3, width=1.2)
    # ax0_1.legend(loc='right', bbox_to_anchor=(1.47, 0.5), ncol = 1, handlelength = 3, frameon = False, shadow = False, prop={'family': 'Times New Roman', 'size': 20})
    ax0_1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.14), ncol=3, handlelength=4, frameon=False, shadow=False,
                     prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig('H:\\Fermilab\\pyplotplots\\fig16a.png', bbox_inches='tight')
    # plt.show()
    plt.close()


def fig16b():
    theta, X11, X12, X14, h1, h2 = np.loadtxt('H:\\Fermilab\\pyplotplots\\Err-X1_soln_r8.txt', skiprows=1).T  # fig16b

    fig = plt.figure()
    fig.set_size_inches(10, 7)
    dim = (12, 12)
    ax0_1 = plt.subplot2grid(dim, (0, 0), colspan=12, rowspan=12)  # absolute
    ax0_1.plot([x for x in theta], X11, color='blue', label='$X_1^{(1)}$', linestyle='-', linewidth=5)
    ax0_1.plot([x for x in theta], X12, color='red', label='$X_1^{(2)}$', linestyle='-', linewidth=5)
    # ax0_1.plot([x  for x in theta], X14, color='cyan', label='$X_1^{(4)}$', linestyle='-', linewidth=5)
    ax0_1.axhline(0.1, color = (0, 1, 0, 0), linestyle = 'dashed', alpha = 0.7, linewidth = 4)
    ax0_1.axhline(0.2, color = 'black', linestyle = 'dashed', alpha = 0.7, linewidth = 4)
    ax0_1.set_xlabel('$\\theta_0/\\pi$ [rad]', fontsize=20, fontname="Times New Roman")
    ax0_1.set_ylabel('Relative error in $X_1$', fontsize=20, fontname="Times New Roman")
    ax0_1.set_xticklabels([round(x, 4) for x in ax0_1.get_xticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.set_yticklabels([round(x, 4) for x in ax0_1.get_yticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.minorticks_on()
    ax0_1.yaxis.set_ticks_position('both')
    ax0_1.xaxis.set_ticks_position('both')
    ax0_1.tick_params(which='major', direction='in', length=6, width=1.2)
    ax0_1.tick_params(which='minor', direction='in', length=3, width=1.2)
    # ax0_1.legend(loc='right', bbox_to_anchor=(1.47, 0.5), ncol = 1, handlelength = 3, frameon = False, shadow = False, prop={'family': 'Times New Roman', 'size': 20})
    ax0_1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.14), ncol=3, handlelength=4, frameon=False, shadow=False,
                 prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig('H:\\Fermilab\\pyplotplots\\fig16b.png', bbox_inches='tight')
    # plt.show()
    plt.close()


def fig17a():
    theta, X21, X22, X24, X2num = np.loadtxt('H:\\Fermilab\\pyplotplots\\X2_soln_r8.txt', skiprows=1).T   # fig16a

    fig = plt.figure()
    fig.set_size_inches(10, 7)
    dim = (12, 12)
    ax0_1 = plt.subplot2grid(dim, (0, 0), colspan=12, rowspan=12)  # absolute
    ax0_1.plot([x for x in theta], X21, color='blue', label='$X_2^{(1)}$', linestyle = '-', linewidth = 5)
    ax0_1.plot([x for x in theta], X22, color='red', label='$X_2^{(2)}$', linestyle = '-', linewidth = 5)
    ax0_1.plot([x for x in theta], X2num, color='black', label='$X_2^{(num)}$', linestyle = '-', linewidth = 5)
    ax0_1.set_xlabel('$\\theta_0/\\pi$ [rad]', fontsize=20, fontname="Times New Roman")
    ax0_1.set_ylabel('$X_2$', fontsize=20, fontname="Times New Roman")
    ax0_1.set_xticklabels([round(x, 4) for x in ax0_1.get_xticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.set_yticklabels([round(x, 4) for x in ax0_1.get_yticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.minorticks_on()
    ax0_1.yaxis.set_ticks_position('both')
    ax0_1.xaxis.set_ticks_position('both')
    ax0_1.tick_params(which='major', direction='in', length=6, width=1.2)
    ax0_1.tick_params(which='minor', direction='in', length=3, width=1.2)
    # ax0_1.legend(loc='right', bbox_to_anchor=(1.47, 0.5), ncol = 1, handlelength = 3, frameon = False, shadow = False, prop={'family': 'Times New Roman', 'size': 20})
    ax0_1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.14), ncol=3, handlelength=4, frameon=False, shadow=False,
                     prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig('H:\\Fermilab\\pyplotplots\\fig17a.png', bbox_inches='tight')
    # plt.show()
    plt.close()


def fig17b():
    theta, X21, X22, X24, h1, h2 = np.loadtxt('H:\\Fermilab\\pyplotplots\\Err-X2_soln_r8.txt', skiprows=1).T  # fig16b

    fig = plt.figure()
    fig.set_size_inches(10, 7)
    dim = (12, 12)
    ax0_1 = plt.subplot2grid(dim, (0, 0), colspan=12, rowspan=12)  # absolute
    ax0_1.plot([x for x in theta], X21, color='blue', label='$X_2^{(1)}$', linestyle='-', linewidth=5)
    ax0_1.plot([x for x in theta], X22, color='red', label='$X_2^{(2)}$', linestyle='-', linewidth=5)
    # ax0_1.plot([x  for x in theta], X24, color='cyan', label='$X_2^{(4)}$', linestyle='-', linewidth=5)
    ax0_1.axhline(0.1, color = (0, 1, 0, 0), linestyle = 'dashed', alpha = 0.7, linewidth = 4)
    ax0_1.axhline(0.2, color = 'black', linestyle = 'dashed', alpha = 0.7, linewidth = 4)
    ax0_1.set_xlabel('$\\theta_0/\\pi$ [rad]', fontsize=20, fontname="Times New Roman")
    ax0_1.set_ylabel('Relative error in $X_2$', fontsize=20, fontname="Times New Roman")
    ax0_1.set_xticklabels([round(x, 4) for x in ax0_1.get_xticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.set_yticklabels([round(x, 4) for x in ax0_1.get_yticks()], fontsize=20, fontname="Times New Roman")
    ax0_1.minorticks_on()
    ax0_1.yaxis.set_ticks_position('both')
    ax0_1.xaxis.set_ticks_position('both')
    ax0_1.tick_params(which='major', direction='in', length=6, width=1.2)
    ax0_1.tick_params(which='minor', direction='in', length=3, width=1.2)
    # ax0_1.legend(loc='right', bbox_to_anchor=(1.47, 0.5), ncol = 1, handlelength = 3, frameon = False, shadow = False, prop={'family': 'Times New Roman', 'size': 20})
    ax0_1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.14), ncol=3, handlelength=4, frameon=False, shadow=False,
                 prop={'family': 'Times New Roman', 'size': 20})
    plt.savefig('H:\\Fermilab\\pyplotplots\\fig17b.png', bbox_inches='tight')
    # plt.show()
    plt.close()


fig16a()
fig16b()
fig17a()
fig17b()