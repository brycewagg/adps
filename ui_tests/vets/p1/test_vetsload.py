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

class TestVetsload():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_vetsload(self):
    # Test name: vets_load

    self.driver.get("http://3.238.20.218:8080/")
    self.driver.set_window_size(1200, 969)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) span:nth-child(2)").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, "h2")
    assert len(elements) > 0
  
