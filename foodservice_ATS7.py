import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_admin_EditService(self):
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
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/service_list")
        time.sleep(1)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/service/3/edit/")
        driver.find_element_by_id("id_service_category").clear()
        driver.find_element_by_id("id_service_category").send_keys("Edit Done")
        time.sleep(1)
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("Edit Done")
        time.sleep(1)
        driver.find_element_by_id("id_location").clear()
        driver.find_element_by_id("id_location").send_keys("Edit Done")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/button").click()
        time.sleep(1)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/service_list")
    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

