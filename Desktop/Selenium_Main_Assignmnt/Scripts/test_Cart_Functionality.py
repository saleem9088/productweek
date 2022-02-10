from Config.config import Test_Data
from Pages.Grocery_Page import Grocery_Page
from Pages.Login_Page import Login_Page
from Scripts.test_Base import test_Base


class Test_Cart(test_Base):

    def test_cart_functionality(self):
        log = test_Base.getLogger()
        self.loginGrocery = Login_Page(self.driver)
        self.loginGrocery.base_login_to_application()
        self.home = Grocery_Page(self.driver)
        self.home.click_operation(self.home.GROCERY)
        log.info("Navigating to Grocery Section")
        self.home.implicit_waiting()
        data = self.home.get__data("test_Cart_Functionality")
        self.home.Hover_operation(self.home.Staples)
        self.home.click_operation(self.home.Add_Toor_Daal)
        self.home.click_operation(self.home.Add_gujrati_daal)
        dataDictGrocery = Test_Data.getTestData(self, "test_Cart")
        log.info("Adding product 1")
        a = int(1)
        self.home.Switch_to_child_window(a)
        self.home.click_operation(self.home.Add_to_basket)
        self.home.Hover_operation(self.home.Dairy)
        self.home.click_operation(self.home.Cheese)
        self.home.click_operation(self.home.Add_amul_cheese)
        log.info("Adding First Product")
        b = int(2)
        self.home.Switch_to_child_window(b)
        self.home.click_operation(self.home.Add_to_basket)
        self.home.Hover_operation(self.home.Snacks)
        self.home.click_operation(self.home.Cookies)
        self.home.click_operation(self.home.Unibic)
        log.info("Adding Second Product")
        c = int(3)
        self.home.Switch_to_child_window(c)
        self.home.click_operation(self.home.Add_to_basket)
        self.home.click_operation(self.home.Go_to_basket)
        flag = self.home.is_text_present(str(dataDictGrocery["Cookies"]))
        log.info(flag)
        assert True == flag
        flag = self.home.is_text_present(str(dataDictGrocery["Dairy"]))
        print(type(dataDictGrocery["Dairy"]))
        log.info(flag)
        assert True == flag
        flag = self.home.is_text_present(str(dataDictGrocery["Staples"]))
        log.info(flag)
        assert True == flag
        log.info("All 3 items are successfully added into basket")
        self.home.Switch_to_child_window(a)
        self.home.click_operation(self.home.Go_To_Cart)
        flag = self.home.is_text_present(str(dataDictGrocery["quantity_in_cart"]))
        assert True == flag
        log.info("All 3 items are successfully added into Cart")
        log.info("Test Case 2 is passed")
