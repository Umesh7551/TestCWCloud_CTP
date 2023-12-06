from CommonImportsPkg.common_imports import *

class AddRFIDTagTest(unittest.TestCase):
    def __init__(self, methodName='test_addRFIDTag', data=None):
        super(AddRFIDTagTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addRFIDTag(self):
        if self.data:
            self.driver.maximize_window()
            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_addRFIDTag']['username']
            password = self.data['test_addRFIDTag']['password']
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

            menu_products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
            self.assertTrue(menu_products.is_displayed(), msg="Products Menu is not Displayed")
            menu_products.click()
            time.sleep(5)

            sidebar_menu_rfid_tag = self.driver.find_element(By.XPATH,
                                                             "//span[text()='RFID Tag']")
            self.assertTrue(sidebar_menu_rfid_tag.is_displayed(),
                            msg="RFID Tag menu is not displayed.")
            sidebar_menu_rfid_tag.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            product_code = self.data["test_addRFIDTag"]["Product Code"]
            input_product_code = self.driver.find_element(By.ID, "headerTab_6BEBA63D3D014D9CBF0C74F7E5D0FDC9")
            self.assertTrue(input_product_code.is_displayed(), msg="Product Code input is not displayed.")
            input_product_code.send_keys(product_code)
            time.sleep(5)

            product = self.data["test_addRFIDTag"]["Product"]
            input_product = self.driver.find_element(By.ID, "headerTab_B456D14F3DC54EFE8378FFE88597149A")
            self.assertTrue(input_product.is_displayed(), msg="Product Input is not displayed.")
            input_product.send_keys(product)
            time.sleep(5)

            tag_value = self.data["test_addRFIDTag"]["Tag Value"]
            input_tag_value = self.driver.find_element(By.ID, "headerTab_C048011FA52F409DB461EAE659DD004F")
            self.assertTrue(input_tag_value.is_displayed(), msg="Tag Value Input is not displayed.")
            input_tag_value.send_keys(tag_value)
            time.sleep(5)

            tag_type = self.data["test_addRFIDTag"]["Tag Type"]
            input_tag_type = self.driver.find_element(By.ID, "headerTab_9E89133760594284B76F9A044408EC10")
            self.assertTrue(input_tag_type.is_displayed(), msg="Tag Type input is not displayed.")
            input_tag_type.send_keys(tag_type)
            time.sleep(5)

            tagging_date = self.data["test_addRFIDTag"]["Tagging Date"]
            input_tagging_date = self.driver.find_element(By.ID, "headerTab_B70961444E0A45938756807DDCE4E883")
            self.assertTrue(input_tagging_date.is_displayed(), msg="Tagging Date input is not displayed.")
            input_tagging_date.send_keys(tagging_date)
            time.sleep(5)

            batch_number = self.data["test_addRFIDTag"]["Batch Number"]
            input_batch_number = self.driver.find_element(By.ID, "headerTab_3676DE90C3D542D0A0E69F906666B0FC")
            self.assertTrue(input_batch_number.is_displayed(), msg="Batch Number input box is not displayed.")
            input_batch_number.send_keys(batch_number)
            time.sleep(5)

            batch = self.data["test_addRFIDTag"]["Batch"]
            input_batch = self.driver.find_element(By.ID, "headerTab_34531C4CC21A41CCB107FDCCE8A4020E")
            self.assertTrue(input_batch.is_displayed(), msg="Batch input is not displayed.")
            input_batch.send_keys(batch)
            time.sleep(5)

            location = self.data["test_addRFIDTag"]["Location"]
            input_location = self.driver.find_element(By.ID, "headerTab_79D49C5DBFB34C898BC5479E73A09BFF")
            self.assertTrue(input_location.is_displayed(), msg="Location input is not displayed.")
            input_location.send_keys(location)
            time.sleep(5)

            tag_status = self.data["test_addRFIDTag"]["Tag Status"]
            input_tag_status = self.driver.find_element(By.ID, "headerTab_A4335C2B76D94CE5BEAAC5814AF3401F")
            self.assertTrue(input_tag_status.is_displayed(), msg="Tag Status input is not displayed.")
            input_tag_status.send_keys(tag_status)
            time.sleep(5)

            last_scanned_date = self.data["test_addRFIDTag"]["Last Scanned Date"]
            input_last_scanned_date = self.driver.find_element(By.ID, "headerTab_8D866234F3374BC3A8CF3CBF360C3239")
            self.assertTrue(input_last_scanned_date.is_displayed(), msg="Last Scanned Date input is not displayed.")
            input_last_scanned_date.send_keys(last_scanned_date)
            time.sleep(5)

            scanned_by = self.data["test_addRFIDTag"]["Scanned By"]
            input_scanned_by = self.driver.find_element(By.ID, "headerTab_7273A3F525634450B1703500ED870758")
            self.assertTrue(input_scanned_by.is_displayed(), msg="Scanned By input is not displayed.")
            input_scanned_by.send_keys(scanned_by)
            time.sleep(5)

            expiry_date = self.data["test_addRFIDTag"]["Expiry Date"]
            input_expiry_date = self.driver.find_element(By.ID, "headerTab_1288173DC4FC43FFA40D5638DB6DAA67")
            self.assertTrue(input_expiry_date.is_displayed(), msg="Expiry Date input is not displayed.")
            input_expiry_date.send_keys(expiry_date)
            time.sleep(5)

            custom_attributes = self.data["test_addRFIDTag"]["Custom Attributes"]
            input_custom_attributes = self.driver.find_element(By.ID, "headerTab_1BFCB53588FF4DFD86E112490D6335B0")
            self.assertTrue(input_custom_attributes.is_displayed(), msg="Custom Attributes input is not displayed.")
            input_custom_attributes.send_keys(custom_attributes)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_product_code and input_tag_value is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash("You have passed Add RFID Tag Test case.", "success")
        else:
            flash("You have not passed Add RFID Tag Test case.", "error")