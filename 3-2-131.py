from selenium import webdriver
import unittest
import time

expectedOutput = "Congratulations! You have successfully registered!"

def registration(link):
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("1")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("2")
    input3 = browser.find_element_by_class_name('form-control.third')
    input3.send_keys("3")
    input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
    input4.send_keys("4")
    input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
    input5.send_keys("5")
    
    time.sleep(1)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    
    return welcome_text
    browser.quit()
    
class TestLink(unittest.TestCase):
    def test_link1(self):
        actualOutput = registration("http://suninjuly.github.io/registration1.html")
        self.assertEqual(actualOutput, expectedOutput, "expected success message")
        
    def test_link2(self):
        actualOutput = registration("http://suninjuly.github.io/registration2.html")
        self.assertEqual(actualOutput, expectedOutput, "expected success message")
        
if __name__ == "__main__":
    unittest.main()