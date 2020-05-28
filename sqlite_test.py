import sqlite3
import random
import timeit


def insert(number):
    con = sqlite3.connect('test.db')
    cursor_obj = con.cursor()

    try:
        with con:
            query = 'INSERT INTO table_{0} (number) VALUES (?)'.format(random.randint(1, 3))
            values = (number,)
            cursor_obj.execute(query, values)

        con.close()

    except sqlite3.Error as e:
        print('Insert exception. {}'.format(e))


def get_by_number(number):
    con = sqlite3.connect('test.db')
    cursor_obj = con.cursor()

    try:
        query1 = 'SELECT * FROM table_1 WHERE number = ?'
        query2 = 'SELECT * FROM table_1 WHERE number = ?'
        query3 = 'SELECT * FROM table_1 WHERE number = ?'
        value = (number,)
        cursor_obj.execute(query1, value, )
        cursor_obj.execute(query2, value, )
        cursor_obj.execute(query3, value, )

        query_result = cursor_obj.fetchall()

        con.close()

        return query_result

    except sqlite3.Error as e:
        print('Select exception. {}'.format(e))


def delete_tables():
    con = sqlite3.connect('test.db')
    cursor_obj = con.cursor()

    try:
        with con:
            query = 'DELETE FROM table_1'
            cursor_obj.execute(query)
            query = 'DELETE FROM table_2'
            cursor_obj.execute(query)
            query = 'DELETE FROM table_3'
            cursor_obj.execute(query)

    except sqlite3.Error as e:
        print('Truncate exception. {}'.format(e))


# Clearing tables for a new run
delete_tables()

start = timeit.default_timer()
for i in range(1000):
    insert(i)

print('Write time: ', (timeit.default_timer() - start) / 1000)

start = timeit.default_timer()
for i in range(1000):
    print(get_by_number(i))

print('Write time: ', (timeit.default_timer() - start) / 1000)
