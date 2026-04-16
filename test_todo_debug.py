import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting debugging test...")

try:
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/diego/Downloads/todo-list-app/Software_Testing/index.html")
    driver.maximize_window()
    logging.info("Page loaded")

    # Input + button
    task_input = driver.find_element(By.ID, "taskInput")
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Task']")

    # Intentionally test a problematic case (YOUR debugging test)
    task_input.send_keys("")    # ← empty on purpose to trigger alert
    logging.info("Entered empty task")

    add_button.click()
    logging.info("Clicked Add Task")

    # ---------------------------------------------------------
    # Handle unexpected alerts
    # ---------------------------------------------------------
    try:
        alert = driver.switch_to.alert
        logging.warning(f"Alert detected: {alert.text}")
        alert.accept()
        logging.info("Alert accepted")
    except:
        logging.info("No alert appeared")

    # ---------------------------------------------------------
    # Dynamic element waiting
    # ---------------------------------------------------------
    wait = WebDriverWait(driver, 5)
    try:
        task = wait.until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='taskList']/li"))
        )
        logging.info(f"Task found: {task.text}")
    except:
        logging.info("Task did not appear (expected for empty input)")

    logging.info("Debug test complete")

except Exception as e:
    logging.error(f"ERROR: {e}")
    driver.save_screenshot("error_debug.png")
    logging.info("Saved debug screenshot")

finally:
    driver.quit()
    logging.info("Browser closed")