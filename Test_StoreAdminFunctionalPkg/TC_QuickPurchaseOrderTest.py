from CommonImportsPkg.common_imports import *

class QuickPurchaseOrderTest(unittest.TestCase):
    def __init__(self, methodName='test_quick_purchase_order', data=None):
        super(QuickPurchaseOrderTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_quick_purchase_order(self):
        self.driver.maximize_window()

        self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
        time.sleep(5)
        username = data['test_quick_purchase_order']['username']
        # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
        username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
        self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
        username_input.send_keys(username)
        time.sleep(5)

        # Step 5: Enter password in the password input box
        password = data['test_quick_purchase_order']['password']
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

        sidebar_menu_quick_purchase_order = self.driver.find_element(By.XPATH,
                                                                     "//span[text()='Quick Purchase Order']")
        self.assertTrue(sidebar_menu_quick_purchase_order.is_displayed(),
                        msg="Quick Purchase Order menu is not displayed.")
        sidebar_menu_quick_purchase_order.click()
        time.sleep(5)

        business_unit = data["test_quick_purchase_order"]["Business_Unit"]
        input_business_unit = self.driver.find_element(By.ID, "businessunit")
        self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
        input_business_unit.send_keys(business_unit)
        time.sleep(5)

        supplier = data["test_quick_purchase_order"]["Supplier"]
        input_supplier = self.driver.find_element(By.ID, "supplier")
        self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
        input_supplier.send_keys(supplier)
        time.sleep(5)

        remarks = data["test_quick_purchase_order"]["Remarks"]
        input_remarks = self.driver.find_element(By.ID, "remarks")
        self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
        input_remarks.send_keys(remarks)
        time.sleep(5)

        date = data["test_quick_purchase_order"]["Date"]
        input_date = self.driver.find_element(By.ID, "date")
        self.assertTrue(input_date.is_displayed(), msg="Date input is not displayed.")
        input_date.send_keys(date)
        time.sleep(5)

        save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']")
        self.assertTrue(save_button.is_displayed(), msg="Save Button is not displayed.")
        confirm_button = self.driver.find_element(By.ID, "Confirm")
        self.assertTrue(confirm_button.is_displayed(), msg="Confirm Button is not displayed.")
        save_button.click()
        confirm_button.click()
