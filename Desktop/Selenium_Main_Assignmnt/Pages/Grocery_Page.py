from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page


dict_d = {}


class Grocery_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)

    GROCERY = (By.XPATH, "//*[text()='Grocery']")
    SERACH_GROCERY_TEXT = (By.XPATH, "//input[@title='Search grocery products']")
    SEARCH_GROCERY_BUTTON = (
        By.XPATH, "//input[@title='Search grocery products']/parent::div//following-sibling::button")
    Add_Product_Milk = (By.XPATH, "//*[text()='Add Item']")
    Go_To_Cart = (By.XPATH, "//*[text()='Cart']")
    Add_Toor_Daal = (By.XPATH, "//*[text()='Toor Dal']")
    Staples = (By.XPATH, "//*[text()='Staples']")
    Add_gujrati_daal = (By.XPATH,"//*[text()='Origo Fresh Gujarat Toor Dal (Split)']")
    Dairy = (By.XPATH, "//*[text()='Dairy & Eggs']")
    Cheese = (By.XPATH, "//*[text()='Cheese']")
    Add_amul_cheese =(By.XPATH, "//*[text()='Amul Processed cheese Cubes']")
    Add_to_basket = (By.XPATH, "//*[text()='ADD TO BASKET']")
    Snacks = (By.XPATH,"//*[text()='Snacks & Beverages']")
    Cookies = (By.XPATH,"//*[text()='Cookies']")
    Unibic = (By.XPATH, "//*[text()='UNIBIC Assorted Cookies']")
    Go_to_basket =(By.XPATH, "//*[text()='GO TO BASKET']")
    TATA_FILTER = (By.XPATH, "//div[text()='Tata']//preceding-sibling::div")
    BESAN = (By.XPATH, "//a[text()='Tata BESAN 1 KG']")


    def get__data(self, test_case):
        global dict_d
        dict_d = Test_Data.getTestData(self, test_case)
        return dict_d
