# -*- coding: utf-8 -*-
import pandas as pd
#https://thispointer.com/pandas-sort-rows-or-columns-in-dataframe-based-on-values-using-dataframe-sort_values/
#df creation
matrix = [(222, 16, 23),(333, 31, 11)(444, 34, 11),   ]
matrix 
# Create a DataFrame object of 3X3 Matrix
dfObj = pd.DataFrame(matrix, index=list('abc'))
dfObj
dfObj.sort_values(by='b', axis=1)
dfObj.sort_values(by='b', axis=1, ascending=False)
