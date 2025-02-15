import numpy as np
import pandas as pd

arr_2d = np.array([[1,2,3],[1,2,3]])
print(arr_2d)

element = arr_2d[1,2]
print(element)

dimension = arr_2d.ndim
print(dimension)

arr_size = arr_2d.size
print(arr_size)

products = ['orange','bana','apple','pear']
sales =  [120, 40, 70, 60]

product_series = pd.series(sales, index=products)

total_sales = sales_series.sum()

best_selling_product = sales_series.idxmax()

print(f"best selling product{best_selling_product}")