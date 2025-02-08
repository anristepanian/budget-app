import copy
import os
import pandas as pd


class Analysis:
    """The Analysis class consists of essential methods for analysing the Habit data.

    Methods:
        currently_tracked_habits(db): Prints and returns a list of all currently tracked habits.
        same_periodicity_habits(db): Prints and returns a list of all habits with the same periodicity.
        habits_longest_streak(db): Prints and returns the longest run streak of all defined habits.
        given_habits_longest_streak(db, habit: str = None): Prints and returns the longest run streak for a given habit.
    """
    @staticmethod
    def currently_tracked_habits(db):
        """
        Prints and returns a list of all currently tracked habits.

        :param db: The database, to which you are connected.
        :type db: class
        :return: Returns a list of all currently tracked habits.
        :rtype: list
        """
        data = DB.get_habit_data(db)
        raw_data = copy.deepcopy(data)
        data.insert(0, ("Name", "Start date", "Expiration date", "Periodicity", "Status", "Current streak",
                        "Longest streak", "Last check date"))
        print('\n'.join(map(str, data)))
        return raw_data

    @staticmethod
    def same_periodicity_habits(db):
        """
        Prints and returns a list of all habits with the same periodicity.

        :param db: The database, to which you are connected.
        :type db: class
        :return: Returns a list of all habits with the same periodicity.
        :rtype: list
        """
        periodicity = input("What is the periodicity of a habit?\n")
        if periodicity != "Weekly" and periodicity != "Daily":
            return print(f"\nThere is no \"{periodicity}\" periodicity!\n")
        cur = db.cursor()
        cur.execute("""SELECT name, periodicity, status FROM habit
        WHERE periodicity = ?""", (periodicity,))
        select = cur.fetchall()
        raw_select = copy.deepcopy(select)
        select.insert(0, ("Name", "Periodicity", "Status"))
        print('\n'.join(map(str, select)))
        return raw_select

    @staticmethod
    def habits_longest_streak(db):
        """
        Prints and returns the longest run streak of all defined habits.

        :param db: The database, to which you are connected.
        :type db: class
        :return: Returns the longest run streak of all defined habits.
        :rtype: list
        """
        cur = db.cursor()
        cur.execute("""SELECT habit.name, habit.status, streak.longest_streak FROM habit
        LEFT JOIN streak on habit.habit_id = streak.habit_id""")
        select = cur.fetchall()
        raw_select = copy.deepcopy(select)
        select.insert(0, ("Name", "Status", "Longest streak"))
        print('\n'.join(map(str, select)))
        return raw_select

    @staticmethod
    def given_habits_longest_streak(db, habit: str = None):
        """
        Prints and returns the longest run streak for a given habit.

        :param db: The database, to which you are connected.
        :type db: class
        :param habit: The name of a habit, but if the name is not passed, it should be entered in the function
        (default None).
        :type habit: str
        :return: Returns the longest run streak for a given habit.
        :rtype: list
        """
        if not habit:
            habit = input("What is the name of a habit?\n")
        cur = db.cursor()
        cur.execute("""SELECT habit.name, habit.status, streak.longest_streak FROM habit
        LEFT JOIN streak on habit.habit_id = streak.habit_id
        WHERE habit.name = ?""", (habit,))
        try:
            select = cur.fetchall()
        except TypeError:
            return print(f"\nHabit with {habit} name doesn't exist!\n")
        raw_select = copy.deepcopy(select)
        select.insert(0, ("Name", "Status", "Longest streak"))
        print('\n'.join(map(str, select)))
        return raw_select
