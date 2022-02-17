from Pages.User_Login_Page1 import User_Test_LoginPage1
from Utilities.test_Base import test_Base


class Test_Login1_User(test_Base):
    def test_Login(self):
        #Object creation of necessary pages
        self.login=User_Test_LoginPage1(self.driver)
        self.login.login1()



