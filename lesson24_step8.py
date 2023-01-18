from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book");
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

