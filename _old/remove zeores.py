from statistics import median
import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np

df = pd.read_csv('/home/luiz/Documentos/faculdade/trabalho_ia/dataset.csv')
x = 0
while x <= 917:
    
    if df['CHOLESTEROL'][x] == 0:
       
        mean = df['CHOLESTEROL'].mean()   
        df.at[x,'CHOLESTEROL'] = mean
       
    x = x+1
    
df.to_csv('dataset_final.csv')
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("report_test_median.html")