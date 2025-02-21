# import sqlite3
# import pytz
# from datetime import datetime

# # Load Database Packages
# conn = sqlite3.connect('./data/data.db', check_same_thread=False)
# c = conn.cursor()

# IST = pytz.timezone('Asia/Kolkata')  # Indian Standard Time

# # Function to create page visited table
# def create_page_visited_table():
#     c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')

# # Function to add page visited details
# def add_page_visited_details(pagename, timeOfvisit=None):
#     if timeOfvisit is None:
#         timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
#     else:
#         timeOfvisit = timeOfvisit.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")
#     c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))
#     conn.commit()

# # Function to view all page visited details
# def view_all_page_visited_details():
#     c.execute('SELECT * FROM pageTrackTable')
#     data = c.fetchall()
#     return data

# # Function to create emotion classifier table
# def create_emotionclf_table():
#     c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfvisit TIMESTAMP)')

# # Function to add prediction details
# def add_prediction_details(rawtext, prediction, probability, timeOfvisit=None):
#     if timeOfvisit is None:
#         timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
#     else:
#         timeOfvisit = timeOfvisit.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")
#     c.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES (?, ?, ?, ?)', (rawtext, prediction, probability, timeOfvisit))
#     conn.commit()

# # Function to view all prediction details
# def view_all_prediction_details():
#     c.execute('SELECT * FROM emotionclfTable')
#     data = c.fetchall()
#     return data

import sqlite3
import os
import pytz
from datetime import datetime

# Ensure absolute path to the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
DB_PATH = os.path.join(BASE_DIR, "data", "data.db")  # Construct absolute path

# Ensure the data folder exists
if not os.path.exists(os.path.join(BASE_DIR, "data")):
    os.makedirs(os.path.join(BASE_DIR, "data"))

# Load Database
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

IST = pytz.timezone('Asia/Kolkata')  # Indian Standard Time

# Function to create page visited table
def create_page_visited_table():
    c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')
    conn.commit()

# Function to add page visited details
def add_page_visited_details(pagename, timeOfvisit=None):
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
    else:
        timeOfvisit = timeOfvisit.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))
    conn.commit()

# Function to view all page visited details
def view_all_page_visited_details():
    c.execute('SELECT * FROM pageTrackTable')
    data = c.fetchall()
    return data

# Function to create emotion classifier table
def create_emotionclf_table():
    c.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability NUMBER, timeOfvisit TIMESTAMP)')
    conn.commit()

# Function to add prediction details
def add_prediction_details(rawtext, prediction, probability, timeOfvisit=None):
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
    else:
        timeOfvisit = timeOfvisit.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES (?, ?, ?, ?)', (rawtext, prediction, probability, timeOfvisit))
    conn.commit()

# Function to view all prediction details
def view_all_prediction_details():
    c.execute('SELECT * FROM emotionclfTable')
    data = c.fetchall()
    return data
