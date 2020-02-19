import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_1.dat', delimiter='\t', names=['Time', 'Voltage', 'Current', 'Power'])


x = list(range(len(df['Time'])))

pLine = plt.plot(x, df['Power'], label='Power in W')
uLine = plt.plot(x, df['Voltage'], label='Voltage in V')
iLine = plt.plot(x, df['Current'], label='Current in A')
plt.legend(frameon=False)
#ax.legend(loc='upper left', frameon=False)
#plt.grid(True)
plt.title('Batterieladung')
plt.xlabel('Time in s')

plt.show()


""""""""""
plt.plot(df['Time'], df['Power'])
plt.plot(df['Time'], df['Voltage'])
plt.plot(df['Time'], df['Current'])
plt.show()
"""""""""
