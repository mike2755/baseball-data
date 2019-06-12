import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

data = pd.read_excel('baseball-data/Teams.xlsx', sheetname = 'Sheet2')
data1 = pd.read_excel('baseball-data/Teams.xlsx', sheetname = 'Sheet3')
data2 = pd.read_excel('baseball-data/Revenue.xlsx', sheetname = 'Sheet2')

print(data.head())
