import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_forgot_your_password(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://maverickfoodservices-vishhy.herokuapp.com/accounts/password_reset/")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("vtamrakar@unomaha.edu")
        driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/p[2]/input")
        time.sleep(5)

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

