#! /usr/bin/env python3

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from datasense import Xbar, R

chart_data = pd.read_csv(Path(__file__).parent / 'xbarr.csv',
                         index_col='Sample').iloc[:, 0:]
xbar = Xbar(chart_data)
print('Xbar chart')
print('Upper control limit', xbar.ucl, sep=' = ')
print('Average moving range', xbar.mean, sep=' = ')
print('Lower control limit', xbar.lcl, sep=' = ')
print(f'Sigma(Xbar)', xbar.sigma, sep=' = ')
for i in range(-3, 4):
    print(f'{i} Sigma', ' '.join(map(str, [xbar.sigmas[i]])), sep=' = ')
ax1 = xbar.ax
ax1.set_title('Xbar control chart' + '\n' 'Subtitle')
ax1.set_ylabel('Response (units)')
ax1.set_xlabel('X axis label')
plt.show()
#plt.clf()
mr = mR(chart_data)
print('mR chart')
print('Upper control limit', mr.ucl, sep=' = ')
print('Average moving range', mr.mean, sep=' = ')
print('Lower control limit', mr.lcl, sep=' = ')
print(f'Sigma(X)', mr.sigma, sep=' = ')
for i in range(-3, 4):
    print(f'{i} Sigma', ' '.join(map(str, [mr.sigmas[i]])), sep=' = ')
ax2 = mr.ax
ax2.set_title('mR control chart' + '\n' 'Subtitle')
ax2.set_ylabel('Response (units)')
ax2.set_xlabel('X axis label')
plt.show()
#plt.clf()
