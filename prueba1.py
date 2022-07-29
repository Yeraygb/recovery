import os
import sqlite3


# Build Data path
data_path = "/Users/IEUser/Appdata/Roaming/Mozilla/Firefox/Profiles/opy8vubs.default-release/"
history_db = os.path.join(data_path, 'places.sqlite')

# Make connection with sqlite3 database
c = sqlite3.connect(history_db)

# Create cursor object to execute query
cursor = c.cursor()
select_statement = "select moz_places.url, moz_places.visit_count from moz_places;"
cursor.execute(select_statement)

# Fetch the result and Prints the result
results = cursor.fetchall()

for url, count in results:
	print(url)

# Close the cursor
cursor.close()