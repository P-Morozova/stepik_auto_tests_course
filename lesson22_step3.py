from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    el1 = browser.find_element(By.ID, "num1")
    num1 = int(el1.text)

    el2 = browser.find_element(By.ID, "num2")
    num2 = int(el2.text)

    x = num1 + num2
    print(x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

