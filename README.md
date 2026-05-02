# Implementing a Basic Selenium Test for the Todo List App

This is a simple Todo List web app with automated tests created using Selenium and Python. The main goal was to practice writing and running automated end-to-end tests and to understand how Selenium works with a real web application.

## Files in this Project
- index.html          -> Main webpage
- script.js           -> Handles adding and managing tasks
- styles.css          -> Styling for the app
- test_todo.py        -> Basic Selenium test
- test_todo_debug.py  -> Test with logging and debugging
- error_debug.png     -> Screenshot from a failed test

## What You Need
- Python 3  
- Google Chrome  
- Selenium  

### Install Selenium:
pip install selenium  
ChromeDriver should be handled automatically by Selenium (no manual setup needed in most cases).  

### Running the App
You can just open index.html directly in your browser

### Running the Tests
**Step 1:** Update the file path  
In both test files, update this line: driver.get("file:///your/path/to/index.html")  

**Step 2:** Run the basic test  
python test_todo.py  
This test:  
- Opens the app  
- Adds a task ("Buy groceries")  
- Checks if it appears in the list  

**Step 3:** Run the debug test  
python test_todo_debug.py  
This test includes:  
- Logging (so you can see what’s happening step by step)  
- Error handling  
- Screenshot capture if something fails
- A negative test (trying to add an empty task)

## Debugging
- Logs will show in the terminal
- If something fails, a screenshot (error_debug.png) is saved
- Helps understand where things go wrong (like elements not loading)

## Notes
- Make sure the file path is correct, otherwise tests won’t run
- The app updates dynamically, so waits are important
- The task list is inside ul#taskList
