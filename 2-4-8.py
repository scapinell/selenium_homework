from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    
    book_button = browser.find_element(By.ID, "book")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    book_button.click()
    
    element_x = browser.find_element_by_id('input_value')
    x = int(element_x.text)
    y = calc(x)
    
    answer_form = browser.find_element_by_id('answer')
    answer_form.send_keys(y)
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
