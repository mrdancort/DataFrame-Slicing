# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 17:56:23 2022

@author: Daniel Cortez
"""
# 1. Make the Pandas library available for use in your script.

import pandas as pd 

# 2. Read in the specified input file (codingInput.csv) and create a DataFrame 
# object based on the input.

myDataFrame = pd.read_csv('codingInput.csv')

# 3. Print columns val30, val07, val23, and val01 (in the order listed) from 
# the 217th row of data (according to Excel) in the DataFrame.

print( myDataFrame.loc [ 215: 215, ('val30', 'val07', 'val23', 'val01') ] )

# 4. Print the values in column val15 for 8 rows beginning with the 156th row 
# of data (according to Excel).

print( myDataFrame.loc [ 154 : 161, 'val15'] )

# 5. Print the sum of all values in column val11. You may not use an iteration 
# for this task.

print( myDataFrame['val11'].sum())

# 6. Print the variance of all values in row 204 (according to Excel). 
# Your result should display four decimal positions. 
# (Expected result: 79679.7483) 

print("Variance is %.4f" %       
      myDataFrame.loc[202].var())

# 7. Create a persistent view of rows 30 – 70 (according to Excel). 
# Include columns val06 through (including) val15. 
# Your view should have 40 rows and 10 columns. 

pView = myDataFrame.iloc[ 28 : 68, 5 : 15 ]

# 8. Create a new DataFrame object. This new object will hold all columns 
# from rows 82 - 231 (inclusive and according to Excel). Your new DataFrame 
# should have 150 rows and 30 columns.
# Print the entire (no ellipses…) DataFrame to the console using a temporary 
# override of the environmental variables that limit output.

newDf = pd.DataFrame(myDataFrame.iloc[ 80 : 230 ])
with pd.option_context( 'display.max_rows',    None,
                        'display.max_columns', None ):
    print( newDf ) 
    
