from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Scripts.test_Base import test_Base


class Logout_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)

    logoutTestuser = (By.XPATH, "//*[text()='Test']")
    LOGOUT = (By.XPATH, "//div[text()='Logout']")
    LOGIN = (By.XPATH, "//a[text()='Login']")

    def logout_operation(self):
        log = test_Base.getLogger()
        log.info("Navigating to the logout section")
        self.Hover_operation(self.logoutTestuser)
        self.click_operation(self.LOGOUT)
        text = self.get_text_from_locator(self.LOGIN)
        assert "Login" == text
        log.info("User is successfully logged out from the account")