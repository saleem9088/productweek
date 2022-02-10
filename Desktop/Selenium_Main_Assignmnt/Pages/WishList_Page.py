from selenium.webdriver.common.by import By
from Pages.Base_Page import Base_Page
from Scripts.test_Base import test_Base


class WishList_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)

    user_test = (By.XPATH, "//*[text()='Test']")
    mywishlist = (By.XPATH, "//*[text()='Wishlist']")

    def go_to_wishlist(self):
        log = test_Base.getLogger()
        log.info("Navigating to Wishlist")
        self.Hover_operation(self.user_test)
        self.click_operation(self.mywishlist)




