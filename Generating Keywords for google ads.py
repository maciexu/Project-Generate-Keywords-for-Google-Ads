# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:09:17 2019

@author: mengx
"""

# Project: Generate Keywords for Google Ads

# List of words to pair with products
words =['buy', 'price', 'discount', 'promotion', 'promo', 'shop']

# Print list of words
# ... YOUR CODE FOR TASK 1 ...
print(words)

products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        #keywords_list.append([word + ' ' + product])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)


# Load library
# ... YOUR CODE FOR TASK 3 ...
import pandas as pd
# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it
# ... YOUR CODE FOR TASK 3 ...
keywords_df.head()

# Rename the columns of the DataFrame
keywords_df.columns=["Ad Group", "Keyword"]


# Add a campaign column
# ... YOUR CODE FOR TASK 5 ...
keywords_df['Campaign']='SEM_Sofas'
keywords_df['Criterion Type']='Exact'


# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
# ... YOUR CODE FOR TASK 7 ...
keywords_phrase['Criterion Type']='Phrase'

# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)

# Save the final keywords to a CSV file
# ... YOUR CODE FOR TASK 8 ... 
keywords_df_final.to_csv('keywords.csv', index=False)

# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)






