import requests
import re
#mport zipfile
import io
import json
import csv
import uuid
import pandas as pd
pd.set_option('display.width', 800)
pd.set_option('display.max_columns', 10)
import torch


#create fake cve data for testing to mirror import of actual json
cve_data = {'cve_ID': ['cve-1', 'cve-2', 'cve-3', 'cve-4'],
        'severity': [21, 19, 20, 18],
        'product': ['excel v 3.2', 'word v-193', 'GOLANG3.1', 'RUBY-21'],
        'Percentage': [88, 92, 95, 70]}

# create fake pull from endpoint to get customers to mirror import of actual json
customer = {'ID': ['comany1', 'company2', 'company3', 'company4'],
        'product': ['excel v 3.2', 'word v-193', 'python', 'RUBY-21'], }
print('printing customer')
print(customer)

# # Convert the dictionary into DataFrame
cve_df = pd.DataFrame(cve_data, columns=['cve_ID', 'severity', 'product', 'Percentage','cve_guid'])
# adding customer dataframe
cs_df = pd.DataFrame(customer, columns=['cs_ID', 'product','cs_guid'])

#print("Given Dataframe :\n", cve_df)

for ind in cve_df.index:
    print(cve_df['cve_ID'][ind], cve_df['product'][ind], cve_df['cve_guid'][ind])

# add the guid for the cve
for index_label, row_series in cve_df.iterrows():
    cve_df.at[index_label, 'cve_guid'] = row_series['cve_guid'] =uuid.uuid4()
# print('new guid should be cve_guid')
for ind in cve_df.index:
    print(cve_df['cve_ID'][ind], cve_df['product'][ind], cve_df['cve_guid'][ind])

# add guid for customer
for index_label, row_series in cs_df.iterrows():
    cs_df.at[index_label, 'cs_guid'] = row_series['cs_guid'] =uuid.uuid4()
# print('new guid for  customer should say cs_guid')
# for ind in cs_df.index:
#     print(cs_df['cs_ID'][ind], cs_df['product'][ind], cs_df['cs_guid'][ind])

print(cve_data)
# merging the two data frames
merged_inner_df = pd.merge(left=cve_df, right=cs_df, left_on='product', right_on='product')
print('merged')
print(merged_inner_df)

# Import cve data from file

your_path = 'c://demo/' #C:\Python\active state\nvd
nvd_file = 'nvd_clean.json'
with open(nvd_file) as json_file:
    data = json.load(json_file)


your_path = 'c://demo/' #C:\Python\active state\nvd
nvd_file = 'nvd_clean.json'
with open(nvd_file) as json_file:
    data = json.load(json_file)
    print(data)

# see nvd_test.py for me trying to learn to access nested data elements






