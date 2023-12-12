from CommonImportsPkg.common_imports import *

class AddReturnReasonsTest(unittest.TestCase):
    def __init__(self, methodName='test_addReturn_Reasons', data=None):
        super(AddReturnReasonsTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_addReturn_Reasons(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addReturn_Reasons']['username']
            # password = self.data['test_addReturn_Reasons']['password']
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
            time.sleep(5)

            sidebar_menu_return_reason = self.driver.find_element(By.XPATH, "//span[text()='Return Reason']")
            self.assertTrue(sidebar_menu_return_reason.is_displayed(),
                            msg="Return Reason menu is not displayed.")
            sidebar_menu_return_reason.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='New']")
            self.assertTrue(add_new_button.is_displayed(), msg="New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            search_key = self.data["test_addReturn_Reasons"]["Search_Key"]
            input_search_key = self.driver.find_element(By.ID, "headerTab_B7E5EDABEBC744D4A0D3A833976D9AB5")
            self.assertTrue(input_search_key.is_displayed(), msg="Search Key input is not displayed.")
            input_search_key.send_keys(search_key)
            time.sleep(5)

            name = self.data["test_addReturn_Reasons"]["Name"]
            input_name = self.driver.find_element(By.ID, "headerTab_DF1455B50DAF4766BDCE2E3D2A200DC5")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            active_check = self.driver.find_element(By.ID, "headerTab_AA3A8B7C64394167AA35A4B971AD6890")
            self.assertTrue(active_check.is_displayed(), msg="Active Check box is not displayed.")
            if not active_check.is_selected():
                active_check.click()
            else:
                pass

            description = self.data["test_addReturn_Reasons"]["Description"]
            input_description = self.driver.find_element(By.ID, "headerTab_A56B505BC1BE4FD2B7464AE36B055143")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            customer_return_check = self.driver.find_element(By.ID, "headerTab_F13A676C6B524EA98E4F311E7CA96515")
            self.assertTrue(customer_return_check.is_displayed(), msg="Customer Return Check box is not displayed.")
            if not customer_return_check.is_selected():
                customer_return_check.click()
            else:
                pass

            supplier_return_check = self.driver.find_element(By.ID, "headerTab_58BEB24E5F1E410EBB09C11A7A351826")
            self.assertTrue(supplier_return_check.is_displayed(), msg="Supplier Return Check box is not displayed.")
            if not supplier_return_check.is_selected():
                supplier_return_check.click()
            else:
                pass

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_search_key and input_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
