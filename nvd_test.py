import json
import pandas as pd
pd.set_option('display.width', 800)
pd.set_option('display.max_columns', 50)

# Load a shorter version of the data
your_path = 'c://demo/' #C:\Python\active state\nvd
nvd_file = 'nvd_clean2.json'
with open(nvd_file) as json_file:
    data = json.load(json_file)
    print(data)
cve_df = pd.DataFrame


# Figue out how to get to each data element
print(data[0]['cve']['CVE_data_meta']['ID'])
print(data[0]['cve']['CVE_data_meta']['ID'],data[0]['cve']['CVE_data_meta']['ASSIGNER'])
print(data[0]['cve']['description']['description_data'][0]['value'])
print(data[0]['cve']['description']['description_data'][0]['value'])
print(data[0]['cve']['references']['reference_data'][0]['url'])
print(data[0]['cve']['references']['reference_data'][0]['refsource'])

# todo- Loop over the json oblect and pull required fields





