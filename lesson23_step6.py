from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)

    b = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    b.click()

    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

