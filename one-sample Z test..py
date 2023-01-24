from statsmodels.stats import weightstats as stests
import pandas as pd
from scipy import stats
df = pd.read_csv("C:\\Users\\Saad\\Desktop\\RIC\\blood_pressure.csv")
df[['bp_before','bp_after']].describe()
print(df)
ztest ,pval = stests.ztest(df['bp_before'], x2=None, value=156)
print('p-values == ',float(pval))
print('p-values == ',pval)
if pval<0.05:
 print("reject null hypothesis")
else:
 print("accept null hypothesis")


#Null hypothesis: No difference.
#Alternate hypothesis: There is a significant difference.
#p-value: 0.66516
#Condition: p-value is less than alpha-value we'd reject the null hypothesis, else accept
#Result: Accept null hypothesis.
