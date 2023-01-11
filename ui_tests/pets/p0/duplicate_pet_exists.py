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

class TestDuplicatepetexists():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_duplicatepetexists(self):
    # Test name: duplicate_pet_exists

    self.driver.get("http://3.238.20.218:8080/")
    self.driver.set_window_size(1200, 969)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(2) span:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(1)").click()
    self.driver.find_element(By.LINK_TEXT, "George Franklin").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.find_element(By.ID, "name").click()
    # TODO- Cleanup to allow for random name 
    self.driver.find_element(By.ID, "name").send_keys("Bend")
    self.driver.find_element(By.ID, "birthDate").send_keys("2001-01-01")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # Pet Added
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) > .col-sm-10 > .help-inline")
    assert len(elements) > 0
  
