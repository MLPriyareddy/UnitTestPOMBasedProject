from selenium import webdriver
import unittest
import HtmlTestRunner
import time
from PageObjects.SignUpPage import SignupPage
import sys
sys.path.append("C:/SeleniumProjects/UnitTestPOMBasedProject")


class SignupTest(unittest.TestCase):
    baseURL = "https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
    username = "Test12345"
    userid = "Tester12345@gmail.com"
    password = "Test@12345"
    reenter_password = "Test@12345"
    driver = webdriver.Chrome(executable_path="C:/SeleniumProjects/UnitTestPOMBasedProject/Drivers/chromedriver.exe")

    @classmethod
    def setUpClass(cls) -> None:
        print("Amazon SignUp Page Started....")
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_signup(self):
        sp = SignupPage(self.driver)
        sp.enter_username(self.username)
        sp.enter_userid(self.userid)
        sp.enter_password(self.password)
        sp.password_check(self.reenter_password)
        sp.create_account()
        time.sleep(6)

    @classmethod
    def tearDownClass(cls) -> None:
        print("Customer signup Completed")
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/SeleniumProjects/UnitTestPOMBasedProject/Reports"))







