import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x_data = np.array([34.0, 35.5, 36.7, 37.8, 38.6])
y_data = np.array([34.2, 35.8, 37.0, 38.1, 38.8])

slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
