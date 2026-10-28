# Smart To-Do List Assistant

A command-line task management application built with Python. It helps users organize daily tasks, track their completion status, and store task data permanently using JSON.

## Features

- **Add Tasks:** Create new tasks with a task name.
- **View Tasks:** Display all tasks with their current status.
- **Complete Tasks:** Mark pending tasks as completed.
- **Delete Tasks:** Remove tasks that are no longer needed.
- **Persistent Storage:** Save and load tasks using a JSON file.
- **Input Validation:** Handle invalid task numbers and unexpected input without crashing.

## Technologies Used

- Python 3
- JSON
- Python file handling
- Exception handling
- Lists and dictionaries
- Functions and conditional statements

## Project Structure

```text
To-do-Assistant/
├── todo_assistant_.py
├── tasks.json
├── README.md
└── .gitignore
```

## Requirements

- Python 3 installed
- Visual Studio Code or another Python-compatible editor

## How to Run

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the application:

   ```bash
   python3 todo_assistant_.py
   ```

4. Choose an option from the menu to manage your tasks.

## How It Works

Tasks are stored as dictionaries inside a Python list. Each task contains a name and a completion status.

Example:

```json
[
    {
        "name": "Learn Python",
        "completed": false
    },
    {
        "name": "Build an AI agent",
        "completed": true
    }
]
```

The application uses JSON serialization to save tasks to `tasks.json` and load them when the program starts.

## Learning Outcomes

Through this project, I practised:

- Designing a menu-driven Python application
- Using lists and dictionaries to organize data
- Writing reusable functions
- Handling invalid input with `try` and `except`
- Reading and writing JSON files
- Implementing persistent data storage
- Testing application features and managing project files with Git

## Future Improvements

- Add task priorities and due dates
- Search and filter tasks
- Add task categories
- Build a graphical user interface
- Integrate an AI model to interpret natural-language task requests
- Add reminders and scheduling

## Author

Manan Goel

## Project Series

This project is part of my journey to learn Agentic AI through 50 practical projects, progressing from beginner programming concepts toward intelligent agents and autonomous workflows.