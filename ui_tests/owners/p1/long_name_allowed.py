import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLongnameallowed():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_longnameallowed(self):
    # Test name: long_name_allowed

    self.driver.get("http://3.238.20.218:8080/")
    self.driver.set_window_size(1200, 969)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(2) span:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Add Owner").click()
    self.driver.find_element(By.ID, "firstName").click()
    self.driver.find_element(By.ID, "firstName").send_keys("oihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhroihwrf;ohwrflherlfiuherlfuhr")
    self.driver.find_element(By.ID, "lastName").click()
    self.driver.find_element(By.ID, "lastName").send_keys("1")
    self.driver.find_element(By.ID, "address").send_keys("1")
    self.driver.find_element(By.ID, "city").send_keys("1")
    self.driver.find_element(By.ID, "telephone").send_keys("1111111111")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, "h2")
    assert len(elements) == 0
  
