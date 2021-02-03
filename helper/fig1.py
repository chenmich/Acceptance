import pandas as pd
import numpy as np
from scipy.stats import norm 
from matplotlib  import pyplot as plt

fig_point = 100

lot_mu = 0
another_lot_mu = 10
sample_mu = lot_mu
sample_sigma = 3

lot_range = 4
sample_range = 8

auxiliary_line_color = '#9f9f9f'
data_line_color = '#4f4f4f'
fill_color = '#bfbfbf'

title_fontsize = 18

def draw_variable_sample(savefile):
    fig_point = 100

    lot_mu = 0
    another_lot_mu = 10
    sample_mu = lot_mu
    sample_sigma = 3

    lot_range = 4
    sample_range = 8
    fig, ax = plt.subplots(1, 1)

    lot_x = np.linspace(lot_mu - lot_range, lot_mu + lot_range, fig_point)
    lot_y = norm.pdf(lot_x)

    k = 4.0
    fill_start = lot_x[0]
    fill_x = np.linspace(fill_start, k, 100) 
    fill_y = norm.pdf(fill_x, loc=another_lot_mu, scale=sample_sigma)

    sample_x = np.linspace(sample_mu - sample_range, 
                            sample_mu + sample_range, fig_point)
    sample_y = norm.pdf(sample_x, scale=sample_sigma)

    not_fill_x_end = sample_x[-1]
    not_fill_x = np.linspace(k, not_fill_x_end, 100)
    not_fill_y = norm.pdf(not_fill_x, loc=lot_mu, scale=sample_sigma)

    ax.plot(lot_x, lot_y, color=data_line_color)
    ax.plot(sample_x, sample_y, color=data_line_color)
    ax.plot(lot_x + another_lot_mu, lot_y, color=data_line_color)
    ax.plot(sample_x + another_lot_mu, sample_y, color=data_line_color)

    ax.vlines(k,  0,  0.3, color=auxiliary_line_color)
    ax.vlines(-6, 0, 0.3, color=auxiliary_line_color)
    ax.hlines(0, -10, 20, color=auxiliary_line_color)
    ax.fill_between(fill_x, fill_y, facecolor=fill_color)
    ax.fill_between(not_fill_x, not_fill_y, facecolor=fill_color)
    
    ax.set_title('Variable sample', fontsize=title_fontsize, color=auxiliary_line_color)
    
    ax.annotate('$k\\sigma$', xy=(k, 0.15), xytext=(7, 0.25),
                arrowprops=dict(arrowstyle="-",
                            color=auxiliary_line_color,
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3"), color=auxiliary_line_color, fontsize=9)
    ax.annotate('L', xy=(-6, 0.15), xytext=(-3.5, 0.25),
                arrowprops=dict(arrowstyle="-",
                            color=auxiliary_line_color,
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3"), color=auxiliary_line_color, fontsize=9)
    ax.annotate('$\\alpha$', xy=(3.5, 0.01), xytext=(1.0, -0.05),
                arrowprops=dict(arrowstyle="-",
                            color=auxiliary_line_color,
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3"), color=auxiliary_line_color, fontsize=9)
    ax.annotate('$\\beta$', xy=(5.5, 0.01), xytext=(8.5, -0.05),
                arrowprops=dict(arrowstyle="-",
                            color=auxiliary_line_color,
                            patchB=None,
                            shrinkB=0,
                            connectionstyle='arc3, rad=0.3'), color=auxiliary_line_color, fontsize=9)

    ax.vlines(0, 0, 0.45, color=auxiliary_line_color)
    ax.vlines(10, 0, 0.45, color=auxiliary_line_color)
    ax.set_xlim(-10)
    ax.set_ylim(-0.06)
    ax.axis('off')
    plt.savefig(savefile)
