from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
FILE_PATH = 'creditcard.csv'
df = pd.read_csv(FILE_PATH)
df.head()
value_counts_info = df.Class.value_counts()
print(value_counts_info)
ig, ax = plt.subplots(ncols=2,nrows=1)
ax1,ax2 = ax.flatten()
ax1.plot(value_counts_info)
ax2.plot(value_counts_info)
value_counts_info.plot(kind="bar")
plt.show()
value_counts_info.plot(kind="bar",logy=True)
plt.show()
df1 = df.query('Class == 1').V1
df0 = df.query('Class == 0').V1
plt.hist(df0, bins = 20)
num_bins = 20
dens = True
fig, ax = plt.subplots()
ax.hist(df0, num_bins, density = dens, color = 'lightgrey', alpha = 0.5, label = 'Class 0')
ax.hist(df1, num_bins, density = dens, color = 'red', alpha = 0.5, label = 'Class 1')
ax.set_xlabel('Class')
ax.legend()
plt.show()
