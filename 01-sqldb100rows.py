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

    # Retrieve the desired rows from the reviews2 table
    query = f"SELECT * FROM reviews2 LIMIT {num_rows};"
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