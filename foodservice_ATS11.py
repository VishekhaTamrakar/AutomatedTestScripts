import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_admin_Product_Delete(self):
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
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/product_list")
        time.sleep(1)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/product/create/")
        select = Select(driver.find_element_by_xpath("//*[@id='id_cust_name']"))
        select.select_by_index(2)
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("TEST For Delete")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("TEST For Delete")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("50")
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys("150")
        time.sleep(2)
        elem = driver.find_element_by_class_name("save")
        elem.click()
        time.sleep(2)
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/product_list")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div[3]/table/tbody/tr[4]/td[10]/a").click()
        time.sleep(2)
        delete_alert = driver.switch_to.alert
        delete_alert.accept()
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/product_list")
        time.sleep(2)
    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

