import streamlit as st
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Function to create a table with fixed columns
def create_table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            email TEXT
        )
    """)
    conn.commit()

# Function to insert data into the table
def insert_data(name, age, email):
    c.execute("INSERT INTO my_table (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()

# Create the table with fixed columns
create_table()

# Streamlit App UI
st.title('Streamlit Database Manager')

st.write("Table 'my_table' has been created with the following columns: id, name, age, email.")

# Input for new data (name, age, email)
name = st.text_input('Enter Name')
age = st.number_input('Enter Age', min_value=0, max_value=120, step=1)
email = st.text_input('Enter Email')

if st.button('Add Row'):
    if name and email:  # Ensure required fields are filled
        insert_data(name, age, email)
        st.success(f'Row added to "my_table" successfully!')
    else:
        st.error('Please fill in both the Name and Email fields.')

# Display the current data in the table
if st.button('Show Data'):
    c.execute("SELECT * FROM my_table")
    rows = c.fetchall()
    if rows:
        st.write("Current data in 'my_table':")
        st.write(rows)
    else:
        st.write("No data available in 'my_table'.")

# Close the database connection when done
conn.close()
