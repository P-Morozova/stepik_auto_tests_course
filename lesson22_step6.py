from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    button.click()

    time.sleep(5)

    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

