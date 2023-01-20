import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col=0, parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(17,7))
    plt.plot(df['value'])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    from calendar import month_name
    months = month_name[1:]
    df_bar = df.copy()
    df_bar['months'] = pd.Categorical(df_bar.index.strftime('%B'), categories=months, ordered=True)
    dfp = pd.pivot_table(data=df_bar, index=pd.DatetimeIndex(df_bar.index).year, columns='months', values='value')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,4))
    bar_plot = dfp.plot(kind='bar', ylabel='Average Page Views', xlabel='Years', rot=0, ax=ax)
    _ = bar_plot.legend(bbox_to_anchor=(1, 1.02), loc='upper left')



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    x = df_box['month'].unique()
    y = list(x[8:]) + list(x[:8])
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(19,8))
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    sns.boxplot(data=df_box, x='month', y='value', ax=ax2, order=y)
    ax1.set(xlabel='Year', ylabel='Page Views')
    ax2.set(xlabel='Month', ylabel='Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
