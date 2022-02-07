from selenium.webdriver.common.by import By

from Page_Object.Pages.BasePage import Base_page

i = '0'

tem = 'h'


class Home(Base_page):

    def set_tem(self, a):
        global tem
        tem = a

    Current_Temperature = (By.ID, "temperature")
    Get_Info = (By.XPATH, "//*[text()='Current temperature']//following-sibling::span")
    Get_info_text = (By.XPATH, "//*[text()='Current temperature']//following-sibling::span")
    Get_Moisturizers = (By.XPATH, "//button[text()='Buy moisturizers']")
    Get_Sunscreen = (By.XPATH, "//button[text()='Buy sunscreens']")
    Fetch_Product = (By.XPATH, "(//*[@class='container']//child::div//p)")
    Add_product = (By.XPATH, "//p[contains(text(),'" + tem + "')]//following-sibling::button")
    Go_To_Cart = (By.XPATH, "//button[@onclick='goToCart()']")
    Pay_with_Card=(By.XPATH, "//span[text()='Pay with Card']")
    Email = (By.XPATH,"// input[ @ placeholder = 'Email']")
    Card_Number = (By.XPATH,"// input[ @ placeholder = 'Card number']")
    MonthYear = (By.XPATH,"// input[ @ placeholder = 'MM / YY']")
    CV = (By.XPATH,"// input[ @ placeholder = 'CVC']")
    ZIP = (By.XPATH,"// input[ @ placeholder = 'ZIP Code']")
    Pay_IN_INR =(By.XPATH," // span[starts - with(text(), 'Pay INR')]")
    Success_Msg = (By.XPATH,"// p[ @class ='text-justify']")
