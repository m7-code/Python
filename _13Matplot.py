
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)  # 1000 points from 0 to 10
y = np.sin(x)                 # sine of each point

plt.plot(x, y)                 # create line plot
plt.title("Sine Wave")         # optional title
plt.xlabel("x")                # label for x-axis
plt.ylabel("sin(x)")           # label for y-axis
plt.grid(True)                  # add grid for better reading
plt.show()                      # display the plot

                                     #Seaborn

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  # Needed for plt.show()

# SAMPLE DATA 
df = pd.DataFrame({
    'Category': [1, 2, 3, 4, 5, 6, 7, 8],
    'Value': [10, 15, 7, 12, 14, 9, 11, 13],
    'Score': [8, 6, 9, 7, 6, 8, 7, 9]
})

# GLOBAL STYLE 
sns.set_style("whitegrid")  # Styles: white, dark, whitegrid, darkgrid, ticks
sns.set_palette("coolwarm")  # Color theme

# LINE PLOT 
sns.lineplot(data=df, x='Value', y='Score')
plt.title("Line Plot")
plt.show()

# SCATTER PLOT 
sns.scatterplot(data=df, x='Value', y='Score', hue='Category', size='Score')
plt.title("Scatter Plot")
plt.show()

# BAR PLOT 
sns.barplot(data=df, x='Category', y='Value')
plt.title("Bar Plot")
plt.show()

# COUNT PLOT 
sns.countplot(data=df, x='Category')
plt.title("Count Plot")
plt.show()

# HISTOGRAM 
sns.histplot(data=df, x='Value', bins=5, kde=True)
plt.title("Histogram")
plt.show()

# KDE PLOT 
sns.kdeplot(data=df, x='Value', fill=True)
plt.title("KDE Plot")
plt.show()

# BOX PLOT 
sns.boxplot(data=df, x='Category', y='Value')
plt.title("Box Plot")
plt.show()

# VIOLIN PLOT 
sns.violinplot(data=df, x='Category', y='Value')
plt.title("Violin Plot")
plt.show()

# HEATMAP 
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()

# PAIR PLOT 
sns.pairplot(df, hue="Category")
plt.suptitle("Pair Plot", y=1.02)  # Title slightly above
plt.show()

                           
