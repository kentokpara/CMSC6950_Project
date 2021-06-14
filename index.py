# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# %%
from argopy import DataFetcher as ArgoDataFetcher
argo_loader = ArgoDataFetcher()


# %%
ds = argo_loader.region([-75, -45, 20, 30, 0, 10, '2018-01', '2018-06-30']).to_xarray()
ds_1 = argo_loader.region([-75, -45, 20, 30, 0, 10, '2018-07', '2019-01-01']).to_xarray()


# %%
#ds = ArgoDataFetcher().profile(6902746, 30).to_xarray()
df = ds.to_dataframe()


# %%
df_1 = ds_1.to_dataframe()


# %%
df['TIME']= pd.to_datetime(df['TIME'])


# %%
df_1['TIME']= pd.to_datetime(df_1['TIME'])


# %%
Temp = df['TEMP']
Time = df['TIME']
fig, ax = plt.subplots(figsize =(20,7))
plt.plot(Time, Temp)
ax.set_xlabel('Time')
ax.set_ylabel('Temperature')
ax.set_title('Time Vs Temperature - JAN TO JUN')
ax.grid()
plt.savefig('JAN_JUN.png')


# %%
Temp_1 = df_1['TEMP']
Time_1 = df_1['TIME']
fig1, ax1 = plt.subplots(figsize =(20,7))
plt.plot(Time_1, Temp_1)
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature')
ax1.set_title('Time Vs Temperature - JUL - DEC')
ax1.grid()
plt.savefig('JUL_DEC.png')


