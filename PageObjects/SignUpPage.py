class SignupPage():
    textbox_username_Name = "customerName"
    textbox_userEmail_Name = "email"
    textbox_password_Name = "password"
    textbox_password_Check_Name = "passwordCheck"
    Button_create_account_ID = "continue"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_name(self.textbox_username_Name).send_keys(username)

    def enter_userid(self, userid):
        self.driver.find_element_by_name(self.textbox_userEmail_Name).send_keys(userid)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.textbox_password_Name).send_keys(password)

    def password_check(self, reenter_password):
        self.driver.find_element_by_name(self.textbox_password_Check_Name).send_keys(reenter_password)

    def create_account(self):
        self.driver.find_element_by_id(self.Button_create_account_ID).click()
