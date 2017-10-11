# Pandas : a labelled column oriented data

import pandas as pd

df = pd.DataFrame( { 	
			'label' : ['A', 'B', 'C', 'A', 'B', 'C'], 
			'value' : [1, 2, 3, 4, 5, 6] 
		} ) 
print df

print df['label']

print df['label'].str.lower()

print df['value'].sum()

print df.groupby('label').sum()

