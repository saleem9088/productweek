import logging

from Pages.User_Login_Page1 import User_Test_LoginPage1
from Pages.User_Registration_Page import User_Registration_Page
from Utilities.test_Base import test_Base


class Test_Registration_User(test_Base):

    def test_registration(self):
        logging.info("Registration function started")

        self.login=User_Test_LoginPage1(self.driver)
        self.reg=User_Registration_Page(self.driver)

        self.login.click_create_account_button()

        self.reg.registration()
