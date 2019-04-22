import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_admin_AddService(self):
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
        driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[3]/a").click()
        time.sleep(1)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/service/create/")
        select = Select(driver.find_element_by_xpath("//*[@id='id_cust_name']"))
        select.select_by_index(2)
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Food Prep/Delivery")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("TEST")
        elem = driver.find_element_by_id("id_location")
        elem.send_keys("TEST")
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("150")
        time.sleep(2)
        elem = driver.find_element_by_class_name("save")
        elem.click()
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/service_list")
        time.sleep(5)
    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

