from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    in1 = browser.find_element(By.NAME, "firstname")
    in1.send_keys("Polina")

    in2 = browser.find_element(By.NAME, "lastname")
    in2.send_keys("Polinova")

    in3 = browser.find_element(By.NAME, "email")
    in3.send_keys("p@mail.com")

    in4 = browser.find_element(By.ID, "file")
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.txt')
    in4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

