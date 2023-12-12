from CommonImportsPkg.common_imports import *

class AddStorageLocationTest(unittest.TestCase):
    def __init__(self, methodName='test_addStorage_location', data=None):
        super(AddStorageLocationTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addStorage_location(self):
        if self.data:
            self.driver.maximize_window()

            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_addStorage_location']['username']
            password = self.data['test_addStorage_location']['password']
            username_input = self.driver.find_element(By.ID, "username")
            self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            username_input.send_keys(username)
            time.sleep(5)

            # Step 5: Enter password in the password input box
            password_input = self.driver.find_element(By.ID, "password")
            self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            password_input.send_keys(password)
            time.sleep(5)

            # Step 6: Click on the login button
            login_button = self.driver.find_element(By.ID, "login")
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

            sidebar_menu_storage_location = self.driver.find_element(By.XPATH, "//span[text()='Storage Location']")
            self.assertTrue(sidebar_menu_storage_location.is_displayed(),
                            msg="Storage Location menu is not displayed.")
            sidebar_menu_storage_location.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data['test_addStorage_location']['Business_Unit']
            input_business_unit = self.driver.find_element(By.ID, "headerTab_409B6D159F984629BB664FDEC90B1936")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            value = self.data['test_addStorage_location']['Value']
            input_value = self.driver.find_element(By.ID, "headerTab_5ADE8D2E8C0149C5BFFCC270BB238548")
            self.assertTrue(input_value.is_displayed(), msg="Value input is not displayed.")
            input_value.send_keys(value)
            time.sleep(5)

            name = self.data['test_addStorage_location']['Name']
            input_name = self.driver.find_element(By.ID, "headerTab_8FF51B00ABCE45D59FD2BC18671550AA")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            storage_capacity = self.data['test_addStorage_location']['Storage_Capacity']
            input_storage_capacity = self.driver.find_element(By.ID, "headerTab_04A9A8C3F1494BDF874D5028EFE75295")
            self.assertTrue(input_storage_capacity.is_displayed(), msg="Storage Capacity input is not displayed.")
            input_storage_capacity.send_keys(storage_capacity)
            time.sleep(5)

            active_check = self.driver.find_element(By.ID, "headerTab_44F0C43B0466459A879D384057BEE1F9")
            self.assertTrue(active_check.is_displayed(), msg="Active Check box is not displayed.")
            if not active_check.is_selected():
                active_check.click()

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit and input_value and input_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
