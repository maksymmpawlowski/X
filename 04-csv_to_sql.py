


'''
import csv
import pymysql

file_path = 'reviews.csv'
table_name = 'reviews2'

# Establish a connection to the MySQL database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Me6111111',
                             database='chicago_airbnb')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Read the CSV file and get the column names from the header row
with open(file_path, 'r', encoding='utf-8') as file:
    csv_data = list(csv.reader(file))
csv_header = csv_data[0]
column_names = [column.strip() for column in csv_header]

# Generate the SQL statement to create the table
sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for column_name in column_names:
    sql_create_table += f"`{column_name}` VARCHAR(255), "  # Assuming VARCHAR(255) for all columns
sql_create_table = sql_create_table.rstrip(', ') + ");"

# Create the table
cursor.execute(sql_create_table)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("New table created successfully.")'''

'''
import csv
import pymysql

file_path = 'reviews.csv'
table_name = 'reviews2'

# Establish a connection to the MySQL database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Me6111111',
                             database='chicago_airbnb')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Read the CSV file and get the column names from the header row
with open(file_path, 'r', encoding='utf-8') as file:
    csv_data = list(csv.reader(file))
csv_header = csv_data[0]
column_names = [column.strip() for column in csv_header]

# Generate the SQL statement to create the table
sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for column_name in column_names:
    if column_name == 'comments':
        sql_create_table += f"`{column_name}` LONGTEXT, "  # Use LONGTEXT data type for the 'comments' column
    else:
        sql_create_table += f"`{column_name}` VARCHAR(255), "  # Assuming VARCHAR(255) for other columns
sql_create_table = sql_create_table.rstrip(', ') + ");"

# Create the table
cursor.execute(sql_create_table)

# Prepare the SQL statement to insert data into the table
sql_insert_data = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(column_names))})"

# Remove the header row before inserting data
csv_data = csv_data[1:]

# Insert data into the table
cursor.executemany(sql_insert_data, csv_data)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Table created and data inserted successfully.")
'''







'''
import csv
import pymysql
import os

file_path = 'reviews.csv'
table_name = os.path.splitext(os.path.basename(file_path))[0]

# Establish a connection to the MySQL database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Me6111111',
                             database='chicago_airbnb')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Read the CSV file and get the column names from the header row
with open(file_path, 'r', encoding='utf-8') as file:
    csv_data = list(csv.reader(file))
csv_header = csv_data[0]
column_names = [column.strip() for column in csv_header]

# Generate the SQL statement to create the table
sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for column_name in column_names:
    if column_name == 'comments':
        sql_create_table += f"`{column_name}` LONGTEXT, "  # Use LONGTEXT data type for the 'comments' column
    else:
        sql_create_table += f"`{column_name}` VARCHAR(255), "  # Assuming VARCHAR(255) for other columns
sql_create_table = sql_create_table.rstrip(', ') + ");"

# Create the table
cursor.execute(sql_create_table)

# Prepare the SQL statement to insert data into the table
sql_insert_data = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(column_names))})"

# Remove the header row before inserting data
csv_data = csv_data[1:]

# Insert data into the table
cursor.executemany(sql_insert_data, csv_data)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()

print("Table created and data inserted successfully.")
'''

# count nulls
'''
import csv

file_path = 'reviews.csv'
empty_cell_count = 0

# Open the CSV file and iterate over its rows
with open(file_path, 'r', encoding='utf-8') as file:
    csv_data = csv.reader(file)
    header = next(csv_data)  # Skip the header row
    for row in csv_data:
        for cell in row:
            if not cell.strip():  # Check if cell is empty or contains only whitespace
                empty_cell_count += 1

print(f"Number of empty cells in {file_path}: {empty_cell_count}")
'''





import csv
import pymysql
import os

file_path = 'reviews.csv'
table_name = os.path.splitext(os.path.basename(file_path))[0]

# Establish a connection to the MySQL database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Me6111111',
                             database='chicago_airbnb')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Read the CSV file and get the column names from the header row
with open(file_path, 'r', encoding='utf-8') as file:
    csv_data = list(csv.reader(file))
csv_header = csv_data[0]
column_names = [column.strip() for column in csv_header]

# Generate the SQL statement to create the table
sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for column_name in column_names:
    if column_name == 'comments':
        sql_create_table += f"`{column_name}` LONGTEXT, "  # Use LONGTEXT data type for the 'comments' column
    else:
        sql_create_table += f"`{column_name}` VARCHAR(255), "  # Assuming VARCHAR(255) for other columns
sql_create_table = sql_create_table.rstrip(', ') + ");"

# Create the table
cursor.execute(sql_create_table)

# Prepare the SQL statement to insert data into the table
sql_insert_data = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(column_names))})"

# Remove the header row before inserting data
csv_data = csv_data[1:]

# Insert data into the table
cursor.executemany(sql_insert_data, csv_data)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()
