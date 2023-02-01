import pyautogui
import time

# The time interval between clicks in seconds
click_interval = 0.5

try:
    while True:
        # Perform a left mouse click
        pyautogui.click()
        # Wait for the specified interval
        time.sleep(click_interval)
except KeyboardInterrupt:
    print("Auto-clicker stopped")
