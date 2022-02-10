from Config.config import Test_Data
from Pages.Fashion_Page import Fashion_Page
from Pages.Login_Page import Login_Page
from Pages.WishList_Page import WishList_Page
from Scripts.test_Base import test_Base


class Test_Wishlist(test_Base):

    def test_wishlist_functionality(self):
        log = test_Base.getLogger()
        self.loginwishlist = Login_Page(self.driver)
        self.loginwishlist.base_login_to_application()
        dataDictWishlist = Test_Data.getTestData(self, "test_wishlist")
        self.fashion = Fashion_Page(self.driver)
        log.info("Navigating to Fashion Section")
        self.fashion.Hover_operation(self.fashion.Fashion)
        self.fashion.Hover_operation(self.fashion.Kids)
        log.info("Inside the Kids Section")
        self.fashion.click_operation(self.fashion.Girls_Dresses)
        self.fashion.click_operation(self.fashion.dress1)
        self.fashion.Hover_operation(self.fashion.Women_Ethnic)
        self.fashion.click_operation(self.fashion.Women_Sarees)
        log.info("Inside the Saree Section")
        self.fashion.click_operation(self.fashion.saree1)
        self.wish = WishList_Page(self.driver)
        self.wish.go_to_wishlist()
        dress_kid = self.wish.is_text_present(str(dataDictWishlist["kidsdress"]))
        assert dress_kid == True
        log.info("Kids dress is added into wishlist successfully")
        dress_saree = self.wish.is_text_present(str(dataDictWishlist["womensaree"]))
        assert dress_saree == True
        log.info("Saree is added into wishlist successfully")
        log.info("Test Case 4 is passed successfully")

