from CommonImportsPkg.common_imports import *

class QuickStockCountTest(unittest.TestCase):
    def __init__(self, methodName='test_quick_stock_count', data=None):
        super(QuickStockCountTest, self).__init__(methodName)
        self.data = data

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_quick_stock_count(self):
        if self.data:
            self.driver.maximize_window()

            self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            time.sleep(5)
            username = self.data['test_quick_stock_count']['username']
            password = self.data['test_quick_stock_count']['password']
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

            menu_inventory = self.driver.find_element(By.XPATH, "//span[text()='Inventory']")
            self.assertTrue(menu_inventory.is_displayed(), msg="Inventory Menu is not Displayed")
            menu_inventory.click()
            time.sleep(5)

            sidebar_menu_quick_stock_count = self.driver.find_element(By.XPATH,
                                                                      "//span[text()='Quick Stock Count']")
            self.assertTrue(sidebar_menu_quick_stock_count.is_displayed(),
                            msg="Quick Stock Count menu is not displayed.")
            sidebar_menu_quick_stock_count.click()
            time.sleep(5)

            business_unit = self.data["test_quick_stock_count"]["Business_Unit"]
            input_business_unit = self.driver.find_element(By.ID, "businessunit")
            self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
            input_business_unit.send_keys(business_unit)
            time.sleep(5)

            type = self.data["test_quick_stock_count"]["Type"]
            input_type = self.driver.find_element(By.ID, "ctype")
            self.assertTrue(input_type.is_displayed(), msg="Type input is not displayed.")
            input_type.send_keys(type)
            time.sleep(5)

            remarks = self.data["test_quick_stock_count"]["Remarks"]
            input_remarks = self.driver.find_element(By.ID, "remarks")
            self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
            input_remarks.send_keys(remarks)
            time.sleep(5)

            date = self.data["test_quick_stock_count"]["Date"]
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
            flash("You have passed Test case.", "success")
        else:
            flash("You have not passed Test case.", "error")