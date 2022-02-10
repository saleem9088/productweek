from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Scripts.test_Base import test_Base


class Home_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)

    SEARCH = (By.XPATH, "//input[@name='q']")
    SEARCH_ENTER = (By.XPATH, "//button[@type='submit']")

