#!/usr/bin/python3

import MySQLdb

def test_create_state_command():

    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="Riverwater1993_", db="airbnb_db")

    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM states")
    initial_state = cursor.fetchone()[0]

    cursor.execute("INSERT INTO states (name) VALUES ('Houston')")

    db.commit()

    cursor.execute("SELECT COUNT(*) FROM states")
    updated_state = cursor.fetchone()[0]
    print(f"Initial State: {initial_state}")
    print(f"Updated State: {updated_state}")

    assert updated_state == initial_state + 1, "Test failed: The expected change did not occur."

    db.close()

test_create_state_command()

