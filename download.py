import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Calling the Browser
driver = webdriver.Chrome()

# Insert Video URL
url = 'https://story.snapchat.com/p/db234cbd-4d19-49f0-a8e1-dda5aed9beba/1575826619181056'

# Opening the browser
driver.get("http://127.0.0.1:5000/")

# Pausing for a 5 seconds
time.sleep(5)
  
# Typing into input field and hitting enter
driver.find_element(By.CLASS_NAME, "form-control").send_keys(url, 
    Keys.ENTER
)
    
# Pausing again
time.sleep(5)

download = driver.find_elements(By.CLASS_NAME, "download")

for link in download:
    get = link.click()
    time.sleep(5)
