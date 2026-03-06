import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    sea_lvl = pd.read_csv('epa-sea-level.csv')

    x = sea_lvl["Year"]
    y = sea_lvl["CSIRO Adjusted Sea Level"]

    fig, ax = plt.subplots()

    # Scatter plot of original data
    ax.scatter(x, y)

    # First line of best fit: all data extended to 2050
    result = linregress(x, y)
    x_extended = np.arange(x.min(), 2051)
    y_pred = result.intercept + result.slope * x_extended
    ax.plot(x_extended, y_pred)

    # Second line of best fit: data from 2000 extended to 2050
    x_2000 = x[x >= 2000]
    y_2000 = y[x >= 2000]
    result_2000 = linregress(x_2000, y_2000)
    x_extended_2000 = np.arange(2000, 2051)
    y_pred_2000 = result_2000.intercept + result_2000.slope * x_extended_2000
    ax.plot(x_extended_2000, y_pred_2000)

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()