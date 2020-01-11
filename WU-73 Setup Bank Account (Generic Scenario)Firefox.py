import time
import random

# import requetss 
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from lxml import html

print('WU-73 Setup Bank Account (Generic Scenario)Firefox')
class TestSelenium(unittest.TestCase):

    def test_email_confirmation_flow(self):
        #first_email_xpath = '//*[@id="mr_132702533"]/td[2]'
        value = random.randint(999999999,99999999999999999)
        print ("Using the following number as the the bank account name:",value,) 

        signup_form_driver = webdriver.Firefox()
        signup_form_driver.maximize_window()
        # signup_form_driver.get('https://app.dev.worldunited.com/login')
        signup_form_driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[1]/div[2]/div/input').send_keys('hubertbristow@gmail.com')
        signup_form_driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/div[1]/div[3]/div[1]/div/input').send_keys('L2a4qnbL2')
        signup_form_driver.find_element_by_css_selector('#root > div > div > div > div > form > div.CardFooter.small > button.ui.fluid.primary.button').click()
        time.sleep(5)

        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[1]/div[2]/a/div/div/span').click()
        time.sleep(3)
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[1]/button').click()
        time.sleep(3)
        signup_form_driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/div/input').send_keys(value)
        time.sleep(3)
        signup_form_driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/button').click()
        time.sleep(3)

        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[2]/div[1]/div/div/input').send_keys('Bob')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[1]/div[2]/div[1]/input').send_keys('Hong Kong')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[2]/div[2]/div[1]/input').send_keys('HK')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[6]/div/button').click()
        time.sleep(3)

        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[1]/div[2]/div[1]/input').send_keys('HSBC')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[2]/div[2]/div[1]/input').send_keys('Hong Kong')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[1]/div[3]/div[1]/input').send_keys('10 Hennessy Rd')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[2]/div[3]/div[1]/input').send_keys('HK')
        signup_form_driver.execute_script("window.scrollBy(0, 300);")
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[1]/div[5]/div[1]/input').send_keys('HK')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[6]/div/button').click()
        time.sleep(3)

        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[2]/div[2]/div[2]/div/input').send_keys('HSBC')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[1]/div[2]/div[1]/input').send_keys('Hong Kong')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[2]/div[2]/div[1]/input').send_keys('Hong Kong')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[1]/div[3]/div[1]/input').send_keys('Hong Kong')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[3]/div[4]/div[2]/div[3]/div[1]/input').send_keys('HK')
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[6]/div/button').click()
        time.sleep(3)
        
        signup_form_driver.execute_script("window.scrollBy(0, 300);")
        signup_form_driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[6]/div/button').click()
        time.sleep(3)
        signup_form_driver.quit()

if __name__=='__main__':
    unittest.main()

