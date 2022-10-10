# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:58:46 2021

@author: marce
"""

import pandas as pd
import seaborn as sns
path = r'C:\Users\marce\Documents\stress_minus_rewards_plot.csv'
df_robs = pd.read_csv(path)

df_robs=df_robs.values

sns.clustermap(df_robs,method='complete',metric='euclidean',cmap='Spectral',vmin=0, vmax=15)

