from habit_track import DbHabit
from db import DB
from analyse import Analysis
import os

# remove_db is needed to remove the previously created test.db, in case the teardown_method wasn't called itself.
remove_db = False

if remove_db:
    # if the remove_db is True, os will remove the "test.db".
    os.remove("test.db")
else:
    class TestHabit:
        """The TestHabit class is used to test the program.

        The Methods:
            setup_method(): Creates the "test.db", inserts data about habit to the "test.db" directly without calling
            the DbHabit class.
            test_habit(): Creates a habit through DbHabit class, inserts and analysis data.
            teardown_method(): Closes and removes the "test.db".
        """
        def setup_method(self):
            """
            Creates the "test.db", inserts data about habit to the "test.db" directly without calling the DbHabit class.

            :return: None
            """
            self.db_title = "test.db"
            self.db = DB.get_db(name=self.db_title)

            DB.add_habit(self.db, "test_habit", "test_description", "2025-01-20", "2025-01-30", "Daily")
            DB.habit_check(self.db, "test_habit", True, "2025-01-20")

        def test_habit(self):
            """
            Creates a habit through DbHabit class, inserts and analysis data.

            :return: None
            """
            habit = DbHabit("test_habit_1", "test_description_1", "2025-01-20", "2025-01-31", "Daily")
            habit.store(db=self.db)
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-20")
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-22")
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-23")
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-24")
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-25")
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-27")
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-28")
            habit.add_habit_check(db=self.db, check=True, check_date="2025-01-29")

            longest_streak = Analysis.given_habits_longest_streak(self.db, "test_habit_1")[0][2]
            assert longest_streak == 4

            count = DB.get_habit_data(self.db)
            assert len(count) == 2

        def teardown_method(self):
            """
            Closes and removes the "test.db".

            :return: None
            """
            DB.db_close(self.db)
            os.remove(self.db_title)
