import logging

from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


class User_Test_LoginPage1(Base_Page):
    USER_NAME_TEXTFIELD = (By.XPATH, "//input[@formcontrolname='username']")
    PASSWORD_TEXTFIELD = (By.XPATH, "//input[@formcontrolname='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login ']")
    CREATE_NEW_ACCOUNT_BUTTON = (By.XPATH, "//a[text()=' Create a new account ']")
    EMAIL_TEXT = (By.XPATH, "//span[@class='desgination']")
    log = test_Base.getLogger()

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver
        dict_d = {}
        dict_d = Test_Data.getTestData(self, "BaseData", "test_URL")
        self.driver.get(dict_d["name"])

    def login1(self):
        log = test_Base.getLogger()
        log.info("Login method is started")
        dict_d = {}

        dict_d = Test_Data.getTestData(self, "Registration", "test_Registration_kakashi")
        log.info(dict_d)

        self.send_keys_operation(User_Test_LoginPage1.USER_NAME_TEXTFIELD, dict_d["name"])
        log.info("User name is filled")

        self.send_keys_operation(User_Test_LoginPage1.PASSWORD_TEXTFIELD, dict_d["newPassword"])
        log.info("Password is entered")

        self.click_operation(User_Test_LoginPage1.LOGIN_BUTTON)
        log.info("Login button is clicked")
        log.info("User is loged in successfully")

        # Verification of the user account after logging in
        email = self.get_text_from_locator(User_Test_LoginPage1.EMAIL_TEXT)
        assert email == dict_d["email"]
        log.info("User is logged into his account successfully")


    def login1(self):
        log = test_Base.getLogger()
        log.info("Login method is started")
        dict_d = {}

        dict_d = Test_Data.getTestData(self, "Registration", "test_login_firdose")
        log.info(dict_d)

        self.send_keys_operation(User_Test_LoginPage1.USER_NAME_TEXTFIELD, dict_d["name"])
        log.info("User name is filled")

        self.send_keys_operation(User_Test_LoginPage1.PASSWORD_TEXTFIELD, dict_d["newPassword"])
        log.info("Password is entered")

        self.click_operation(User_Test_LoginPage1.LOGIN_BUTTON)
        log.info("Login button is clicked")
        log.info("User is loged in successfully")

        # Verification of the user account after logging in
        email = self.get_text_from_locator(User_Test_LoginPage1.EMAIL_TEXT)
        assert email == dict_d["email"]
        log.info("User is logged into his account successfully")

    def click_create_account_button(self):
        self.click_operation(User_Test_LoginPage1.CREATE_NEW_ACCOUNT_BUTTON)
        logging.info("create new button is clicked")