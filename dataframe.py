import pandas as pd
from pandas_profiling import ProfileReport
from scipy.stats import entropy
import numpy as np

df = pd.read_csv("Trabalho_IA\data\large_grocery.csv",delimiter=";")

profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("large_report.html")