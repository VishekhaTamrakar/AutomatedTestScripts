import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

class foodservice_ATS1(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()

    def test_add_customer_using_excel(self):
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
        driver.find_element_by_xpath("//*[@id='content-main']/div[2]/table/tbody/tr[1]/th/a").click()
        with open('/Users/vishhy/Desktop/Testing.csv') as csvDATAFile:
            csvReader = csv.DictReader(csvDATAFile)
            for row in csvReader:
                driver.find_element_by_xpath("//*[@id='content-main']/ul/li/a").click()
                time.sleep(1)
                elem = driver.find_element_by_id('id_cust_name')
                elem.send_keys(row['name'])
                elem = driver.find_element_by_id('id_organization')
                elem.send_keys(row['organization'])
                elem = driver.find_element_by_id('id_role')
                elem.send_keys(row['role'])
                elem = driver.find_element_by_id('id_email')
                elem.send_keys(row['email'])
                elem = driver.find_element_by_id('id_bldgroom')
                elem.send_keys(row['building'])
                elem = driver.find_element_by_id('id_address')
                elem.send_keys(row['address'])
                elem = driver.find_element_by_id('id_account_number')
                elem.send_keys(row['account'])
                elem = driver.find_element_by_id('id_city')
                elem.send_keys(row['city'])
                elem = driver.find_element_by_id('id_state')
                elem.send_keys(row['state'])
                elem = driver.find_element_by_id('id_zipcode')
                elem.send_keys(row['zipcode'])
                elem = driver.find_element_by_id('id_phone_number')
                elem.send_keys(row['contact'])
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='customer_form']/div/div/input[1]").click()
                time.sleep(2)

        def teardown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()