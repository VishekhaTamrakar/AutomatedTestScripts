import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_admin_EditCustomer(self):
        user = "vish"
        pwd = "1instructor1"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/customer_list")
        time.sleep(1)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/customer/2/edit/")
        driver.find_element_by_id("id_organization").clear()
        driver.find_element_by_id("id_organization").send_keys(" Edit Done")
        time.sleep(1)
        driver.find_element_by_id("id_role").clear()
        driver.find_element_by_id("id_role").send_keys(" Edit Done")
        time.sleep(1)
        driver.find_element_by_id("id_bldgroom").clear()
        driver.find_element_by_id("id_bldgroom").send_keys(" Edit Done")
        time.sleep(2)
        elem = driver.find_element_by_class_name("save")
        elem.click()
        time.sleep(1)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/customer_list")
    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

