# vertically

'''
import csv

# Read 0001.csv and store its rows in a list
data_0001 = []
with open('0001.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data_0001.append(row)

# Read 0002.csv and store its rows in a list
data_0002 = []
with open('0002.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data_0002.append(row)

# Combine the data horizontally
combined_data = []
for i in range(len(data_0001)):
    combined_row = data_0001[i] + data_0002[i]
    combined_data.append(combined_row)

# Save the combined data as 0003.csv
with open('0003.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(combined_data)
'''




# horizontally
'''
import csv

# Read 0001.csv and store its rows in a list
data_0001 = []
with open('0001.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data_0001.append(row)

# Read 0002.csv and append its rows to the existing list
with open('0002.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data_0001.append(row)

# Save the combined data as 0003.csv
with open('0003.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data_0001)
'''



# Remove headers
'''
import csv

# Read 0001.csv and store its rows in a list
data_0001 = []
with open('0001.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data_0001.append(row)

# Read 0002.csv and store its rows in a list (excluding the header)
data_0002 = []
with open('0002.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        data_0002.append(row)

# Combine the data vertically
combined_data = data_0001 + data_0002

# Save the combined data as 0003.csv
with open('0003.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(combined_data)
'''





# add first column as 1-st from another file
# right outer join
'''
import pandas as pd

# Read 0003.csv into a pandas DataFrame
df_0003 = pd.read_csv('0003.csv')

# Read output_0.csv into a pandas DataFrame with only the 'lang' column
df_lang = pd.read_csv('output_0.csv', usecols=['lang'])

# Perform a left outer join on the DataFrames
df_result = df_0003.merge(df_lang, how='left', left_index=True, right_index=True)

# Save the result as 0004.csv
df_result.to_csv('0004.csv', index=False)
'''






# left outer join (lang)
'''
import pandas as pd

# Read 0003.csv into a pandas DataFrame
df_0003 = pd.read_csv('0003.csv')

# Read output_0.csv into a pandas DataFrame with only the 'lang' column
df_lang = pd.read_csv('output_0.csv', usecols=['lang'])

# Perform a left outer join on the DataFrames with 'lang' on the left side
df_result = df_lang.merge(df_0003, how='left', left_index=True, right_index=True)

# Save the result as 0004.csv
df_result.to_csv('0004.csv', index=False)
'''





# left outer join (index)
'''
import pandas as pd

# Read 0003.csv into a pandas DataFrame
df_0003 = pd.read_csv('0003.csv')

# Read output_0.csv into a pandas DataFrame with only the 'lang' column
df_lang = pd.read_csv('output_0.csv', usecols=['index'])

# Perform a left outer join on the DataFrames with 'lang' on the left side
df_result = df_lang.merge(df_0003, how='left', left_index=True, right_index=True)

# Save the result as 0004.csv
df_result.to_csv('0004.csv', index=False)
'''





# remove column
'''
import pandas as pd

# Read 0004.csv into a pandas DataFrame
df_0004 = pd.read_csv('0004.csv')

# Remove the 'index_y' column
df_0004.drop('index_y', axis=1, inplace=True)

# Save the modified DataFrame as 0005.csv
df_0004.to_csv('0005.csv', index=False)
'''





# rename the column
import pandas as pd

# Read the CSV file
df = pd.read_csv('0005.csv')

# Rename the column
df = df.rename(columns={'index_x': 'index'})

# Save the updated DataFrame to a new CSV file
df.to_csv('0006.csv', index=False)