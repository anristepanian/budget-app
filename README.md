# My Budget Track App / Project

Creating good habits and breaking bad ones is no easy task. To keep track of certain habits or achieving personal goals, more and more people rely on so-called habit trackers to help them throughout the day.<br>
The Habit Track application helps users build and maintain habits, track progress, and stay motivated.<br>
The core idea is to provide a simple yet feature-rich application for creating, managing, and analyzing habits. However, it is important to keep in mind the limited advanced database capabilities.<br>
Python’s OOP simplifies maintainability, while SQLite3 provides a lightweight, portable backend.

## Criteria

- The Habit Track application was built using `Python version 3.11.5`.
- The code was documented using the `Sphinx (reStructuredText)` style.
- The object-oriented programming was used to create the Habit Track application.
- Users are able to create habits with two habit periods, namely `Weekly` and `Daily`.
- The Habit Track application already has 5 predefined habits.
	1. Documenting code.
	2. Naming variables properly.
	3. Not drinking coffee.
	4. Not skipping leg day.
	5. Writing OOP code.
- The Habit Track application tracks when a habit has been created, and the date and time the habit tasks have been completed.
- For each predefined habit, there are provided examples of tracking data for a period of at least 4 weeks.
- The data are stored in the backend database via using a relational database solution using tool `sqlite3`.
- The Habit Track application has an `Analytics` module that allows users to analyze their habits. It allows users to:
	1. return a list of all currently tracked habits,
	2. return a list of all habits with the same periodicity,
	3. return the longest run streak of all defined habits,
	4. and return the longest run streak for a given habit.
- The Habit Track application has a command line interface (CLI) that allows users to create, delete and analyze their habits.
- The critical parts of the Habit Track application, in particular the validity of the habit tracking components and the analytics module, can be tested by providing a unit test suite that can be run following the instructions provided with in `Tests` paragraph.

## User Actions

- A **user** can define multiple habits in the application. A habit has a task specification and a periodicity.
- A *task* can be completed, i.e., “checked-off”, by a **user** at any point in time.
- Each task needs to be checked-off at least once during the period the **user** defined for the respective habit. If a **user** misses to complete a habit during the specified period, the **user** is said to break the habit.
- If a **user** manages to complete the task of a habit x consecutive periods in a row, I.e., without breaking the habit, we say that the user established a *streak of x periods*. For instance, if a **user** wants to work out every day and does so for two full weeks, they establish a 14-day streak of working out.
- The habits **users** enter in the app are not only stored but can also be analyzed. **Users** want answers to several questions like: what’s my longest habit streak? What's the list of my current daily habits? With which habits did I struggle most last month?

## Installation

```commandline
pip install -r requirements.txt
```

## Usage

Start

```commandline
python main.py
```

and follow the instructions on the screen.

## Tests

Write

```commandline
pytest .
```

in the command line, in order to test the program.