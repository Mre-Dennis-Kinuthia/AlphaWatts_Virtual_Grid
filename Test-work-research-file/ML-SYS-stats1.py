#!/usr/bin/env python3
#simple ML sys
import numpy as np
from scipy import stats

data = [20, 21, 32, 33, 44, 41, 20, 20, 90, 80, 39, 89, 100]
x = np.mean(data)
print("MEAN", x)

y = np.median(data)
print("MEDIAN", y)

z = stats.mode(data, keepdims=True)
print("MODE", z)

a = np.std(data)
print("Standard Deviation", a)

b = np.var(data)
print("Variance", b)

c = np.percentile(data, 90)
print("Percentile", c)