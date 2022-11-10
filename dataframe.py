import pandas as pd
from pandas_profiling import ProfileReport
from scipy.stats import entropy
import numpy as np

df = pd.read_csv('small_grocery.csv')

profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("your_report.html")