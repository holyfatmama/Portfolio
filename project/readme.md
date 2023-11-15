# Task manager/viewer
#### <url>
#### Description:
For my CS50 Final project, I decided to make a task manager/scheduler/viewer as I constantly am figuring out what tasks are yet to be completed and have a hard time keeping track of them.
The project is coded in python using the Flask framework that was taught in week 9.
This project is fairly simple and there are 7 files in total:
#### 1. App.py (the main application)
#### 2. Tasks.db (database used to contain the tasks to keep track of completed and non completed tasks)
#### 3. Layout.html
#### 4. Index.html (main homepage and to keep track of incomplete tasks)
#### 5. Addtask.html (to add new tasks)
#### 6. Styles.css
#### 7. favicon.ico

### App.py
The main framework used in coding/developing this project. I chose this framework as I spent a lot of my time doing Problem Set 9 Finance and I think that this is a good choice as I can utilize a lot of the things I learnt before such as Javascript, HTML, CSS, Python and SQL.

### Tasks.db
The database to store the tasks are inside tasks.db

Which the structure is as such:
#### 1.'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#### 2.'task' TEXT NOT NULL,
#### 3.'detail' TEXT,
#### 4.'importance' BOOLEAN,
#### 5.'deadline' NUMERIC NOT NULL,
#### 6.'timestamp' INTEGER DEFAULT CURRENT_TIMESTAMP)

