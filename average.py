import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
a = pd.read_csv('attendance.csv')
b=a[['Name']+['Status']]
print(b)