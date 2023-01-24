from scipy.stats import ttest_1samp
import numpy as np
ages = np.genfromtxt('C:\\Users\\Saad\\Desktop\\RIC\\ages.csv')
print(ages)
ages_mean = np.mean(ages)
print("Actual Average of our data: ")
print(ages_mean)
muavg=30
print("In null hypothesis we assume the average to be:")
print(muavg)
tset, pval = ttest_1samp(ages, muavg)
print('p-values == ',pval)
if pval< 0.05: # alpha value is 0.05
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
