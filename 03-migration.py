'''
import mysql.connector
import pandas as pd

def display_reviews(num_rows):
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Me6111111",
        database="chicago_airbnb"
    )
    cursor = conn.cursor()

    # Retrieve the desired columns from the reviews2 table
    query = f"SELECT `index`, `comments` FROM reviews2 LIMIT {num_rows};"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Create a dataframe from the rows
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)

    # Display the dataframe
    print(df)

    # Close the connection
    conn.close()

# Call the function to display 100 rows as a dataframe
display_reviews(num_rows=100)
'''


#migration of the values from one column of one table to another
'''
import mysql.connector

def transfer_data(host, user, password, db_name, table1_name, table1_column, table2_name, table2_column, num_rows):
    # Connect to the database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = conn.cursor()

    # Retrieve the rows from the first table column
    query = f"SELECT `{table1_column}` FROM {table1_name} LIMIT {num_rows};"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Insert the rows into the second table column
    for i, row in enumerate(rows, 1):
        value = row[0]  # Assuming the first table column contains a single value
        insert_query = f"INSERT INTO {table2_name} (`{table2_column}`) VALUES (%s);"
        cursor.execute(insert_query, (value,))

        # Save changes after every 100 rows
        if i % 100 == 0:
            conn.commit()

    # Save any remaining changes
    conn.commit()

    # Close the connection
    conn.close()

# Example usage:
transfer_data("localhost", "root", "Me6111111", "chicago_airbnb", "reviews2", "index", "reviews_translations", "index", 1000)
'''






#the same but omitting ones where primary key is the same
'''
import mysql.connector

def transfer_data(host, user, password, db_name, table1_name, table1_column, table2_name, table2_column, num_rows):
    # Connect to the database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = conn.cursor()

    # Retrieve the rows from the first table column
    query = f"SELECT `{table1_column}` FROM {table1_name} LIMIT {num_rows};"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Insert the rows into the second table column
    for i, row in enumerate(rows, 1):
        value = row[0]  # Assuming the first table column contains a single value
        insert_query = f"INSERT IGNORE INTO {table2_name} (`{table2_column}`) VALUES (%s);"
        cursor.execute(insert_query, (value,))

        # Save changes after every 100 rows
        if i % 100 == 0:
            conn.commit()

    # Save any remaining changes
    conn.commit()

    # Close the connection
    conn.close()

# Example usage:
transfer_data("localhost", "root", "Me6111111", "chicago_airbnb", "reviews2", "index", "reviews_translations", "index", 1000)
'''







'''
import mysql.connector

def transfer_data(host, user, password, db_name, table1_name, table1_column, table2_name, table2_column, num_rows, additional_columns1=None, additional_columns2=None):
    # Connect to the database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = conn.cursor()

    # Construct the SELECT query based on the additional columns
    if additional_columns1 and additional_columns2:
        additional_columns1_str = ", ".join([f"`{col}`" for col in additional_columns1])
        additional_columns2_str = ", ".join([f"`{col}`" for col in additional_columns2])
        query = f"SELECT `{table1_column}`, {additional_columns1_str} FROM {table1_name} LIMIT {num_rows};"
    else:
        query = f"SELECT `{table1_column}` FROM {table1_name} LIMIT {num_rows};"

    # Retrieve the rows from the first table columns
    cursor.execute(query)
    rows = cursor.fetchall()

    # Construct the INSERT query based on the additional columns
    if additional_columns2:
        additional_columns2_str = ", ".join([f"`{col}`" for col in additional_columns2])
        insert_query = f"INSERT IGNORE INTO {table2_name} (`{table2_column}`, {additional_columns2_str}) VALUES (%s{', %s' * len(additional_columns2)});"
    else:
        insert_query = f"INSERT IGNORE INTO {table2_name} (`{table2_column}`) VALUES (%s);"

    # Insert the rows into the second table columns
    for i, row in enumerate(rows, 1):
        values = [row[0]]  # Assuming the first table column contains a single value
        values.extend(row[1:])  # Additional column values if provided

        cursor.execute(insert_query, tuple(values))

        # Save changes after every 100 rows
        if i % 100 == 0:
            conn.commit()

    # Save any remaining changes
    conn.commit()

    # Close the connection
    conn.close()

# Example usage:
transfer_data("localhost", "root", "Me6111111", "chicago_airbnb", "reviews2", "index", "reviews_translations", "index", 1000)'''

'''
Each pair of column arguments represents a mapping between a column in the first table and a corresponding column in the second table, 
and if a single column argument is provided without its corresponding pair, an error should be returned stating to add the target column.
The function should accept the following arguments: SQL database name, name of the first table, name of the second table, pairs of columns 
representing mappings between the first and second tables (each pair consisting of a column from the first table and its corresponding column 
in the second table), number of rows for the operation, 
and optional additional column pairs (representing additional mappings between the tables).
host = "localhost"
user = "root"
password = "your_password"
database = "your_database"
table1 = "your_table1"
table2 = "your_table2"
column_pairs = [("column1_table1", "column1_table2")]
num_rows = 1000
additional_column_pairs = [("column2_table1", "column2_table2")]

transfer_data(host, user, password, database, table1, table2, column_pairs, num_rows, *additional_column_pairs)
'''




'''
import mysql.connector

def transfer_data(host, user, password, database, table1, table2, column_pairs, num_rows, *additional_column_pairs):
    # Establish connection to MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()

    try:
        # Retrieve data from table1
        select_query = f"SELECT * FROM {table1} LIMIT {num_rows}"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Transfer data to table2
        for row in rows:
            values = []
            for from_column, to_column in column_pairs:
                values.append(row[from_column])
            for additional_from_column, additional_to_column in additional_column_pairs:
                values.append(row[additional_from_column])

            # Construct the INSERT query
            placeholders = ', '.join(['%s'] * len(values))
            insert_query = f"INSERT INTO {table2} VALUES ({placeholders})"
            
            # Execute the INSERT query
            cursor.execute(insert_query, tuple(values))
            
            # Commit the changes every 100 rows
            if cursor.rowcount % 100 == 0:
                conn.commit()

        # Commit any remaining changes
        conn.commit()

        print("Data transfer completed successfully.")

    except Exception as e:
        print(f"An error occurred during data transfer: {str(e)}")
        conn.rollback()

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Example usage
host = "localhost"
user = "root"
password = "Me6111111"
database = "chicago_airbnb"
table1 = "reviews2"
table2 = "reviews_translations"
column_pairs = [("index", "index")]
num_rows = 1000
additional_column_pairs = [("comments", "translations")]

transfer_data(host, user, password, database, table1, table2, column_pairs, num_rows, *additional_column_pairs)








import mysql.connector

def transfer_data(host, user, password, database, table1, table2, column_pairs, num_rows, *additional_column_pairs):
    # Establish connection to MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()

    try:
        # Retrieve data from table1
        select_query = f"SELECT * FROM {table1} LIMIT {num_rows}"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Transfer data to table2
        for row in rows:
            values = []
            for from_column, to_column in column_pairs:
                values.append(row[from_column])
            for additional_from_column, additional_to_column in additional_column_pairs:
                values.append(row[additional_from_column])

            # Construct the INSERT query
            placeholders = ', '.join(['%s'] * len(values))
            insert_query = f"INSERT INTO {table2} VALUES ({placeholders})"
            
            # Execute the INSERT query
            cursor.execute(insert_query, tuple(values))
            
            # Commit the changes every 100 rows
            if cursor.rowcount % 100 == 0:
                conn.commit()

        # Commit any remaining changes
        conn.commit()

        print("Data transfer completed successfully.")

    except Exception as e:
        print(f"An error occurred during data transfer: {str(e)}")
        conn.rollback()

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Example usage
host = "localhost"
user = "root"
password = "Me6111111"
database = "chicago_airbnb"
table1 = "reviews2"
table2 = "reviews_translations"
column_pairs = [(0, 0)]  # Replace with the column indices of table1 and table2
num_rows = 1000
additional_column_pairs = []  # Replace with additional column pairs if needed

transfer_data(host, user, password, database, table1, table2, column_pairs, num_rows, *additional_column_pairs)'''






#mini using pair but not working
'''
import mysql.connector

def transfer_data(host, user, password, db_name, table1_name, table2_name, column_pairs, num_rows):
    # Connect to the database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = conn.cursor()

    # Retrieve the rows from the first table column
    select_query = f"SELECT `{column_pairs[0][0]}` FROM {table1_name} LIMIT {num_rows}"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Insert the rows into the second table column
    for i, row in enumerate(rows, 1):
        value = row[0]  # Assuming the first table column contains a single value
        insert_query = f"INSERT IGNORE INTO {table2_name} (`{column_pairs[0][1]}`) VALUES (%s)"
        cursor.execute(insert_query, (value,))

        # Save changes after every 100 rows
        if i % 100 == 0:
            conn.commit()

    # Save any remaining changes
    conn.commit()

    # Close the connection
    conn.close()

# Example usage:
column_pairs = [("comments", "translations")]
transfer_data("localhost", "root", "Me6111111", "chicago_airbnb", "reviews2", "reviews_translations", column_pairs, 1000)
'''







#accepts nulls
'''
import mysql.connector

def transfer_data(host, user, password, db_name, table1_name, table2_name, column_pairs, num_rows):
    # Connect to the database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = conn.cursor()

    # Retrieve the rows from the first table column
    select_query = f"SELECT `{column_pairs[0][0]}` FROM {table1_name} LIMIT {num_rows}"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Insert the rows into the second table column
    for i, row in enumerate(rows, 1):
        value = row[0] if row[0] is not None else None  # Handle null values
        insert_query = f"INSERT IGNORE INTO {table2_name} (`{column_pairs[0][1]}`) VALUES (%s)"
        cursor.execute(insert_query, (value,))

        # Save changes after every 100 rows
        if i % 100 == 0:
            conn.commit()

    # Save any remaining changes
    conn.commit()

    # Close the connection
    conn.close()

# Example usage:
column_pairs = [("comments", "translations")]
transfer_data("localhost", "root", "Me6111111", "chicago_airbnb", "reviews2", "reviews_translations", column_pairs, 1000)
'''






'''
#basic display of the 50 rows of specified column from table from database
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Me6111111",
    database="chicago_airbnb"
)
cursor = conn.cursor()

# Retrieve the first 50 rows from the 'comments' column
select_query = "SELECT comments FROM reviews2 LIMIT 50"
cursor.execute(select_query)
rows = cursor.fetchall()

# Display the comments
for row in rows:
    print(row[0])

# Close the connection
conn.close()
'''





'''
import mysql.connector
import pandas as pd

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Me6111111",
    database="chicago_airbnb"
)
cursor = conn.cursor()

# Retrieve the first 50 rows from the 'comments' column
select_query = "SELECT comments FROM reviews2 LIMIT 50"
cursor.execute(select_query)
rows = cursor.fetchall()

# Create a DataFrame from the result
df = pd.DataFrame(rows, columns=['comments'])

# Display the DataFrame
print(df)

# Close the connection
conn.close()
'''



'''
#could you write me the same code but which copies values from comments to translations between 
#those one ones which have the same value in column 'index'?

import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Me6111111",
    database="chicago_airbnb"
)
cursor = conn.cursor()

# Retrieve the rows from the 'comments' and 'index' columns
select_query = "SELECT comments, `index` FROM reviews2 LIMIT 50"
cursor.execute(select_query)
rows = cursor.fetchall()

# Copy comments to translations for rows with the same index
for row in rows:
    comment = row[0]
    index = row[1]
    
    update_query = "UPDATE reviews_translations SET translations = %s WHERE `index` = %s"
    cursor.execute(update_query, (comment, index))
    conn.commit()

# Close the connection
conn.close()
'''








'''
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Me6111111",
    database="chicago_airbnb"
)
cursor = conn.cursor()

# Retrieve the rows from the 'comments' and 'index' columns
select_query = "SELECT comments, `index` FROM reviews2 LIMIT 50"
cursor.execute(select_query)
rows = cursor.fetchall()

# Copy comments to translations for rows with the same index
for row in rows:
    comment = row[0]
    index = row[1]
    
    update_query = "UPDATE reviews_translations SET translations = %s WHERE `index` = %s"
    cursor.execute(update_query, (comment, index))
    conn.commit()

# Close the connection
conn.close()
'''




#index problem
'''
import mysql.connector
def migrator(host, user, password, db, num_rows, table_from, col_from, table_to, col_to):
    # Connect to the database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db
    )
    cursor = conn.cursor()

    # Retrieve the rows from the source column
    select_query = f"SELECT {col_from}, `index` FROM {table_from} LIMIT {num_rows}"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Copy data from the source column to the destination column
    for row in rows:
        data = row[0]
        index = row[1]
        
        update_query = f"UPDATE {table_to} SET {col_to} = %s WHERE `index` = %s"
        cursor.execute(update_query, (data, index))
        conn.commit()

    # Close the connection
    conn.close()

# Example usage
migrator('localhost', 'root', 'Me6111111', 'chicago_airbnb', 50, 'reviews2', 'index', 'comments', 'index')
'''
'''
'index' is a reserved keyword in MySQL, and using it as a column name without proper escaping causes a syntax error. 
To address this, you need to enclose the column name 'index' within backticks () to avoid conflicts with the reserved keyword. 
By doing so, MySQL recognizes 'index' as a column name rather than a keyword. 
Modifying the code to include backticks around the column name (index`) ensures the syntax is correct and resolves the error.
'''







#return to roots, simplest way
#but able to perform only once because doesn't consider that the pk may be the same 
'''
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Me6111111',
    database='chicago_airbnb'
)
cursor = conn.cursor()

# Retrieve the rows from the 'comments' column and 'index' column of 'reviews2'
select_query = "SELECT comments, `index` FROM reviews2"
cursor.execute(select_query)
rows = cursor.fetchall()

# Insert the values into the 'comment' column of 'comments' table, preserving the indexes
for row in rows:
    data = row[0]
    index = row[1]
    insert_query = "INSERT INTO comments (comment, `index`) VALUES (%s, %s)"
    cursor.execute(insert_query, (data, index))
    conn.commit()

# Close the connection
conn.close()
'''


# this one is looking for empty index and starting work for first one
# very good one
'''
do i understand corectly - this code is copying absolutely all values of column 'comments' and puts them in the 'comment' 
if in 'comments' is null in 'comment' will be null as well
is that true in one sentence?
ChatGPT
Yes, that is correct. The code copies all values from the 'comments' column and inserts them into the 'comment' column. If a value in the 
'comments' column is null, the corresponding value in the 'comment' column will also be null.
User
so how the index in 'comments'  table can be different? if even the nulls have to have their own indexes and if absolutely all values from column 
'comments' are copied answer in one sentence
ChatGPT
The index in the 'comments' table can be different if there are already existing rows in the 'comments' table with their own 
index values before the copying process, or if there are deletions and subsequent insertions that may affect the index values.
User
The index in the 'comments' table can be different if there are already existing rows in the 'comments' table with their own 
index values before the copying process, so before copying process you mean - before the run of the code first time. 
because if this column was empty and we've runned the code - there're only copied values which have indexes like in the table from 
which they've been copied
is that true? in one sentence
ChatGPT
Yes, if the 'comments' table was initially empty and the code was run for the first time, the copied values will have indexes 
corresponding to the original table from which they were copied.
User
and if we'll stop it and run again - the indexes still be the same because the code is looking for the first empty row and from 
it starts its work. so if we don't touch the sql table at all - except of running this code we can be 100% sure that the indexes are 
absolutely the same. is that true in one sentence
ChatGPT
Yes, if the code is not modified and the SQL table is not modified outside of running the code, the indexes will remain the same across 
multiple runs, ensuring that they are consistent with the original table.
'''
'''
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Me6111111',
    database='chicago_airbnb'
)
cursor = conn.cursor()

# Retrieve the rows from the 'comments' column and 'index' column of 'reviews2'
select_query = "SELECT comments, `index` FROM reviews2"
cursor.execute(select_query)
rows = cursor.fetchall()

# Insert the values into the 'comment' column of 'comments' table, preserving the indexes
commit_interval = 100
inserted_indexes = set()
for i, row in enumerate(rows, 1):
    data = row[0]
    index = row[1]
    
    # Check if the index is already inserted
    if index in inserted_indexes:
        continue

    # Check if the index exists in the destination table
    select_existing_query = "SELECT `index` FROM comments WHERE `index` = %s"
    cursor.execute(select_existing_query, (index,))
    existing_row = cursor.fetchone()
    
    if existing_row is not None:
        inserted_indexes.add(index)
        continue

    # Insert the row into the 'comments' table
    insert_query = "INSERT INTO comments (comment, `index`) VALUES (%s, %s)"
    cursor.execute(insert_query, (data, index))
    inserted_indexes.add(index)
    
    # Perform commit after every 100 rows
    if i % commit_interval == 0:
        conn.commit()

# Commit any remaining changes
conn.commit()

# Close the connection
conn.close()
'''





# replacing values in table 2 column 1 and 2 between table 1 column 1 and 2 in the pairs of the indexes
'''
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Me6111111',
    database='chicago_airbnb'
)
cursor = conn.cursor()

# Retrieve the rows from the 'comments' column and 'index' column of 'reviews2'
select_query = "SELECT comments, `index` FROM reviews2"
cursor.execute(select_query)
rows = cursor.fetchall()

# Update the 'comment' column in 'comments' table if values are different
for row in rows:
    data = row[0]
    index = row[1]

    # Check if the index exists in the destination table
    select_existing_query = "SELECT `index`, comment FROM comments WHERE `index` = %s"
    cursor.execute(select_existing_query, (index,))
    existing_row = cursor.fetchone()
    
    if existing_row is not None:
        existing_index, existing_comment = existing_row
        if existing_comment != data:
            update_query = "UPDATE comments SET comment = %s WHERE `index` = %s"
            cursor.execute(update_query, (data, existing_index))
    else:
        insert_query = "INSERT INTO comments (comment, `index`) VALUES (%s, %s)"
        cursor.execute(insert_query, (data, index))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
'''

'''
I took it with tears in my eyes and decided to fuck off this 0.083% of the data
print(251/300000)
'''





# code which iterates row by row of the table 'reviews', checking only vlues from columns 'index' and 'comments', 
# cpy them , no mtter what is inside (even if they're empty) thenpaste them both to the table 'comments' - to the cplumns 'index' and 'comment'

import pymysql

# Establish a connection to the MySQL database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Me6111111',
                             database='chicago_airbnb')
cursor = connection.cursor()

# Retrieve the rows from the 'index' and 'comments' columns of the 'reviews' table
select_query = "SELECT `index`, comments FROM reviews"
cursor.execute(select_query)
rows = cursor.fetchall()

# Create the 'comments' table with the 'index' and 'comment' columns
create_table_query = """
    CREATE TABLE IF NOT EXISTS comments (
        `index` INT,
        comment TEXT
    )
"""
cursor.execute(create_table_query)

# Iterate over rows and insert values into the 'comments' table
for row in rows:
    index = row[0]
    comment = row[1]

    # Insert values into the 'comments' table
    insert_query = "INSERT INTO comments (`index`, comment) VALUES (%s, %s)"
    cursor.execute(insert_query, (index, comment))

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()