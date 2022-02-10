from selenium.webdriver.common.by import By
from Pages.Base_Page import Base_Page


class Fashion_Page(Base_Page):

    def __init__(self, driver):
        super().__init__(driver)

    Fashion = (By.XPATH, "//*[text()='Fashion']")
    Kids =(By.XPATH, "//*[text()='Kids']")
    Girls_Dresses = (By.XPATH, "//*[text()='Girls Dresses']")
    dress1 =(By.XPATH,"(//*[text()='Girls Midi/Knee Length Casual Dress']/parent::div//preceding-sibling::a)[1]//div[@class='_2hVSre _1DmLJ5 -o7Q4n']")
    Women_Ethnic = (By.XPATH, "//*[text()='Women']")
    Women_Sarees = (By.XPATH, "//*[text()='Sarees']")
    saree1 = (By.XPATH,"(//*[text()='Ek-Pal']/parent::div//preceding-sibling::a)[1]//div[@class='_2hVSre _1DmLJ5 -o7Q4n']")

