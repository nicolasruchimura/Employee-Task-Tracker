# Employees Tasks Tracker
1. Purpose: create a simple web-based task management tool for small teams, allowing employees to add and delete tasks.
2. Technologies used:
        - Frontend: HTML, CSS, JavaScript (Vanilla)
        - Backend:	Python + Flask (Microframework)
        - Database:	SQLite (Built-in with Python)
        - Deployment:	Localhost (Tested on Flask dev server)
3. System Architecture
       User (Browser) → Flask Server (Python) → SQLite Database
Code Flow

    User Interaction:

        Submits a task via the HTML form (index.html).

        Clicks "X" to delete a task.

    Backend Logic (app.py):

        Add Task: Flask saves the task to SQLite.

        Delete Task: Removes the task from the database.

    Database:

        Table schema: tasks(id INTEGER PRIMARY KEY, task TEXT).

   
