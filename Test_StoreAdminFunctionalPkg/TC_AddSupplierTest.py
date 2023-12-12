from CommonImportsPkg.common_imports import *

class AddSupplierTest(unittest.TestCase):
    def __init__(self, methodName='test_addsupplier', data=None):
        super(AddSupplierTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_addsupplier(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addsupplier']['username']
            # password = self.data['test_addsupplier']['password']
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

            menu_purchase = self.driver.find_element(By.XPATH, "//span[text()='Sales']")
            self.assertTrue(menu_purchase.is_displayed(), msg="Purchase Menu is not Displayed")
            menu_purchase.click()
            time.sleep(5)

            sidebar_menu_supplier = self.driver.find_element(By.XPATH,
                                                             "//span[text()='Supplier']")
            self.assertTrue(sidebar_menu_supplier.is_displayed(),
                            msg="Supplier menu is not displayed.")
            sidebar_menu_supplier.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            business_unit = self.data["test_addsupplier"]["Business Unit"]
            input_business_unit = self.driver.find_element(By.ID, "headerTab_765FDEFCD5524686A3E1EBAB8E898740")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            supplier_code = self.data["test_addsupplier"]["Supplier Code"]
            input_supplier_code = self.driver.find_element(By.ID, "headerTab_52957BB4CB314F78B240E4D3856E8F2A")
            self.assertTrue(input_supplier_code.is_displayed(), msg="Supplier Code input is not displayed.")
            input_supplier_code.send_keys(supplier_code)
            time.sleep(5)

            name = self.data["test_addsupplier"]["Name"]
            input_name = self.driver.find_element(By.ID, "headerTab_98DC62FB03F84DDD947683A67A3DE902")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            supplier_category = self.data["test_addsupplier"]["Supplier Category"]
            input_supplier_category = self.driver.find_element(By.ID, "headerTab_98DC62FB03F84DDD947683A67A3DE902")
            self.assertTrue(input_supplier_category.is_displayed(), msg="Supplier Category input is not displayed.")
            input_supplier_category.send_keys(supplier_category)
            time.sleep(5)

            price_list = self.data["test_addsupplier"]["Price List"]
            input_price_list = self.driver.find_element(By.ID, "headerTab_1D6ABCCC41D341E08855D7CDC28B2EA6")
            self.assertTrue(input_price_list.is_displayed(), msg="Price List input is not displayed.")
            input_price_list.send_keys(price_list)
            time.sleep(5)

            description = self.data["test_addsupplier"]["Description"]
            input_description = self.driver.find_element(By.ID, "headerTab_80E0A44C5C9E4A94B0F9F31060F00991")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            reference_no = self.data["test_addsupplier"]["Reference_no"]
            input_reference_no = self.driver.find_element(By.ID, "headerTab_43B906199766449EB67B0FC39B87B44A")
            self.assertTrue(input_reference_no.is_displayed(), msg="Reference_no input is not displayed.")
            input_reference_no.send_keys(reference_no)
            time.sleep(5)

            gst_no = self.data["test_addsupplier"]["GST_No"]
            input_gst_no = self.driver.find_element(By.ID, "headerTab_20F2AD84DFB14D96AB7B5C08355211BB")
            self.assertTrue(input_gst_no.is_displayed(), msg="GST_no input is not displayed.")
            input_gst_no.send_keys(gst_no)
            time.sleep(5)

            payment_method = self.data["test_addsupplier"]["Payment_Method"]
            input_payment_method = self.driver.find_element(By.ID, "headerTab_BE13C5AE33A9486A81373A20DB06D7A4")
            self.assertTrue(input_payment_method.is_displayed(), msg="Payment Method input is not displayed.")
            input_payment_method.send_keys(payment_method)
            time.sleep(5)

            local_purchase_check = self.driver.find_element(By.ID, "headerTab_61A9AB12CEFE4DBEA8F3D5B3E694311E")
            if local_purchase_check.is_selected():
                pass
            else:
                local_purchase_check.click()

            payment_terms = self.data["test_addsupplier"]["Payment_Terms"]
            input_payment_terms = self.driver.find_element(By.ID, "headerTab_A317B4ECAA2A45E5AE240F70C031A8A9")
            self.assertTrue(input_payment_terms.is_displayed(), msg="Payment Terms input is not displayed.")
            input_payment_terms.send_keys(payment_terms)
            time.sleep(5)

            currency = self.data["test_addsupplier"]["Currency"]
            input_currency = self.driver.find_element(By.ID, "headerTab_9DA9E495F62F41959BE77685B5EB2B2C")
            self.assertTrue(input_currency.is_displayed(), msg="Currency input is not displayed.")
            input_currency.send_keys(currency)
            time.sleep(5)

            lead_days = self.data["test_addsupplier"]["Lead_Days"]
            input_lead_days = self.driver.find_element(By.ID, "headerTab_D099B2322C9A4385B8718F761A35E7C9")
            self.assertTrue(input_lead_days.is_displayed(), msg="Lead Days input is not displayed.")
            input_lead_days.send_keys(lead_days)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit and input_supplier_code and input_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
