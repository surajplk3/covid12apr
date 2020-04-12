# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:36:00 2020

@author: utpal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('IndividualDetails.csv', parse_dates=['date_announced'], dayfirst = True)

newdf = df['date_announced']
newdf = pd.DataFrame(newdf)

newdf.groupby(newdf['date_announced'].dt.month).count().plot(kind='bar')
plt.tight_layout()
plt.savefig('monthly_confirm.jpg', dpi =100)

newdf.groupby([newdf['date_announced'].dt.year, newdf['date_announced'].dt.month, newdf['date_announced'].dt.day]).count().plot(kind='bar')
plt.tight_layout()
plt.savefig('daily_confirm.jpg', dpi = 100)

fig = newdf.groupby(newdf['date_announced'].dt.date).count().plot(kind='bar')

