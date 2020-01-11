import time
import random

# import requetss 
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from lxml import html

print('WU-63 Customer Login (Generic Scenrio)Firefox')
class TestSelenium(unittest.TestCase):
   
    def test_email_confirmation_flow(self):
        #first_email_xpath = '//*[@id="mr_132702533"]/td[2]'

        signup_form_driver = webdriver.Firefox()
        signup_form_driver.maximize_window()
        # signup_form_driver.get('https://app.dev.worldunited.com/login')
        signup_form_driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[1]/div[2]/div/input').send_keys('mjkpzarf@grr.la')
        signup_form_driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[1]/div[3]/div[1]/div/input').send_keys('Password123')
        signup_form_driver.find_element_by_css_selector('#root > div > div > div > div > form > div.CardFooter.small > button.ui.fluid.primary.button').click()
        time.sleep(3)
        # Click on the first email in list
    
if __name__=='__main__':
    unittest.main()
