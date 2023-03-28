import pandas as pd
import os

pd.read_csv('data/rain_data_2015-12.csv', usecols=['Site', 'Date', 'Rainfall (mm)'])

from catchment import models

dataset = models.read_variable_from_csv('data/rain_data_2015-12.csv')

dataset.shape