from Pages.Grocery_Page import Grocery_Page
from Pages.Login_Page import Login_Page
from Scripts.test_Base import test_Base


class Test_Loginn(test_Base):

    def login_functionality(self):

        self.login = Login_Page(self.driver)
        self.login.base_login_to_application()

    def test_login_functionality(self):
        log = test_Base.getLogger()
        self.login = Login_Page(self.driver)
        self.login.base_login_to_application()
        self.grocery = Grocery_Page(self.driver)
        self.grocery.click_operation(self.grocery.GROCERY)
        text = self.grocery.is_text_present("Staples")
        assert text == True
        log.info("Test case 1 is passed")



