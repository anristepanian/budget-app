import sqlite3


class DB:
    """The DB class consists of essential methods for interacting with database.

    Methods:
        get_db(name="main.db"): Creates a connection with a database.
        create_tables(db): Creates the Habit, Streak and Track tables in the database, if they don't exist already.
    """
    @classmethod
    def get_db(cls, name="main.db"):
        """
        Creates a connection with a database.

        :param name: Name of a database.
        :type name: str
        :return: Returns the database.
        :rtype: class
        """
        db = sqlite3.connect(name, timeout=5)
        cls.create_tables(db)
        return db

    @staticmethod
    def create_tables(db):
        """
        Creates the Habit, Streak and Track tables in the database, if they don't exist already.

        :param db: The database, to which you are connected.
        :type db: class
        :return: None
        """
        cur = db.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS actions (
            date TEXT,
            income REAL,
            income_type TEXT,
            expense REAL,
            expense_type TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS report (
        year INTEGER PRIMARY KEY,
        january REAL,
        february REAL,
        march REAL,
        april REAL,
        may REAL,
        june REAL,
        july REAL,
        august REAL,
        september REAL,
        october REAL,
        november REAL,
        december REAL,
        total REAL
        )
        """)

        db.commit()

    @staticmethod
    def add_month(db, year, months: list):
        cur = db.cursor()
        cur.execute("""SELECT year FROM report
        WHERE year = ?""", (year,))
        if not cur.fetchall():
            cur.execute("""INSERT INTO
            report(year, january, february, march, april, may, june, july, august, september, october, november,
            december)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (year, *months))
        else:
            cur.execute("""SELECT * FROM report
            WHERE year = ?""", (year,))
            values = cur.fetchall()[0][1:-1]
            new_values = [a + b for a, b in zip(months, values)]
            cur.execute("""UPDATE report
            SET january = ?, february = ?, march = ?, april = ?, may = ?, june = ?, july = ?, august = ?, september = ?,
            october = ?, november = ?, december = ?
            WHERE year = ?""", (*new_values, year))
        db.commit()

    @staticmethod
    def add_total(db, year):
        cur = db.cursor()
        cur.execute("""SELECT * FROM report
        WHERE year = ?""", (year,))
        values = sum(cur.fetchall()[0][1:-1])
        cur.execute("""UPDATE report
        SET total = ?
        WHERE year = ?""", (values, year))

    @staticmethod
    def add_action(db, date, income, income_type, expense, expense_type):
        cur = db.cursor()
        cur.execute("""INSERT INTO
        actions(date, income, income_type, expense, expense_type)
        VALUES(?, ?, ?, ?, ?)""", (date, income, income_type, expense, expense_type))

    @classmethod
    def delete_income(cls, db, date):
        cur = db.cursor()
        cur.execute("""UPDATE actions
        SET income = 0, income_type = 'NULL'
        WHERE date = ?""", (date,))
        cls.delete_action(db)

    @classmethod
    def delete_expense(cls, db, date):
        cur = db.cursor()
        cur.execute("""UPDATE actions
        SET expense = 0, expense_type = 'NULL'
        WHERE date = ?""", (date,))
        cls.delete_action(db)

    @staticmethod
    def delete_action(db):
        cur = db.cursor()
        cur.execute("""DELETE FROM actions
        WHERE income = 0 AND income_type = 'NULL'
        AND expense = 0 AND expense_type = 'NULL'""")
