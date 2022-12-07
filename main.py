#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:53:14 2022

@author: nabiki
"""

# dataframes 
import pandas as pd

# plotting 
import matplotlib.pylab as plt
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

# math operations 
import numpy as np

#%% Generate a dataframe with random values
# random generator object
rng = np.random.default_rng(seed=1)

# Generate two variables 
x = np.linspace(0,100,num=101)
y = rng.random(101) * 50 # generate 100 random values with max value of 100
z = rng.random(101) * 100 # generate 100 random values with max value of 100


#create dataframe
dict_features = {'x':x, 'y':y, 'z' : z}
df = pd.DataFrame(dict_features)
print(df.head(10))

# save dataframe

df.to_csv("my_dataframe.csv", index=False)


#%% Plot data frame

# load dataframe
df = pd.read_csv("./my_dataframe.csv")

plt.plot(df['x'], df['y'])
# plt.scatter(df['x'], df['y'])
plt.title("Random x and y variables")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.savefig("./random x and y plot.png")
plt.show() # this flushes buffer, save before showing your figure

#%% multiple data on the same plot 

df = pd.read_csv("./my_dataframe.csv")

plt.plot(df['x'], df['y'], label='y data')
plt.plot(df['x'], df['z'], label='z data')
plt.title("Random y and z variables")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.savefig("./random y and z data plot.png")
plt.show() # this flushes buffer, save before showing your figure


