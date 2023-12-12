from CommonImportsPkg.common_imports import *

class AddTillTest(unittest.TestCase):
    def __init__(self, methodName='test_addTill', data=None):
        super(AddTillTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addTill(self):
        if self.data:
            self.driver.maximize_window()

            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_addTill']['username']
            password = self.data['test_addTill']['password']
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

            sidebar_menu_till = self.driver.find_element(By.XPATH, "//span[text()='Till']")
            self.assertTrue(sidebar_menu_till.is_displayed(), msg="Till menu is not displayed.")
            sidebar_menu_till.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            store = self.data['test_addTill']['Store']
            input_store = self.driver.find_element(By.ID, "headerTab_7FE7DEA08CD846AF9AFFEFB152C4B234")
            self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
            input_store.send_keys(store)
            time.sleep(5)

            pos_type = self.data['test_addTill']['POS_Type']
            input_pos_type = self.driver.find_element(By.ID, "headerTab_521F1546BCF24539B800B3FE6417F92C")
            self.assertTrue(input_pos_type.is_displayed(), msg="Pos Type input is not displayed.")
            input_pos_type.send_keys(pos_type)
            time.sleep(5)

            till_id = self.data['test_addTill']['Till_ID']
            input_till_id = self.driver.find_element(By.ID, "headerTab_8FF51B00ABCE45D59FD2BC18671550AA")
            self.assertTrue(input_till_id.is_displayed(), msg="Till ID input is not displayed.")
            input_till_id.send_keys(till_id)
            time.sleep(5)

            name = self.data['test_addTill']['Name']
            input_name = self.driver.find_element(By.ID, "headerTab_2BFAD20AC82E42CBB295A7E72386A7CA")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            description = self.data['test_addTill']['Description']
            input_description = self.driver.find_element(By.ID, "headerTab_5DBB7666597A4AB4B45BF239EF239F68")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            next_order_number = self.data['test_addTill']['Next_Order_Number']
            input_next_order_number = self.driver.find_element(By.ID, "headerTab_CFCE0A38E8ED4511AC74D68BD77F2D17")
            self.assertTrue(input_next_order_number.is_displayed(), msg="Description input is not displayed.")
            input_next_order_number.send_keys(next_order_number)
            time.sleep(5)

            prefix = self.data['test_addTill']['Prefix']
            input_prefix = self.driver.find_element(By.ID, "headerTab_2350596E8BC94DB484B121448DA8EFD3")
            self.assertTrue(input_prefix.is_displayed(), msg="Prefix input is not displayed.")
            input_prefix.send_keys(prefix)
            time.sleep(5)

            suffix = self.data['test_addTill']['Suffix']
            input_suffix = self.driver.find_element(By.ID, "headerTab_28A68B46C8694CD08F5DBA2EDFEF9D95")
            self.assertTrue(input_suffix.is_displayed(), msg="Suffix input is not displayed.")
            input_suffix.send_keys(suffix)
            time.sleep(5)

            access_controller = self.data['test_addTill']['Access_Controller']
            input_access_controller = self.driver.find_element(By.ID, "headerTab_67EBFF9CE4AB48B4BE20409D2B6D8FB9")
            self.assertTrue(input_access_controller.is_displayed(), msg="Access Controller input is not displayed.")
            input_access_controller.send_keys(access_controller)
            time.sleep(5)

            enable_paynow_check = self.driver.find_element(By.ID, "headerTab_759A7EECAB264992B74BFCF455D641A5")
            if not enable_paynow_check.is_selected():
                enable_paynow_check.click()

            kot_print_template = self.data['test_addTill']['KOT_Print_Template']
            input_kot_print_template = self.driver.find_element(By.ID, "headerTab_F4D0FD94C81242E88028BFCCA06EDE13")
            self.assertTrue(input_kot_print_template.is_displayed(),
                            msg="KOT Print Template input is not displayed.")
            input_kot_print_template.send_keys(kot_print_template)
            time.sleep(5)

            status = self.data['test_addTill']['Status']
            input_status = self.driver.find_element(By.ID, "headerTab_18F1AD63A40E4ABFB3832F568C5EC2C8")
            self.assertTrue(input_status.is_displayed(),
                            msg="Status input is not displayed.")
            input_status.send_keys(status)
            time.sleep(5)

            logged_in_cashier = self.data['test_addTill']['Logged_in_Cashier']
            input_logged_in_cashier = self.driver.find_element(By.ID, "headerTab_011BF7B786424F3A948092D3D0A9CE24")
            self.assertTrue(input_logged_in_cashier.is_displayed(),
                            msg="Logged In Cashier input is not displayed.")
            input_logged_in_cashier.send_keys(logged_in_cashier)
            time.sleep(5)

            enable_rfid_check = self.driver.find_element(By.ID, "headerTab_D60187E388584AFA8752E23D469C88A2")
            self.assertTrue(enable_rfid_check.is_displayed(), msg="Enable RFID Check box is not displayed.")
            if not enable_rfid_check.is_selected():
                enable_rfid_check.click()

            cancel_kot_print_template = self.data['test_addTill']['Cancel_KOT_Print_Template']
            input_cancel_kot_print_template = self.driver.find_element(By.ID,
                                                                       "headerTab_8303A2F379984D79A1F924985939DA8C")
            self.assertTrue(input_cancel_kot_print_template.is_displayed(),
                            msg="Cancel KOT Print Template input is not displayed.")
            input_cancel_kot_print_template.send_keys(cancel_kot_print_template)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_store is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")