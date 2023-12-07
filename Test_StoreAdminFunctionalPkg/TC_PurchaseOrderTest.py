from CommonImportsPkg.common_imports import *

class PurchaseOrderTest(unittest.TestCase):
    def __init__(self, methodName='test_purchase_order', data=None):
        super(PurchaseOrderTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_purchase_order(self):
        if self.data:
            self.driver.maximize_window()

            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_purchase_order']['username']
            # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
            username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
            self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
            username_input.send_keys(username)
            time.sleep(5)

            # Step 5: Enter password in the password input box
            password = self.data['test_purchase_order']['password']
            password_input = self.driver.find_element(By.XPATH,
                                                      "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
            self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
            password_input.send_keys(password)
            time.sleep(5)

            # Step 6: Click on the login button
            login_button = self.driver.find_element(By.XPATH,
                                                    "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
            self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
            if username_input and password_input is not None:
                login_button.click()
            time.sleep(10)
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

            sidebar_menu_purchase_order = self.driver.find_element(By.XPATH,
                                                                   "//span[text()='Purchase Order']")
            self.assertTrue(sidebar_menu_purchase_order.is_displayed(),
                            msg="Purchase Order menu is not displayed.")
            sidebar_menu_purchase_order.click()
            time.sleep(5)

            business_unit = self.data["test_purchase_order"]["Business_Unit"]
            input_business_unit = self.driver.find_element(By.ID, "headerTab_40D1EE8DA564487D9373AD3DBF21F5C4")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            date = self.data["test_purchase_order"]["Date"]
            input_date = self.driver.find_element(By.ID, "headerTab_14784A1CE0E74C65947CF72C73F0CC84")
            self.assertTrue(input_date.is_displayed(), msg="Date input is not displayed.")
            input_date.send_keys(date)
            time.sleep(5)

            supplier = self.data["test_purchase_order"]["Supplier"]
            input_supplier = self.driver.find_element(By.ID, "headerTab_9B8D684D9D6340BDB1C1665FDEF9D810")
            self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
            input_supplier.send_keys(supplier)
            time.sleep(5)

            supplier_address = self.data["test_purchase_order"]["Supplier_Address"]
            input_supplier_address = self.driver.find_element(By.ID, "headerTab_C52D2B62DA794C1480228699BC39D009")
            self.assertTrue(input_supplier_address.is_displayed(), msg="Supplier Address input is not displayed.")
            input_supplier_address.send_keys(supplier_address)
            time.sleep(5)

            delivery_location = self.data["test_purchase_order"]["Delivery_Location"]
            input_delivery_location = self.driver.find_element(By.ID, "headerTab_03BA9FF390A448D98467057400A508A2")
            self.assertTrue(input_delivery_location.is_displayed(), msg="Delivery Location input is not displayed.")
            input_delivery_location.send_keys(delivery_location)
            time.sleep(5)

            storage_location = self.data["test_purchase_order"]["Storage_Location"]
            input_storage_location = self.driver.find_element(By.ID, "headerTab_F4C464FF229D4F799C28238DA9E4B525")
            self.assertTrue(input_storage_location.is_displayed(), msg="Storage Location input is not displayed.")
            input_storage_location.send_keys(storage_location)
            time.sleep(5)

            payment_terms = self.data["test_purchase_order"]["Payment_Terms"]
            input_payment_terms = self.driver.find_element(By.ID, "headerTab_48DFDB66892741B3A8AE4D361454F43F")
            self.assertTrue(input_payment_terms.is_displayed(), msg="Payment Terms input is not displayed.")
            input_payment_terms.send_keys(payment_terms)
            time.sleep(5)

            price_list = self.data["test_purchase_order"]["Price_List"]
            input_price_list = self.driver.find_element(By.ID, "headerTab_2466B04BCED24C04AE6FE5EF5FAD5FE4")
            self.assertTrue(input_price_list.is_displayed(), msg="Price List input is not displayed.")
            input_price_list.send_keys(price_list)
            time.sleep(5)

            supplier_reference = self.data["test_purchase_order"]["Supplier_reference"]
            input_supplier_reference = self.driver.find_element(By.ID, "headerTab_2466B04BCED24C04AE6FE5EF5FAD5FE4")
            self.assertTrue(input_supplier_reference.is_displayed(),
                            msg="Supplier Reference input is not displayed.")
            input_supplier_reference.send_keys(supplier_reference)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_business_unit and input_date and input_supplier and input_storage_location and input_price_list is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")