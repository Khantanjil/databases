"""
Learning data bases
Create function
Insert function
Delete function
Update function
View function
"""

# Importing sqlite3
import sqlite3


# Create an database
def create_database():
    conn = sqlite3.connect(  # Make a connection to database
        "lite.db"  # Name of the database file
    )
    cur = conn.cursor()  # Create a cursor object
    cur.execute(  # Execute a SQL Query
        # Create a table with 3 columns
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity TEXT, price REAL )"
    )
    conn.commit()  # Save the changes
    conn.close()  # Exit the connection of the database


def insert_database(item, quantity, price):
    conn = sqlite3.connect(
        "lite.db"
    )
    cur = conn.cursor(
    )
    cur.execute(
        "INSERT INTO store VALUES (?,?,?)", (  # Insert a new row
            item, quantity, price
        )
    )
    conn.commit()
    conn.close()


def delete_database(item):
    conn = sqlite3.connect(
        "lite.db"
    )
    cur = conn.cursor(
    )
    cur.execute(
        "DELETE FROM store WHERE item=?", (  # Delete the item passed on the parameter of the function
            item,
        )
    )
    conn.commit(
    )
    conn.close(
    )


def update_database(quantity, price, item):
    conn = sqlite3.connect(
        "lite.db"
    )
    cur = conn.cursor(
    )
    cur.execute(
        "UPDATE store SET quantity=?, price=? WHERE item=?", (  # Updates the quantity or price to an item
            quantity,
            price,
            item
        )
    )
    conn.commit(
    )
    conn.close(
    )


def view_database():
    conn = sqlite3.connect(
        "lite.db"
    )
    cur = conn.cursor(
    )
    cur.execute(
        "SELECT * FROM store"
    )
    rows = cur.fetchall(
    )
    conn.commit(
    )
    conn.close(
    )
    return rows

create_database()  # Create the database
# insert_database("Uvas", 500, 0.35) # Insert a row
print(view_database())  # Show the rows
# delete_database("Uvas") # Delete an row
# print(view_database())
#update_database(10, 2.19, "Melancia") # Update the quantity and the price of the melancia (watermelon on portuguese)
print(view_database())
