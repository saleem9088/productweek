import logging
from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base

class User_Registration_Page(Base_Page):
    USER_NAME_TEXTFIELD = (By.XPATH, "//input[@placeholder='Enter username']")
    EMAIL_ID_TEXTFIELD = (By.XPATH, "//input[@placeholder='Enter email address']")
    FIRST_NAME_TEXTFIELD = (By.XPATH, "//input[@placeholder='Enter first name']")
    LAST_NAME_TEXTFIELD = (By.XPATH, "//input[@placeholder='Enter last name']")
    PHONE_NO_TEXTFIELD = (By.XPATH, "//input[@placeholder='Enter 10 digit phone number']")
    BATCH_DROPDOWN = (By.ID, "batchId")
    PASSWORD_TEXTFIELD = (By.XPATH, "//input[@placeholder='Enter password']")
    CONFIRM_PASSWORD_TEXTFIELD = (By.XPATH, "//input[@placeholder='Enter same password']")
    SIGNUP_BUTTON = (By.XPATH, "//button")

    def __init__(self, driver):
        super().__init__(driver)
        dict_d = {}
        dict_d = Test_Data.getTestData(self, "BaseData", "test_URL")
        self.driver.get(dict_d["name"])

    #Finction for registration
    def registration(self):
        log = test_Base.getLogger()

        dict_d = {}

        dict_d = Test_Data.getTestData(self, "Registration", "test_Registration_hashirama")

        #Adding the necessary details
        self.send_keys_operation(User_Registration_Page.USER_NAME_TEXTFIELD, dict_d["name"])
        log.info("Username is passed")

        self.send_keys_operation(User_Registration_Page.EMAIL_ID_TEXTFIELD, dict_d["email"])
        log.info("Email is entered")

        self.send_keys_operation(User_Registration_Page.FIRST_NAME_TEXTFIELD, dict_d["firstname"])
        log.info("First name is entered")

        self.send_keys_operation(User_Registration_Page.LAST_NAME_TEXTFIELD, dict_d["lastname"])
        log.info("Last name is entered")

        self.send_keys_operation(User_Registration_Page.PHONE_NO_TEXTFIELD, dict_d["phone"])
        log.info("Phone number is entered")

        self.dropdown_operation(User_Registration_Page.BATCH_DROPDOWN).select_by_visible_text(dict_d["batch"])
        log.info("Batch is selected")

        self.send_keys_operation(User_Registration_Page.PASSWORD_TEXTFIELD, dict_d["newPassword"])
        log.info("Password is entered")

        self.send_keys_operation(User_Registration_Page.CONFIRM_PASSWORD_TEXTFIELD, dict_d["confirmPassword"])
        log.info("Password is confirmed")

        self.click_operation(User_Registration_Page.SIGNUP_BUTTON)
        log.info("Signup button is clicked")

        dict_d1 = {}
        dict_d1 = Test_Data.getTestData(self, "BaseData", "test_LoginPageTitle")

        assert self.get_title() == dict_d1["name"]
        log.info("Title is verified. User is registered in successfully")