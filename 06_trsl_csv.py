'''
import pandas as pd
from googletrans import Translator

translator = Translator()

# Read the output.csv file
data = pd.read_csv('output.csv')

# Create empty lists for index and translated comments
index_list = []
translated_comments = []

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    comment = row['comment']
    lang = row['lang']
    
    # Translate the comment if the language is not English
    if lang != 'en':
        translation = translator.translate(comment, dest='en').text
    else:
        translation = comment
    
    # Append index and translated comment to the respective lists
    index_list.append(index)
    translated_comments.append(translation)

    # Save the translations to the translations.csv file after each iteration
    translations = pd.DataFrame({'index': index_list, 'comment': translated_comments})
    translations.to_csv('translations.csv', index=False)

print("Translation completed successfully.")
'''




'''
import pandas as pd
from googletrans import Translator
import time

translator = Translator()

# Read the output.csv file
data = pd.read_csv('output.csv')

# Create empty lists for index and translated comments
index_list = []
translated_comments = []

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    comment = row['comment']
    lang = row['lang']
    
    # Translate the comment if the language is not English
    if lang != 'en':
        translation = None
        while translation is None:
            try:
                translation = translator.translate(comment, dest='en').text
            except Exception as e:
                print(f"Translation failed for index {index}. Retrying...")
                time.sleep(2)  # Add a delay of 2 seconds before retrying

    else:
        translation = comment
    
    # Append index and translated comment to the respective lists
    index_list.append(index)
    translated_comments.append(translation)

    # Save the translations to the translations.csv file after each iteration
    translations = pd.DataFrame({'index': index_list, 'comment': translated_comments})
    translations.to_csv('translations.csv', index=False)

print("Translation completed successfully.")
'''






'''
Translation failed for index 6035. Retrying...
Translation failed for index 6035. Retrying...
Translation failed for index 6035. Retrying...
Translation failed for index 6035. Retrying...
Translation failed for index 6035. Retrying...
Translation failed for index 6035. Retrying...
Translation failed for index 6035. Retrying...
'''
'''
import pandas as pd
from googletrans import Translator
import time

translator = Translator()

# Read the output.csv file
data = pd.read_csv('output.csv')

# Create empty lists for index and translated comments
index_list = []
translated_comments = []

# Flag to indicate if the desired index has been reached
start_index_reached = False

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    # Skip rows until the desired index is reached
    if not start_index_reached:
        if index != 6035:
            continue
        else:
            start_index_reached = True

    comment = row['comment']
    lang = row['lang']

    # Check if the comment is empty or consists only of whitespace
    if not comment.strip():
        # Assign a default value or skip translation for empty comments
        translation = "N/A"
    elif lang != 'en':
        translation = None
        while translation is None:
            try:
                translation = translator.translate(comment, dest='en').text
            except Exception as e:
                print(f"Translation failed for index {index}. Retrying...")
                time.sleep(2)  # Add a delay of 2 seconds before retrying

    else:
        translation = comment

    # Append index and translated comment to the respective lists
    index_list.append(index)
    translated_comments.append(translation)

    # Save the translations to the translations.csv file after each iteration
    translations = pd.DataFrame({'index': index_list, 'comment': translated_comments})
    translations.to_csv('translations.csv', index=False)
    print(f"Translation saved for index {index}.")

print("Translation completed successfully.")
'''








import pandas as pd
from googletrans import Translator
import time
import math

translator = Translator()

# Read the output.csv file
data = pd.read_csv('output.csv')

# Create empty lists for index and translated comments
index_list = []
translated_comments = []

# Flag to indicate if the desired index has been reached
start_index_reached = False

# Maximum number of retry attempts
max_retries = 3

# Iterate through each row in the DataFrame
for index, row in data.iterrows():
    # Skip rows until the desired index is reached
    if not start_index_reached:
        if index != 6035:
            continue
        else:
            start_index_reached = True

    comment = row['comment']
    lang = row['lang']

    # Check if the comment is NaN or empty string
    if isinstance(comment, float) and math.isnan(comment):
        # Assign a default value for NaN comment
        translation = "N/A"
    elif not comment.strip():
        # Leave translation cell empty for empty comments
        translation = ""
    elif lang != 'en':
        translation = None
        retries = 0
        while translation is None and retries < max_retries:
            try:
                translation = translator.translate(str(comment), dest='en').text
            except Exception as e:
                print(f"Translation failed for index {index}. Retrying...")
                time.sleep(2)  # Add a delay of 2 seconds before retrying
                retries += 1

        if translation is None:
            print(f"Translation failed for index {index} after {max_retries} retries.")
            translation = "N/A"
    else:
        translation = comment

    # Append index and translated comment to the respective lists
    index_list.append(index)
    translated_comments.append(translation)

    # Save the translations to the translations.csv file after each iteration
    translations = pd.DataFrame({'index': index_list, 'comment': translated_comments})
    translations.to_csv('translations.csv', index=False)
    print(f"Translation saved for index {index}.")

print("Translation completed successfully.")