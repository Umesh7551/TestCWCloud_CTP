from CommonImportsPkg.common_imports import *

class AddBusinessUnitTest(unittest.TestCase):
    def __init__(self, methodName='test_addBusiness_unit', data=None):
        super(AddBusinessUnitTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_addBusiness_unit(self):
        if self.data:
            self.driver.maximize_window()

            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_addBusiness_unit']['username']
            password = self.data['test_addBusiness_unit']['password']
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
            # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
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

            sidebar_menu_business_unit = self.driver.find_element(By.XPATH, "//span[text()='Business Unit']")
            self.assertTrue(sidebar_menu_business_unit.is_displayed(), msg="Business Unit menu is not displayed.")
            sidebar_menu_business_unit.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit_id = self.data["test_addBusiness_unit"]["Business_unit_id"]
            input_business_unit_id = self.driver.find_element(By.ID, "headerTab_01BE43C2E97742A6A4048A5AD7AE8995")
            self.assertTrue(input_business_unit_id.is_displayed(), msg="Business Unit ID input is not displayed.")
            input_business_unit_id.send_keys(business_unit_id)
            time.sleep(5)

            name = self.data["test_addBusiness_unit"]["Name"]
            input_name = self.driver.find_element(By.ID, "headerTab_4D6B14DB22364215ADF09FC23E3483F1")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            description = self.data["test_addBusiness_unit"]["Description"]
            input_description = self.driver.find_element(By.ID, "headerTab_BDC6B7BF5CB844A8803628E9E2D0F08E")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            type = self.data["test_addBusiness_unit"]["Type"]
            input_type = self.driver.find_element(By.ID, "headerTab_E28CA6746CD74D5187C6AE3127E83974")
            self.assertTrue(input_type.is_displayed(), msg="Type input is not displayed.")
            input_type.send_keys(type)
            time.sleep(5)

            parent_business_unit = self.data["test_addBusiness_unit"]["Parent_Business_Unit"]
            input_parent_business_unit = self.driver.find_element(By.ID,
                                                                  "headerTab_AD346BE71E244CCEA9F7CC549EEC3CDA")
            self.assertTrue(input_parent_business_unit.is_displayed(),
                            msg="Parent Business Unit input is not displayed.")
            input_parent_business_unit.send_keys(parent_business_unit)
            time.sleep(5)

            legal_entity = self.data["test_addBusiness_unit"]["Legal_Entity"]
            input_legal_entity = self.driver.find_element(By.ID, "headerTab_47D85D2F9BDA45FF9F5C081633BBE7AE")
            self.assertTrue(input_legal_entity.is_displayed(), msg="Legal Entity input is not displayed.")
            input_legal_entity.send_keys(legal_entity)
            time.sleep(5)

            gst_no = self.data["test_addBusiness_unit"]["GST_No"]
            input_gst_no = self.driver.find_element(By.ID, "headerTab_7D3FB0064E2F4804A855BB8F8D14D1E2")
            self.assertTrue(input_gst_no.is_displayed(), msg="GST No input is not displayed.")
            input_gst_no.send_keys(gst_no)
            time.sleep(5)

            currency = self.data["test_addBusiness_unit"]["Currency"]
            input_currency = self.driver.find_element(By.ID, "headerTab_94F9DE8CCC4D4460A1900A8C4A1ACF75")
            self.assertTrue(input_currency.is_displayed(), msg="Currency input is not displayed.")
            input_currency.send_keys(currency)
            time.sleep(5)

            external_bunit_ref = self.data["test_addBusiness_unit"]["External_Bunit_ref"]
            input_external_bunit_ref = self.driver.find_element(By.ID, "headerTab_6965D8D307D340BFA38C14E033EEAB8E")
            self.assertTrue(input_external_bunit_ref.is_displayed(), msg="Currency input is not displayed.")
            input_external_bunit_ref.send_keys(external_bunit_ref)
            time.sleep(5)

            latitude = self.data["test_addBusiness_unit"]["Latitude"]
            input_latitude = self.driver.find_element(By.ID, "headerTab_1726DBCFE8464A50A2E6C3CB1FC533AC")
            self.assertTrue(input_latitude.is_displayed(), msg="Latitude input is not displayed.")
            input_latitude.send_keys(latitude)
            time.sleep(5)

            longitude = self.data["test_addBusiness_unit"]["Longitude"]
            input_longitude = self.driver.find_element(By.ID, "headerTab_C1B99AD7C25A40A18B69B61AE44BC7C7")
            self.assertTrue(input_longitude.is_displayed(), msg="Longitude input is not displayed.")
            input_longitude.send_keys(longitude)
            time.sleep(5)

            image_url = self.data["test_addBusiness_unit"]["Image_url"]
            input_image_url = self.driver.find_element(By.ID, "headerTab_C0688902314444D8B670C912B7D2F181")
            self.assertTrue(input_image_url.is_displayed(), msg="Image URL input is not displayed.")
            input_image_url.send_keys(image_url)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit_id and input_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")