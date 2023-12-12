from CommonImportsPkg.common_imports import *
from login import Login


class AddEmailTemplatesTest(unittest.TestCase):
    def __init__(self, methodName='test_addEmail_Templates', data=None):
        super(AddEmailTemplatesTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_addEmail_Templates(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addEmail_Templates']['username']
            # password = self.data['test_addEmail_Templates']['password']
            # username_input = self.driver.find_element(By.ID, "username")
            # self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            # username_input.send_keys(username)
            # time.sleep(5)
            #
            # # Step 5: Enter password in the password input box
            # password_input = self.driver.find_element(By.ID, "password")
            # self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            # password_input.send_keys(password)
            # time.sleep(5)
            #
            # # Step 6: Click on the login button
            # # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
            # login_button = self.driver.find_element(By.ID, "login")
            # self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
            # login_button.click()
            # time.sleep(10)
            # Step 6: Select Store Admin
            store_admin = self.driver.find_element(By.XPATH, "//h4[text()='Store Admin']")
            # Check if the element is displayed
            self.assertTrue(store_admin.is_displayed(), msg="Store Admin is not displayed")
            store_admin.click()
            time.sleep(10)

            menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
            self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
            menu_settings.click()
            time.sleep(5)

            sidebar_menu_email_templates = self.driver.find_element(By.XPATH, "//span[text()='Email Templates']")
            self.assertTrue(sidebar_menu_email_templates.is_displayed(),
                            msg="Email Templates menu is not displayed.")
            sidebar_menu_email_templates.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='New']")
            self.assertTrue(add_new_button.is_displayed(), msg="New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data["test_addEmail_Templates"]["Business_Unit"]
            input_business_unit = self.driver.find_element(By.ID, "headerTab_14B7879D3815481293B738A105C016BC")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            name = self.data["test_addEmail_Templates"]["Name"]
            input_name = self.driver.find_element(By.ID, "headerTab_26146484C46744C5BAFA43181D36EEAA")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            subject = self.data["test_addEmail_Templates"]["Subject"]
            input_subject = self.driver.find_element(By.ID, "headerTab_E768126E2C70413D86C1806B1AB207DA")
            self.assertTrue(input_subject.is_displayed(), msg="Subject input is not displayed.")
            input_subject.send_keys(subject)
            time.sleep(5)

            from_email = self.data["test_addEmail_Templates"]["From_Email"]
            input_from_email = self.driver.find_element(By.ID, "headerTab_F507A749DFE94E46A2F24BC7BA63ABB6")
            self.assertTrue(input_from_email.is_displayed(), msg="From Email input is not displayed.")
            input_from_email.send_keys(from_email)
            time.sleep(5)

            reply_to = self.data["test_addEmail_Templates"]["Reply_To"]
            input_reply_to = self.driver.find_element(By.ID, "headerTab_D4E52CF55E684D699F9D826F343DD6EA")
            self.assertTrue(input_reply_to.is_displayed(), msg="Reply to input is not displayed.")
            input_reply_to.send_keys(reply_to)
            time.sleep(5)

            to_email = self.data["test_addEmail_Templates"]["To_Email"]
            input_to_email = self.driver.find_element(By.ID, "headerTab_2B6CB7B0340447338A94D40EC3348491")
            self.assertTrue(input_to_email.is_displayed(), msg="To Email input is not displayed.")
            input_to_email.send_keys(to_email)
            time.sleep(5)

            cc_email = self.data["test_addEmail_Templates"]["CC_Email"]
            input_cc_email = self.driver.find_element(By.ID, "headerTab_8E8FE1C2F5804E12A11B527481A6A8A4")
            self.assertTrue(input_cc_email.is_displayed(), msg="CC Email input is not displayed.")
            input_cc_email.send_keys(cc_email)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
