from Config.config import Test_Data
from Pages.Grocery_Page import Grocery_Page
from Pages.HomePage import Home_Page
from Pages.Login_Page import Login_Page
from Scripts.test_Base import test_Base


class Test_Search(test_Base):

    def test_search_add_filter(self):
        log = test_Base.getLogger()
        self.login_3 = Login_Page(self.driver)
        self.login_3.base_login_to_application()
        data_dict_4 = Test_Data.getTestData(self, "test_filter")
        self.home_page = Home_Page(self.driver)
        self.home_page.send_keys_operation(self.home_page.SEARCH, str(data_dict_4["search_product"]))
        self.home_page.click_operation(self.home_page.SEARCH_ENTER)
        self.grocerys = Grocery_Page(self.driver)
        self.grocerys.click_operation(self.grocerys.TATA_FILTER)
        bool = self.home_page.is_text_present(str(data_dict_4["filter_product"]))
        assert True == bool
        log.info("Testcase 3 is passed successfully")
