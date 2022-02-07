from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager


class Test_Setup:

    def __init__(self):
        ch_driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = ch_driver

    # yield
    # ch_driver.close()
