# Task manager/viewer
#### https://youtu.be/LDwx4yon0Gk
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
#### 1.'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
1) id is the primary key that is in autoincrement of the database
#### 2.'task' TEXT NOT NULL
2) Task contains the title of the task, which is a required field
#### 3.'detail' TEXT
3) detail contains the details of the task, which is optional should the user decide to input the details
#### 4.'importance' BOOLEAN
4) importance, a boolean value allows the user to specify if the task is important
#### 5.'deadline' NUMERIC NOT NULL
5) deadline, used to store the deadline of the task in YYYY-MM-DD format
#### 6.'timestamp' INTEGER DEFAULT CURRENT_TIMESTAMP)
6) timestamp, contains the time that the task is created

### Layout.html
Contains the basic layout of the webpage created, which index.html and addtask.html are extended from. Majority of the layout is brought forward from PSET9.

### Index.html
The homepage of the web application. Displays all remaining tasks and also allows the user to mark “completed” in the top right hand corner which will remove the selected task from the database.

For the layout of displaying each task, I chose to do a collapsible as some of the details added may be longer than others which can ruin the layout of the webpage if I were to display all the details for all of the tasks. This makes the layout of the display of tasks cleaner and more functional.

Additionally the table can be arranged according to the task name, the importance, the deadline or the time that it was created, in ascending or descending order.

Some scripts are also added to make the table more interactive such as the sortablejs script and the collapsible script.

### Addtask.html
Allows the user to add new tasks into the database. Users are needed to add in a mandatory title, details of the task optionally, if the task is important and the deadline of the task.

### Styles.css
Contains the styles used in the html web pages, brought forward from PSET9

### Favicon.ico
An alien for the icon of the webpage.
