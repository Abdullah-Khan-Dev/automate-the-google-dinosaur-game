from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import cv2

# Set up the Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://elgoog.im/t-rex/")

# Start the game by simulating a space bar press
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.SPACE)

# Give some time to start the game
time.sleep(2)

# Define a function to capture the game screen
def get_game_screenshot():
    screenshot = driver.get_screenshot_as_png()
    image = np.asarray(bytearray(screenshot), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

# Define the region where the T-Rex runs and obstacles appear
x, y, width, height = 130, 240, 60, 10  # You may need to adjust these values based on your screen resolution

# Main game loop
while True:
    screenshot = get_game_screenshot()
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    region = gray[y:y+height, x:x+width]
    _, thresh = cv2.threshold(region, 200, 255, cv2.THRESH_BINARY_INV)

    # Detect obstacles by checking for white pixels in the thresholded image
    if np.sum(thresh) > 0:
        body.send_keys(Keys.SPACE)
        time.sleep(0.1)  # Add a small delay to avoid pressing the space bar too frequently

    # Add a small delay to control the game speed
    time.sleep(0.05)
