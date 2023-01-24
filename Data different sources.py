import scipy
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("E:\\RIC\\Data.xlsx")
print(df)
print(df.head(2))
df.hist(column='X')
plt.show()
df.hist()
plt.show()
plt.plot()
df.to_excel("ProcessedData.xlsx", sheet_name = "ProcData")
df1 = pd.read_csv('E:\\RIC\\blood_pressure.csv')
print(df1)
print(df1.head(2))
