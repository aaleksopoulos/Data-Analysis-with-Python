import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv", index_col='id')

#it is always a good idea to print something about the dataset
# print(df.head())
# print(df.info())

# Add 'overweight' column
def overweight (w, h):
    '''
        To calculate if a person is overweight, based on instructions
        returns 1 if bmi>25, 0 otherwise
    '''
    bmi = w/(h/100)**2
    return 1 if bmi>25 else 0

df['overweight'] = df.apply(lambda x :overweight(x['weight'], x['height']), axis=1)

#look the head of the df
# print(df.head())

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
for col in ['cholesterol', 'gluc']:
    df[col] = df.apply(lambda x : 0 if x[col]==1 else 1, axis=1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(by=['cardio', 'variable', 'value'], as_index=False).agg('size').rename(columns={'size': 'total'})
    
    # Draw the catplot with 'sns.catplot()'
    cat_fig = sns.catplot(data=df_cat, kind='bar', col='cardio', x='variable', y='total', hue='value')

    # Get the figure for the output
    fig = cat_fig.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))].reset_index()

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros(corr.shape)
    mask[np.triu_indices_from(mask)]=True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,6))

    # Draw the heatmap with 'sns.heatmap()'
    ax=sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig