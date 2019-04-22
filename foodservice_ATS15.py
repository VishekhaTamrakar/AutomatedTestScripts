import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_admin_AddCustomer(self):
        user = "Instructor"
        pwd = "Vishekha@123*"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/admin/login/?next=/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/admin/crm/customer/add/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Vishekha Tamrakar")
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("MIS")
        elem = driver.find_element_by_id("id_role")
        elem.send_keys("TEST")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("vtamrakar@unomaha.edu")
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("PKI")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("5064 S 86th and pkwy apt 10")
        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("15")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("NE")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68127")
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("4029959072")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id='customer_form']/div/div/input[1]")
        elem.click()
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/customer_list")
        time.sleep(2)
    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

