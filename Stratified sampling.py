import pandas as pd # python's library for data manipulation and preprocessing
import numpy as np # python's library for number crunching
import matplotlib # python's library for visualisation
import matplotlib.pyplot as plt
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
import seaborn as sns # also python's library for visualisations
color = sns.color_palette()
sns.set_style('darkgrid')
import sklearn #python's machine learning library
from sklearn.model_selection import train_test_split
housing = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\MSc\\RIC\\RICFiles (1)\\housing.csv') # reading the data into a pandas dataframe
print("First 5 rowa")
print(housing.head())# calling the first five rows of the dataset
print("exploratory analysis")
print(housing.info()) # exploratory analysis
correlation_matrix = housing.corr() #creating a heatmap of the attributes in the dataset
plt.subplots(figsize=(8,6))
sns.heatmap(correlation_matrix, center=0, annot=True, linewidths=.3)
plt.show()
corr = housing.corr() # showing correlations by target variable
print(corr['median_house_value'].sort_values(ascending=False))
sns.distplot(housing.median_income) # showing the distribution of the median_income variable in the dataset
plt.show() # check the distplot params though. see how you can make it prettier
# Divide by 1.5 to limit the number of income categories
housing["median_income_category"] = np.ceil(housing["median_income"] / 1.5)
# showing the frequency of each category
housing.median_income_category.value_counts().sort_index()
housing["median_income_category"].where(housing["median_income_category"] < 5, 5.0, inplace=True)
housing.median_income_category.value_counts().sort_index()
from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["median_income_category"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
    print(strat_test_set.head())
def income_cat_props(data):
    return data['median_income_category'].value_counts() / len(data)
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
compare_props = pd.DataFrame({
"Overall": income_cat_props(housing),
"Stratified": income_cat_props(strat_test_set),
"Random": income_cat_props(test_set),
}).sort_index()
compare_props["Rand. %error"] = 100 * compare_props["Random"] / compare_props["Overall"] - 100
compare_props["Strat. %error"] = 100 * compare_props["Stratified"] / compare_props["Overall"] - 100
compare_props
print("final op")
print (compare_props)
