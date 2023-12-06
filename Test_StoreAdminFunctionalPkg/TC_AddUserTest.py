from CommonImportsPkg.common_imports import *

class AddTillTest(unittest.TestCase):
    def __init__(self, methodName='test_addUser', data=None):
        super(AddTillTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addUser(self):
        if self.data:
            self.driver.maximize_window()
            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_addUser']['username']
            password = self.data['test_addUser']['password']
            # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
            username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
            self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            username_input.send_keys(username)
            time.sleep(5)

            # Step 5: Enter password in the password input box
            password_input = self.driver.find_element(By.XPATH,
                                                      "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
            self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            password_input.send_keys(password)
            time.sleep(5)

            # Step 6: Click on the login button
            login_button = self.driver.find_element(By.XPATH,
                                                    "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
            self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
            login_button.click()
            time.sleep(10)
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

            sidebar_menu_user = self.driver.find_element(By.XPATH, "//span[text()='User']")
            self.assertTrue(sidebar_menu_user.is_displayed(),
                            msg="User menu is not displayed.")
            sidebar_menu_user.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='New']")
            self.assertTrue(add_new_button.is_displayed(), msg="New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data["test_addUser"]["Business_Unit"]
            input_business_unit = self.driver.find_element(By.ID, "control-hooks_bunitname")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            first_name = self.data["test_addUser"]["FirstName"]
            input_first_name = self.driver.find_element(By.ID, "control-hooks_firstname")
            self.assertTrue(input_first_name.is_displayed(), msg="First Name input is not displayed.")
            input_first_name.send_keys(first_name)
            time.sleep(5)

            last_name = self.data["test_addUser"]["LastName"]
            input_last_name = self.driver.find_element(By.ID, "control-hooks_lastname")
            self.assertTrue(input_last_name.is_displayed(), msg="Last Name input is not displayed.")
            input_last_name.send_keys(last_name)
            time.sleep(5)

            user_name = self.data["test_addUser"]["UserName"]
            input_user_name = self.driver.find_element(By.ID, "control-hooks_username")
            self.assertTrue(input_user_name.is_displayed(), msg="User Name input is not displayed.")
            input_user_name.send_keys(user_name)
            time.sleep(5)

            home_dashboard = self.data["test_addUser"]["Home_Dashboard"]
            input_home_dashboard = self.driver.find_element(By.ID, "control-hooks_home_dashboard_id")
            self.assertTrue(input_home_dashboard.is_displayed(), msg="Home Dashboard input is not displayed.")
            input_home_dashboard.send_keys(home_dashboard)
            time.sleep(5)

            home_window = self.data["test_addUser"]["Home_Window"]
            input_home_window = self.driver.find_element(By.ID, "control-hooks_home_window_id")
            self.assertTrue(input_home_window.is_displayed(), msg="Home Window input is not displayed.")
            input_home_window.send_keys(home_window)
            time.sleep(5)

            home_report = self.data["test_addUser"]["Home_Report"]
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

            email = self.data["test_addUser"]["Email"]
            input_email = self.driver.find_element(By.ID, "control-hooks_email")
            self.assertTrue(input_email.is_displayed(), msg="Email input is not displayed.")
            input_email.send_keys(email)
            time.sleep(5)

            description = self.data["test_addUser"]["Description"]
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
            flash("You have passed Test case.", "success")
        else:
            flash("You have not passed Test case.", "error")