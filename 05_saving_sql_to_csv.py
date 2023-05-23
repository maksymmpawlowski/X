import pandas as pd
import mysql.connector

# Connect to the MySQL database using the provided information
cnx = mysql.connector.connect(user='root', password='Me6111111', host='localhost', database='chicago_airbnb')
cursor = cnx.cursor()

# Query to retrieve rows from 'languages' where 'lang' is not 'en' and join with 'comments' table
query = '''
SELECT l.*, c.comment
FROM languages AS l
LEFT JOIN comments AS c ON l.`index` = c.`index`
WHERE l.lang <> 'en'
'''

# Execute the query and load results into a DataFrame
df = pd.read_sql_query(query, cnx)

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

# Close the database connection
cnx.close()