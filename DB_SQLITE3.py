import sqlite3

def init_db():

    create_table = """
    CREATE TABLE IF NOT EXISTS MOVIES(
        id INTEGER PRIMARI KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        production_year INTEGER NULL
    )
    """

    seed_data = """
    INSERT INTO MOVIES (name, production_year)
    VALUES ('Gospodar prstenova', 2001),
            ('Hobit', 2007),
            ('druzba pere kvrzice', 1984),
            ('the godfather', 1995)
    """


    try:
        db_connection = sqlite3.connect ('py-tinkter_sqlite.db')
        cursor = db_connection.cursor()

        cursor.execute(create_table)
        db_connection.commit()

        cursor.execute(seed_data)
        db_connection.commit()

        cursor.close()

    except sqlite3.Error as db_error:
        print(f'dogodila se geske: {db_error}')
    except Exception as ex:
        print(f'dogodila se geske: {ex}')

    finally:
        if db_connection:
            db_connection.close()





def get_data():
    select_table= """
        SELECT * FROM MOVIES
    """

    record_set = None

    try:
        db_connection = sqlite3.connect ('py-tinkter_sqlite.db')
        cursor = db_connection.cursor()

        cursor.execute(select_table)
        record_set=cursor.fetchall()

        cursor.close()

    except sqlite3.Error as db_error:
        print(f'dogodila se geske: {db_error}')
    except Exception as ex:
        print(f'dogodila se geske: {ex}')

    finally:
        if db_connection:
            db_connection.close()

        return record_set
