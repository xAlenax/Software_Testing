from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Start Chrome browser
driver = webdriver.Chrome()

# Step 2: Open your local Todo app
driver.get("file:////Users/macbook/Desktop/Software Testing/todo-list-app/index.html")

# Step 3: Maximize window
driver.maximize_window()

# Step 4: Find input field and button
task_input = driver.find_element(By.ID, "taskInput")
add_button = driver.find_element(By.XPATH, "//button[text()='Add Task']")

# Step 5: Enter a task
task_input.send_keys("Buy groceries")

# Step 6: Click Add Task
add_button.click()

# Step 7: Wait for the task to appear
wait = WebDriverWait(driver, 10)
new_task = wait.until(
    EC.presence_of_element_located((By.XPATH, "//ul[@id='taskList']/li"))
)

# Step 8: Assertion (check if task is added)
assert "Buy groceries" in new_task.text

print("✅ Test Passed: Task added successfully!")

# Step 9: Close browser
user_input = input("Press 'q' to close the browser: ")

if user_input.lower() == 'q':
    driver.quit()
# When you see: Press 'q' to close the browser:
# Type:q
# Press Enter

