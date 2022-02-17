from Pages.User_CompletedQuiz_Page import User_CompletedQuiz_Page
from Pages.User_DashBoard_Page import User_DashBoard_Page
from Pages.User_Login_Page1 import User_Test_LoginPage1
from Pages.User_PendingQuiz_Page import User_PendingQuiz_Page
from Pages.User_Quiz_Page import User_Quiz_Page
from Utilities.test_Base import test_Base


class Test_FilterByCategoryPendingQuiz_User(test_Base):
    def test_filter_by_category(self):
        #Object creation of necessary pages
        log = test_Base.getLogger()
        log.info("Complete quiz method started")

        self.login = User_Test_LoginPage1(self.driver)
        self.dashboard = User_DashBoard_Page(self.driver)
        self.pendingQuiz = User_PendingQuiz_Page(self.driver)

        #To login the account
        self.login.login1()

        #Filtering by the category
        self.dashboard.click_pending_quiz_button()
        self.pendingQuiz.filter_by_category()
