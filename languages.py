# info about every row
'''
import mysql.connector
from mysql.connector import Error
import langdetect

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='chicago_airbnb',
        user='root',
        password='Me6111111'
    )

    if connection.is_connected():
        print('Connected to MySQL database')

        # Fetch all rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()

        # Set the batch size for committing changes
        batch_size = 1000
        count = 0

        # Iterate through the rows and perform language detection
        for row in rows:
            comment_index = row[0]
            comment = row[1]

            # Language detection
            try:
                language = langdetect.detect(comment)
            except Exception as e:
                language = 'unknown'
                print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

            print(f'Comment Index: {comment_index}, Language: {language}')

            # Update 'languages' table
            update_query = "INSERT INTO languages (`index`, lang) VALUES (%s, %s)"
            cursor.execute(update_query, (comment_index, language))

            count += 1
            if count % batch_size == 0:
                connection.commit()
                print(f"Committed changes for {count} rows")

        # Commit any remaining changes
        connection.commit()
        print(f"Committed changes for {count} rows")

        print('Language detection completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''





#prints in terminal info only after made commit

import mysql.connector
from mysql.connector import Error
import langdetect

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='chicago_airbnb',
        user='root',
        password='Me6111111'
    )

    if connection.is_connected():
        print('Connected to MySQL database')

        # Fetch all rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()

        # Set the batch size for committing changes
        batch_size = 1000
        count = 0
        commit_count = 0

        # Iterate through the rows and perform language detection
        for row in rows:
            comment_index = row[0]
            comment = row[1]

            # Language detection
            try:
                language = langdetect.detect(comment)
            except Exception as e:
                language = 'unknown'
                print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

            # Update 'languages' table
            update_query = "INSERT INTO languages (`index`, lang) VALUES (%s, %s)"
            cursor.execute(update_query, (comment_index, language))

            count += 1
            if count % batch_size == 0:
                connection.commit()
                commit_count += 1

        # Commit any remaining changes
        connection.commit()
        commit_count += 1
        print(f"Number of commits: {commit_count}")

        print('Language detection completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
