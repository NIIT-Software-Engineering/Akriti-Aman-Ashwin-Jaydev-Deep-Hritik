# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')

class Invoicegeneration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_invoicegeneration(self):
        driver = self.driver
        driver.get(self.base_url + "/accounts/login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("Admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password123")
        driver.find_element_by_xpath("//input[@value='Submit']").click()
        driver.find_element_by_xpath("//li[4]/a/h2").click()
        driver.find_element_by_id("id_Customer_name").clear()
        driver.find_element_by_id("id_Customer_name").send_keys("Ashwin")
        driver.find_element_by_id("id_Quantity").clear()
        driver.find_element_by_id("id_Quantity").send_keys("12")
        driver.find_element_by_id("id_Dues").clear()
        driver.find_element_by_id("id_Dues").send_keys("10")
        driver.find_element_by_id("id_Amount_given").clear()
        driver.find_element_by_id("id_Amount_given").send_keys("150")
        driver.find_element_by_id("id_Payment_Date").clear()
        driver.find_element_by_id("id_Payment_Date").send_keys("12/12/12")
        driver.find_element_by_xpath("//input[@value='Generate']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
