from Pages.Login_Page import Login_Page
from Pages.Logout_Page import Logout_Page
from Scripts.test_Base import test_Base


class Test_Logout(test_Base):

    def test_add_logout_functionality(self):
        log = test_Base.getLogger()
        self.loginApplic = Login_Page(self.driver)
        self.loginApplic.base_login_to_application()
        self.logout = Logout_Page(self.driver)
        self.logout.logout_operation()
        log.info("Testcase 6 is successfully passed")
