from CommonImportsPkg.common_imports import *

class AddReturnReasonsTest(unittest.TestCase):
    def __init__(self, methodName='test_addReturn_Reasons', data=None):
        super(AddReturnReasonsTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addReturn_Reasons(self):
        if self.data:
            self.driver.maximize_window()

            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_addReturn_Reasons']['username']
            password = self.data['test_addReturn_Reasons']['password']
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
            flash("You have passed Add Return Reasons Test Case.", "success")
        else:
            flash("You have not passed Add Return Reasons Test Case.", "error")
