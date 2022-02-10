from Config.config import Test_Data
from Pages.Login_Page import Login_Page
from Pages.Profile_Page import Profile_Page
from Scripts.test_Base import test_Base


class Test_Address(test_Base):

    def test_add_address_functionality(self):
        log = test_Base.getLogger()
        self.loginApplication = Login_Page(self.driver)
        self.loginApplication.base_login_to_application()
        self.profile = Profile_Page(self.driver)
        self.profile.navigate_to_address()
        self.profile.click_operation(self.profile.ADD_ADDRESS)
        log.info("Adding New Address")
        dataDictAddress = Test_Data.getTestData(self, "test_address")
        log.info("Adding Name")
        self.profile.send_keys_operation(self.profile.NAME, str(dataDictAddress["PersonName"]))
        log.info("Adding phone number")
        self.profile.send_keys_operation(self.profile.PHONE, str(dataDictAddress["Phone"]))
        log.info("Adding pincode")
        self.profile.send_keys_operation(self.profile.PINCODE, str(dataDictAddress["pincode"]))
        log.info("Adding locality")
        self.profile.send_keys_operation(self.profile.LOCALITY, str(dataDictAddress["locality"]))
        log.info("Adding area")
        self.profile.send_keys_operation(self.profile.ADDRESS, str(dataDictAddress["area"]))
        log.info("Selecting radio button")
        self.profile.click_operation(self.profile.HOME_CHECKBOX)
        log.info("Saving changes")
        self.profile.click_operation(self.profile.SAVE_BUTTON)
        log.info("Saved changes successfully!!")
        res = self.profile.element_exist_check(self.profile.Assertion_Element)
        assert res == True
        log.info("Testcase 5 is passed successfully!!!")


