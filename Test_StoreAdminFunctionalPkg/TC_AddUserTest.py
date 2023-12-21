from CommonImportsPkg.common_imports import *
from login import Login


class AddUserTest(unittest.TestCase):
    def __init__(self, methodName='test_add_user', data=None):
        super(AddUserTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_add_user(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addUser']['username']
            # password = self.data['test_addUser']['password']
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
            time.sleep(10)

            sidebar_menu_user = self.driver.find_element(By.XPATH, "//span[text()='User']")
            self.assertTrue(sidebar_menu_user.is_displayed(), msg="User menu is not displayed.")
            sidebar_menu_user.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='New']")
            self.assertTrue(add_new_button.is_displayed(), msg="New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data["test_add_user"]["Business_Unit"]
            input_business_unit = self.driver.find_element(By.ID, "control-hooks_bunitname")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            first_name = self.data["test_add_user"]["FirstName"]
            input_first_name = self.driver.find_element(By.ID, "control-hooks_firstname")
            self.assertTrue(input_first_name.is_displayed(), msg="First Name input is not displayed.")
            input_first_name.send_keys(first_name)
            time.sleep(5)

            last_name = self.data["test_add_user"]["LastName"]
            input_last_name = self.driver.find_element(By.ID, "control-hooks_lastname")
            self.assertTrue(input_last_name.is_displayed(), msg="Last Name input is not displayed.")
            input_last_name.send_keys(last_name)
            time.sleep(5)

            user_name = self.data["test_add_user"]["UserName"]
            input_user_name = self.driver.find_element(By.ID, "control-hooks_username")
            self.assertTrue(input_user_name.is_displayed(), msg="User Name input is not displayed.")
            input_user_name.send_keys(user_name)
            time.sleep(5)

            home_dashboard = self.data["test_add_user"]["Home_Dashboard"]
            input_home_dashboard = self.driver.find_element(By.ID, "control-hooks_home_dashboard_id")
            self.assertTrue(input_home_dashboard.is_displayed(), msg="Home Dashboard input is not displayed.")
            input_home_dashboard.send_keys(home_dashboard)
            time.sleep(5)

            home_window = self.data["test_add_user"]["Home_Window"]
            input_home_window = self.driver.find_element(By.ID, "control-hooks_home_window_id")
            self.assertTrue(input_home_window.is_displayed(), msg="Home Window input is not displayed.")
            input_home_window.send_keys(home_window)
            time.sleep(5)

            home_report = self.data["test_add_user"]["Home_Report"]
            input_home_report = self.driver.find_element(By.ID, "control-hooks_home_report_id")
            self.assertTrue(input_home_report.is_displayed(), msg="Home Window input is not displayed.")
            input_home_report.send_keys(home_report)
            time.sleep(5)

            admin_check = self.driver.find_element(By.ID, "control-hooks_isactive")
            self.assertTrue(admin_check.is_displayed(), msg="Admin Check box is not displayed.")
            if not admin_check.is_selected():
                admin_check.click()
            else:
                pass

            # auto_generate_password_check = self.driver.find_element(By.ID, "")
            # self.assertTrue(auto_generate_password_check.is_displayed(), msg="Admin Check box is not displayed.")
            # if not auto_generate_password_check.is_selected():
            #     auto_generate_password_check.click()
            # else:
            #     pass

            email = self.data["test_add_user"]["Email"]
            input_email = self.driver.find_element(By.ID, "control-hooks_email")
            self.assertTrue(input_email.is_displayed(), msg="Email input is not displayed.")
            input_email.send_keys(email)
            time.sleep(5)

            description = self.data["test_add_user"]["Description"]
            input_description = self.driver.find_element(By.ID, "control-hooks_description")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit and input_first_name and input_last_name and input_user_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
