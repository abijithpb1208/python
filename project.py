import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset =pd.read_csv("C:/Users/abiji/Downloads/Warehouse_and_Retail_Sales.csv")
print(dataset)
dataset.info()
res = sns.barplot(x='MONTH',y='RETAIL SALES',data=dataset)
plt.show()