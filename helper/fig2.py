import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from acceptance import not_pass_rate
from acceptance.simulate import simulate_many

auxiliary_line_color = '#9f9f9f'
data_line_color = 'c'
fill_color = '#bfbfbf'
data_line_width = 1.0
auxiliary_line_width = 0.5

arrow_width = 0.01
arrow_head_length = 1.5
arrow_head_width = 0.5

annotate_arrow_width = 0.1
annotate_arrow_head_width = 1.5
annotate_arrow_head_length = 6

def draw_OC(savefile):

    fig, ax = plt.subplots(1,1)

    plt.vlines(5, ymin=0, ymax=105, color=auxiliary_line_color, linewidth=auxiliary_line_width)
    plt.vlines(25, ymin=0, ymax=15, color=auxiliary_line_color, linewidth=auxiliary_line_width)
    plt.vlines(50, ymin=0, ymax=15, color=auxiliary_line_color, linewidth=auxiliary_line_width)
    plt.hlines(100, xmin=0, xmax=30, color=auxiliary_line_color, linewidth=auxiliary_line_width)

    #knonw the sigma
    n = 3
    k = 0.7
    # compute the $\frac{l-\mu}\sigma$. 
    # Note that the ppf function will return the Cumulative distribution probability of the L's left
    # We need the probability of L's right
    z1 = - norm.ppf(not_pass_rate)
    z_1_alpha =  - math.sqrt(n)*(k - z1)
    acc = norm.cdf(z_1_alpha)
    plt.plot(np.array(not_pass_rate)*100, acc*100, color=data_line_color, linewidth=data_line_width)
    plt.hlines(acc[8]*100, xmin=0, xmax=60, color=auxiliary_line_color, linewidth=auxiliary_line_width)

    #unknown the sigma
    n= 15
    k = 1.1
    A_nk = math.sqrt((1 + k*k/2)/n)
    z = -norm.ppf(not_pass_rate)
    z_beta = (k - z)/A_nk
    # compute the Cumulative distribution probability of the right
    # The function cdf will return the left probability 
    beta = 1 - norm.cdf(z_beta)
    plt.plot(np.array(not_pass_rate)*100, beta*100, color=data_line_color, linewidth=data_line_width)

    plt.hlines(y=(beta[1])*100, xmin=0, xmax=30, colors=auxiliary_line_color, linewidth=auxiliary_line_width)
    plt.hlines(y=beta[5]*100, xmin=0, xmax=30, colors=auxiliary_line_color, linewidth=auxiliary_line_width)


    plt.vlines(x=20, ymin=100, ymax=105, colors=auxiliary_line_color, linewidth=auxiliary_line_width)
    plt.vlines(x=20, ymin=90, ymax=95, colors=auxiliary_line_color, linewidth=auxiliary_line_width)
    

    plt.text(19, 96.5, '$\\alpha$', color=auxiliary_line_color, fontsize=9)
    plt.annotate('$\\beta$', xy=(25, 5), xytext=(15, 5),
                    arrowprops=dict(arrowstyle="-",
                            color=auxiliary_line_color,
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3"), color=auxiliary_line_color, fontsize=9)

    plt.annotate('the unknown $\\sigma$ ', xy=(15, 42), xytext=(40, 70),
                    arrowprops=dict(arrowstyle="-",
                            color=auxiliary_line_color,
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3"), color=auxiliary_line_color, fontsize=9)
    plt.annotate('the known $\\sigma$ ', xy=(40, 22), xytext=(60, 50),
                    arrowprops=dict(arrowstyle="-",
                            color=auxiliary_line_color,
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3"), color=auxiliary_line_color, fontsize=9
                            )

    plt.xlim(right=100, left=0)
    plt.ylim(top=110, bottom=0)
    plt.xlabel('Not pass rate(%)', fontsize=9, color=auxiliary_line_color)
    plt.ylabel('Acceptance rate(%)', fontsize=9, color=auxiliary_line_color)
    

    ticks = np.arange(0, 110, step=10)
    plt.xticks(ticks=ticks, color=auxiliary_line_color, fontsize=6)
    plt.yticks(ticks=ticks, color=auxiliary_line_color, fontsize=6)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(auxiliary_line_color)
    ax.spines['left'].set_color(auxiliary_line_color)

    plt.savefig(savefile)