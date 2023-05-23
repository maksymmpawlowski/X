# basic one meeting requirements in reactions on different cases
'''
import mysql.connector
from mysql.connector import Error
from textblob import TextBlob

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
        
        # Fetch rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()
        
        # Iterate through the rows and update 'translations' table
        for row in rows:
            index = row[0]
            comment = row[1]
            
            # Update 'translations' table
            update_query = f"UPDATE translations SET index={index}, trsl=%s WHERE index={index}"
            
            if comment and TextBlob(comment).detect_language() == 'en':
                # Copy the English comment to 'trsl' column
                translation = comment
            else:
                # Translate the comment to English
                translation = str(TextBlob(comment).translate(to='en'))
            
            # Execute the update query
            cursor.execute(update_query, (translation,))
            connection.commit()
        
        print('Translation and update completed successfully')
        
except Error as e:
    print('Error while connecting to MySQL database', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''




# api problem
'''
import mysql.connector
from mysql.connector import Error
from textblob import TextBlob
from textblob.exceptions import NotTranslated

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
        
        # Fetch rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()
        
        # Iterate through the rows and update 'translations' table
        for row in rows:
            index = row[0]
            comment = row[1]
            
            # Update 'translations' table
            update_query = f"UPDATE translations SET index={index}, trsl=%s WHERE index={index}"
            
            try:
                if comment and TextBlob(comment).detect_language() == 'en':
                    # Copy the English comment to 'trsl' column
                    translation = comment
                else:
                    # Translate the comment to English
                    translation = str(TextBlob(comment).translate(to='en'))
                
                # Execute the update query
                cursor.execute(update_query, (translation,))
                connection.commit()
                
            except NotTranslated:
                # Handle exception when translation is not possible
                print(f"Translation not possible for index {index}")
            
            except Exception as e:
                # Handle other exceptions
                print(f"Error occurred for index {index}: {e}")
        
        print('Translation and update completed successfully')
        
except Error as e:
    print('Error while connecting to MySQL database', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''







# the code expects the response from the Microsoft Translator API to contain a 'language' key, but it is not present in the response, causing a KeyError.
'''
import mysql.connector
from mysql.connector import Error
import requests

# Function to detect the language using Microsoft Translator API
def detect_language(text, api_key):
    endpoint = "https://api.cognitive.microsofttranslator.com/detect?api-version=3.0"
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": api_key
    }
    data = [{
        "Text": text
    }]
    response = requests.post(endpoint, headers=headers, json=data)
    result = response.json()
    return result[0]['language']

# Function to translate the text using Microsoft Translator API
def translate_text(text, target_language, api_key):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to={}".format(target_language)
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": api_key
    }
    data = [{
        "Text": text
    }]
    response = requests.post(endpoint, headers=headers, json=data)
    result = response.json()
    return result[0]['translations'][0]['text']

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
        
        # Fetch rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()
        
        # Iterate through the rows and update 'translations' table
        for row in rows:
            index = row[0]
            comment = row[1]
            
            # Update 'translations' table
            update_query = f"UPDATE translations SET index={index}, trsl=%s WHERE index={index}"
            
            if comment and detect_language(comment, 'YOUR_MICROSOFT_TRANSLATOR_API_KEY') == 'en':
                # Copy the English comment to 'trsl' column
                translation = comment
            else:
                # Translate the comment to English
                translation = translate_text(comment, 'en', 'YOUR_MICROSOFT_TRANSLATOR_API_KEY')
            
            # Execute the update query
            cursor.execute(update_query, (translation,))
            connection.commit()
        
        print('Translation and update completed successfully')
        
except Error as e:
    print('Error while connecting to MySQL database', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''




# DEEPL api
'''
import mysql.connector
from mysql.connector import Error
from textblob import TextBlob
import requests

def detect_language(text, api_key):
    endpoint = "https://api.cognitive.microsofttranslator.com/detect?api-version=3.0"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/json"
    }
    data = [{"text": text}]
    
    response = requests.post(endpoint, headers=headers, json=data)
    result = response.json()
    
    return result[0]['language']

def translate_text(text, api_key):
    endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/json"
    }
    data = [{
        "text": text,
        "to": "en"
    }]
    
    response = requests.post(endpoint, headers=headers, json=data)
    result = response.json()
    translation = result[0]['translations'][0]['text']
    
    return translation

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
        
        # Fetch rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()
        
        # Iterate through the rows and update 'translations' table
        for row in rows:
            index = row[0]
            comment = row[1]
            
            # Update 'translations' table
            update_query = f"UPDATE translations SET index={index}, trsl=%s WHERE index={index}"
            
            if comment and detect_language(comment, 'YOUR_MICROSOFT_TRANSLATOR_API_KEY') == 'en':
                # Copy the English comment to 'trsl' column
                translation = comment
            else:
                # Translate the comment to English
                translation = translate_text(comment, 'YOUR_MICROSOFT_TRANSLATOR_API_KEY')
            
            # Execute the update query
            cursor.execute(update_query, (translation,))
            connection.commit()
        
        print('Translation and update completed successfully')
        
except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''






# works but no changes in table
'''
import mysql.connector
from mysql.connector import Error
from translate import Translator

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

        # Fetch rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()

        # Iterate through the rows and update 'translations' table
        for row in rows:
            comment_id = row[0]
            comment = row[1]

            # Update 'translations' table
            update_query = "UPDATE translations SET trsl=%s WHERE `index`=%s"

            if comment:
                # Perform language detection only if the comment is not empty
                translator = Translator(to_lang='en')
                translation = translator.translate(comment)
            else:
                # Handle empty comment
                translation = ''

            # Execute the update query
            cursor.execute(update_query, (translation, comment_id))
            connection.commit()

        print('Translation and update completed successfully')

except Error as e:
    print('Error while connecting to MySQL database', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''






# works but not commits
'''
import mysql.connector
from mysql.connector import Error
from translate import Translator

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

        # Fetch rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments')
        rows = cursor.fetchall()

        # Iterate through the rows and translate the comments
        for row in rows:
            comment_id = row[0]
            comment = row[1]

            if comment:
                # Perform translation only if the comment is not empty
                translator = Translator(to_lang='en')
                translation = translator.translate(comment)
                print(f'Comment ID: {comment_id}, Translation: {translation}')
            else:
                # Handle empty comment
                translation = ''
                print(f'Comment ID: {comment_id}, Translation: [Empty]')

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''






# For the single line
'''
import mysql.connector
from mysql.connector import Error
from googletrans import Translator
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

        # Fetch one row from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments LIMIT 1')
        row = cursor.fetchone()

        # Create a Translator instance
        translator = Translator()

        # Extract values from the row
        comment_index = row[0]
        comment = row[1]

        # Language detection
        try:
            language = langdetect.detect(comment)
        except Exception as e:
            language = 'unknown'
            print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

        # Translation based on language
        if language == 'en':
            translation = comment
        else:
            try:
                translation = translator.translate(comment, dest='en').text
            except Exception as e:
                translation = 'unknown'
                print(f"Error occurred during translation for Comment Index {comment_index}: {str(e)}")

        print(f'Comment Index: {comment_index}, Translation: {translation}')

        # Insert a new row into 'translations' table
        insert_query = "INSERT INTO translations (`index`, trsl) VALUES (%s, %s)"
        cursor.execute(insert_query, (comment_index, translation))
        connection.commit()

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''




#puts the name of language to new column lang
'''
import mysql.connector
from mysql.connector import Error
from googletrans import Translator
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

        # Fetch one row from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments LIMIT 1')
        row = cursor.fetchone()

        # Create a Translator instance
        translator = Translator()

        # Extract values from the row
        comment_index = row[0]
        comment = row[1]

        # Language detection
        try:
            language = langdetect.detect(comment)
        except Exception as e:
            language = 'unknown'
            print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

        # Translation based on language
        if language == 'en':
            translation = comment
        else:
            try:
                translation = translator.translate(comment, dest='en').text
            except Exception as e:
                translation = 'unknown'
                print(f"Error occurred during translation for Comment Index {comment_index}: {str(e)}")

        print(f'Comment Index: {comment_index}, Translation: {translation}')

        # Insert a new row into 'translations' table
        insert_query = "INSERT INTO translations (`index`, trsl, lang) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (comment_index, translation, language))
        connection.commit()

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''




# 100 rows
'''
import mysql.connector
from mysql.connector import Error
from googletrans import Translator
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

        # Fetch the first 100 rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments LIMIT 100')
        rows = cursor.fetchall()

        # Create a Translator instance
        translator = Translator()

        # Iterate through the rows and perform operations
        for row in rows:
            comment_index = row[0]
            comment = row[1]

            # Language detection
            try:
                language = langdetect.detect(comment)
            except Exception as e:
                language = 'unknown'
                print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

            # Translation based on language
            if language == 'en':
                translation = comment
            else:
                try:
                    translation = translator.translate(comment, dest='en').text
                except Exception as e:
                    translation = 'unknown'
                    print(f"Error occurred during translation for Comment Index {comment_index}: {str(e)}")

            print(f'Comment Index: {comment_index}, Translation: {translation}')

            # Update 'translations' table
            update_query = "INSERT INTO translations (`index`, trsl, lang) VALUES (%s, %s, %s)"
            cursor.execute(update_query, (comment_index, translation, language))
            connection.commit()

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''








'''
# 1000 rows
import mysql.connector
from mysql.connector import Error
from googletrans import Translator
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

        # Fetch the first 1000 rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments LIMIT 1000')
        rows = cursor.fetchall()

        # Create a Translator instance
        translator = Translator()

        # Iterate through the rows and perform operations
        for row in rows:
            comment_index = row[0]
            comment = row[1]

            # Language detection
            try:
                language = langdetect.detect(comment)
            except Exception as e:
                language = 'unknown'
                print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

            # Translation based on language
            if language == 'en':
                translation = comment
            else:
                try:
                    translation = translator.translate(comment, dest='en').text
                except Exception as e:
                    translation = 'unknown'
                    print(f"Error occurred during translation for Comment Index {comment_index}: {str(e)}")

            print(f'Comment Index: {comment_index}, Translation: {translation}')

            # Update 'translations' table
            update_query = "INSERT INTO translations (`index`, trsl, lang) VALUES (%s, %s, %s)"
            cursor.execute(update_query, (comment_index, translation, language))
            connection.commit()

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''









'''
import mysql.connector
from mysql.connector import Error
from googletrans import Translator
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

        # Fetch the first 1000 rows from 'comments' table
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM comments LIMIT 1000')
        rows = cursor.fetchall()

        # Create a Translator instance
        translator = Translator()

        # Iterate through the rows and perform operations
        for row in rows:
            comment_index = row[0]
            comment = row[1]

            # Language detection
            try:
                language = langdetect.detect(comment)
            except Exception as e:
                language = 'unknown'
                print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

            # Translation based on language
            if language == 'en':
                translation = comment
            else:
                try:
                    translation = translator.translate(comment, dest='en').text
                except Exception as e:
                    translation = 'unknown'
                    print(f"Error occurred during translation for Comment Index {comment_index}: {str(e)}")

            print(f'Comment Index: {comment_index}, Translation: {translation}')

            # Update 'translations' table
            update_query = "INSERT INTO translations (`index`, trsl, lang) VALUES (%s, %s, %s)"
            cursor.execute(update_query, (comment_index, translation, language))
            connection.commit()

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''









# i want it to be be performed for all rows of table 'comments' but do commit after every 1000 rows
'''
import mysql.connector
from mysql.connector import Error
from googletrans import Translator
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

        # Create a Translator instance
        translator = Translator()

        # Set the batch size for committing changes
        batch_size = 1000
        count = 0

        # Iterate through the rows and perform operations
        for row in rows:
            comment_index = row[0]
            comment = row[1]

            # Language detection
            try:
                language = langdetect.detect(comment)
            except Exception as e:
                language = 'unknown'
                print(f"Error occurred during language detection for Comment Index {comment_index}: {str(e)}")

            # Translation based on language
            if language == 'en':
                translation = comment
            else:
                try:
                    translation = translator.translate(comment, dest='en').text
                except Exception as e:
                    translation = 'unknown'
                    print(f"Error occurred during translation for Comment Index {comment_index}: {str(e)}")

            print(f'Comment Index: {comment_index}, Translation: {translation}')

            # Update 'translations' table
            update_query = "INSERT INTO translations (`index`, trsl, lang) VALUES (%s, %s, %s)"
            cursor.execute(update_query, (comment_index, translation, language))

            count += 1
            if count % batch_size == 0:
                connection.commit()
                print(f"Committed changes for {count} rows")

        # Commit any remaining changes
        connection.commit()
        print(f"Committed changes for {count} rows")

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''







'''
could you write me the code which analyzes the table 'languages' looking in the column 'lang' for entries diffetent than 'en',
checks the indexes of those ones, then in table 'comments' translates cells from column 'comment' having the same index 
as those rows from table 'languages' which entries from column 'lang' were identified as not 'en', then puts: 
index to the column 'index' and translation on english to the column 'trsl' in the table 'translations'?
'''
'''
import mysql.connector
from mysql.connector import Error
from googletrans import Translator

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

        # Fetch rows from 'languages' table with non-English language entries
        cursor = connection.cursor()
        select_query = "SELECT `index` FROM languages WHERE lang != 'en'"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Create a Translator instance
        translator = Translator()

        # Set the batch size for committing changes
        batch_size = 100
        count = 0

        # Iterate through the rows and perform translation
        for row in rows:
            comment_index = row[0]

            # Fetch the comment from 'comments' table based on the index
            select_comment_query = "SELECT comment FROM comments WHERE `index` = %s"
            cursor.execute(select_comment_query, (comment_index,))
            comment_row = cursor.fetchone()

            if comment_row is not None:
                comment = comment_row[0]

                # Translation of the comment to English
                try:
                    translation = translator.translate(comment, dest='en').text
                except Exception as e:
                    translation = 'unknown'
                    print(f"Error occurred during translation for Comment Index {comment_index}: {str(e)}")

                print(f'Comment Index: {comment_index}, Translation: {translation}')

                # Insert the translation into 'translations' table
                insert_query = "INSERT INTO translations (`index`, trsl) VALUES (%s, %s)"
                cursor.execute(insert_query, (comment_index, translation))

                count += 1
                if count % batch_size == 0:
                    connection.commit()
                    print(f"Committed changes for {count} rows")

        # Commit any remaining changes
        connection.commit()
        print(f"Committed changes for {count} rows")

        print('Translation completed successfully')

except Error as e:
    print('Error while connecting to MySQL database:', e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
'''




'''
write me the code using this query:
SELECT * FROM languages WHERE lang <> 'en';
which for rows returned by this query do this:
checks the number which is in the column index, 
then it's going to the table 'comments' - finding row with corresponding index, 
translates value in column 'comment' to english - if it has a problem with recognition of language it uses the value from column 'lang' of table 'languages',
then it goes to the tabe 'translations' - puts the 'index' in the column 'index' and translated text in the column 'trsl'
i want this code be executed for every row of the filtered table 'languages' by the query i written above
'''
# extremely slow processing (>1s/row), because of exceeding 500 allowed chars of queries caused by putting all the comment content inside
'''
import mysql.connector
from translate import Translator

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(user='root', password='Me6111111', host='localhost', database='chicago_airbnb')
cursor = cnx.cursor()

# Execute the query
query = "SELECT * FROM languages WHERE lang <> 'en';"
cursor.execute(query)
rows = cursor.fetchall()  # Fetch all results

# Iterate over the rows returned by the query
for row in rows:
    index = row[0]
    lang = row[1]

    # Retrieve corresponding comment from the 'comments' table
    query_comments = "SELECT comment FROM comments WHERE `index` = %s;"
    cursor.execute(query_comments, (index,))
    comment_row = cursor.fetchone()

    if comment_row:
        comment = comment_row[0]

        # Translate the comment to English
        translator = Translator(to_lang='en', from_lang=lang)
        translation = translator.translate(comment)

        print(f"Index: {index}, Translation: {translation}")

        # Check if the translation already exists in the 'translations' table
        query_existing = "SELECT * FROM translations WHERE `index` = %s;"
        cursor.execute(query_existing, (index,))
        existing_row = cursor.fetchone()

        if existing_row:
            # Update the existing row
            query_update = "UPDATE translations SET trsl = %s WHERE `index` = %s;"
            try:
                cursor.execute(query_update, (translation, index))
            except mysql.connector.Error as err:
                print(f"Error updating translation for index {index}: {err}")
        else:
            # Insert a new row
            query_insert = "INSERT INTO translations (`index`, trsl) VALUES (%s, %s);"
            try:
                cursor.execute(query_insert, (index, translation))
            except mysql.connector.Error as err:
                print(f"Error inserting translation for index {index}: {err}")

        cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
'''






# copying to trsl and translating there
'''
write me new code. i want it to iterate through the 'languages' table, copy every 'index' value, 
paste it in the 'index' of table 'translations', from the table 'comments' 
with the same index copy value from the column 'comment', paste it in the 'trsl' column in table 'translations' 
then replace it with its translation on english from language described in 
column 'lang' of table 'languages' - if there in column 'lang' is written 'unknown' it tries to translate it by itself 
but if its unable translate it - it puts 'unknown' in the 'trsl' column.
i want it to do commit after every 100 rows
'''
'''
import mysql.connector
from translate import Translator

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(user='root', password='Me6111111', host='localhost', database='chicago_airbnb')
cursor = cnx.cursor()

# Execute the query to retrieve data from the 'languages' table
query_languages = "SELECT `index`, lang FROM languages;"
cursor.execute(query_languages)

# Fetch all rows from the cursor
rows = cursor.fetchall()

# Counter to track the number of processed rows
row_count = 0

# Iterate over the rows
for row in rows:
    index = row[0]
    lang = row[1]

    # Retrieve the corresponding comment from the 'comments' table
    query_comments = "SELECT comment FROM comments WHERE `index` = %s;"
    cursor.execute(query_comments, (index,))
    comment_row = cursor.fetchone()

    if comment_row:
        comment = comment_row[0]

        # Translate the comment to English
        if lang != 'unknown':
            translator = Translator(to_lang='en', from_lang=lang)
            translation = translator.translate(comment)
        else:
            try:
                translation = Translator(to_lang='en').translate(comment)
            except:
                translation = 'unknown'

        # Insert the index and translated comment into the 'translations' table
        query_insert = "INSERT INTO translations (`index`, trsl) VALUES (%s, %s);"
        cursor.execute(query_insert, (index, translation))

        row_count += 1

        # Commit after every 100 rows
        if row_count % 100 == 0:
            cnx.commit()

# Final commit for remaining rows
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
'''







import mysql.connector
from googletrans import Translator

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(user='root', password='Me6111111', host='localhost', database='chicago_airbnb')
cursor = cnx.cursor()

# Initialize the translator
translator = Translator(service_urls=['translate.google.com'])

# Execute the query to retrieve data from the 'languages' table
query_languages = "SELECT `index`, lang FROM languages WHERE lang <> 'en';"
cursor.execute(query_languages)

# Fetch all rows to discard unread results
cursor.fetchall()

# Iterate over the rows returned by the query
for row in cursor:
    index = row[0]
    lang = row[1]

    # Retrieve the corresponding comment from the 'comments' table
    query_comments = "SELECT comment FROM comments WHERE `index` = %s;"
    cursor.execute(query_comments, (index,))
    comment_row = cursor.fetchone()

    if comment_row:
        comment = comment_row[0]
        translation = translator.translate(comment, dest='en', src=lang).text

        # Insert the index and translated comment into the 'translations' table
        query_insert = "INSERT INTO translations (`index`, trsl) VALUES (%s, %s);"
        cursor.execute(query_insert, (index, translation))

        cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()