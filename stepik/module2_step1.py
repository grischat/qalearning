from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x, y):
        return str(int(x) + int(y))


    first_num = browser.find_element_by_id("num1").text
    second_num = browser.find_element_by_id("num2").text
    summary = calc(first_num, second_num)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_visible_text(str(summary))
    clicking = browser.find_element_by_tag_name('button')
    clicking.click()

finally:
    time.sleep(5)
    browser.quit()
