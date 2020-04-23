# Importing psycopg2
import psycopg2

# Function to create a table


def create_table():
    conn = psycopg2.connect(
        # Connect to the pgAdmin3
        "dbname='store' user='postgres' password='admin' host='localhost'"
    )
    cur = conn.cursor(  # Create a object cursor
    )
    cur.execute(  # Execute a SQL Query
        # Create a table
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity Integer, price REAL)"
    )
    conn.commit(  # Save the changes
    )
    conn.close(  # Close the connection of the database
    )


# Function to insert rows
def insert_row(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='store' user='postgres' password='admin' host='localhost'"
    )
    cur = conn.cursor(
    )
    cur.execute(
        "INSERT INTO store VALUES (%s, %s, %s)", (  # Insert a new row of the following 3 columns
            item,
            quantity,
            price
        )
    )
    conn.commit(
    )
    conn.close(
    )

# Function to delete rows


def delete_row(item):
    conn = psycopg2.connect(
        "dbname='store' user='0postgres' password='admin' host='localhost'"
    )
    cur = conn.cursor(
    )
    cur.execute(
        "DELETE FROM store WHERE item=%s", (  # Delete the item passed on the parameter of the delete function
            item,
        )
    )
    conn.commit(
    )
    conn.close(
    )

# Function to update rows


def update_row(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='store' user='postgres' password='admin' host='localhost'"
    )
    cur = conn.cursor()
    cur.execute(
        "UPDATE store SET quantity=%s, price=% WHERE item=%s", (  # Update the quantity and price values of the item passed of the function parameter
            item,
            quantity,
            price
        )
    )
    conn.commit()
    conn.close()

# Function to show the all the existing rows


def view_rows():
    conn = psycopg2.connect(
        "dbname='store' user='postgres' password='admin' host='localhost'"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM store"
    )
    rows = cur.fetchall(
    )
    conn.commit()
    conn.close()
    return rows

create_table()
"""
insert_row("Orange", 100, 0.93)
insert_row("Watermelon", 132, 0.40)
insert_row("Apple", 253, 0.68)
insert_row("Banana", 105, 0.51)
"""
print(view_rows())