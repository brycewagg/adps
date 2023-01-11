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

class TestAdduser():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adduser(self):
    # Test name: add_user

    self.driver.get("http://3.238.20.218:8080/")
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(2) span:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Add Owner").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".form-group:nth-child(1) > .col-sm-10 > .help-inline")))
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(1) > .col-sm-10 > .help-inline")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(2) .help-inline")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(3) .help-inline")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(4) .help-inline")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form-group:nth-child(5) .help-inline")
    assert len(elements) > 0
  
