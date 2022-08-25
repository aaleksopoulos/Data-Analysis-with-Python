import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # print(df.tail())
    x_min = df['Year'].min()

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)

    # Create first line of best fit
    res1 = linregress(x, y)
    x1 = range(x_min, 2051)
    y1 = [res1.slope*i + res1.intercept for i in x1]

    plt.plot(x1, y1, color='green')
    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    
    x2 = range(df2['Year'].min(), 2051)
    y2 = [res2.slope*i + res2.intercept for i in x2]
    
    plt.plot(x2, y2, color='red')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()