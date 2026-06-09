# utils/database.py

import sqlite3

DATABASE_NAME = "customer_analytics.db"


def create_connection():

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    return conn


def create_tables():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(

        CustomerID INTEGER PRIMARY KEY,

        Gender TEXT,

        Age INTEGER,

        AnnualIncome REAL,

        SpendingScore REAL,

        PurchaseCount INTEGER,

        Revenue REAL,

        Churn INTEGER

    )
    """)

    conn.commit()

    conn.close()


def insert_customer(data):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO customers(
        CustomerID,
        Gender,
        Age,
        AnnualIncome,
        SpendingScore,
        PurchaseCount,
        Revenue,
        Churn
    )
    VALUES(?,?,?,?,?,?,?,?)
    """, data)

    conn.commit()

    conn.close()


def get_all_customers():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers"
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_customer(customer_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM customers
        WHERE CustomerID=?
        """,
        (customer_id,)
    )

    customer = cursor.fetchone()

    conn.close()

    return customer


def delete_customer(customer_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM customers
        WHERE CustomerID=?
        """,
        (customer_id,)
    )

    conn.commit()

    conn.close()


def count_customers():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM customers"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count