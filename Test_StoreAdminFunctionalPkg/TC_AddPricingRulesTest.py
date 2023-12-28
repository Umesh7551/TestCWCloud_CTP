from CommonImportsPkg.common_imports import *
from login import Login


class AddPricingRulesTest(unittest.TestCase):
    def __init__(self, methodName='test_add_pricing_rules', data=None):
        super(AddPricingRulesTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_add_pricing_rules(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_addPricing_Rules']['username']
            # password = self.data['test_addPricing_Rules']['password']
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
            # # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
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

            sidebar_menu_pricing_rules = self.driver.find_element(By.XPATH,
                                                                  "//span[text()='Pricing Rules']")
            self.assertTrue(sidebar_menu_pricing_rules.is_displayed(),
                            msg="Pricing Rules menu is not displayed.")
            sidebar_menu_pricing_rules.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            type = self.data["test_add_pricing_rules"]["Type"]
            input_type = self.driver.find_element(By.ID, "headerTab_B3A125482C994AD784298943261113AF")
            self.assertTrue(input_type.is_displayed(), msg="Type input is not displayed.")
            input_type.send_keys(type)
            time.sleep(5)

            name = self.data["test_add_pricing_rules"]["Name"]
            input_name = self.driver.find_element(By.ID, "headerTab_1E2751866DC846728765C9C883C79E6A")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            printed_name = self.data["test_add_pricing_rules"]["Printed_Name"]
            input_printed_name = self.driver.find_element(By.ID, "headerTab_15D5EA483D2A43D794E3FF500D8D9DA3")
            self.assertTrue(input_printed_name.is_displayed(), msg="Printed Name input is not displayed.")
            input_printed_name.send_keys(printed_name)
            time.sleep(5)

            description = self.data["test_add_pricing_rules"]["Description"]
            input_description = self.driver.find_element(By.ID, "headerTab_3A6C9325FFEC42ACAC9E1BE83248F789")
            self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
            input_description.send_keys(description)
            time.sleep(5)

            start_date = self.data["test_add_pricing_rules"]["Start_Date"]
            input_start_date = self.driver.find_element(By.ID, "headerTab_6184E60E039B474B96D37D32A6C3C70C")
            self.assertTrue(input_start_date.is_displayed(), msg="Start Date input is not displayed.")
            input_start_date.send_keys(start_date)
            time.sleep(5)

            end_date = self.data["test_add_pricing_rules"]["End_Date"]
            input_end_date = self.driver.find_element(By.ID, "headerTab_1EA1BC1C84D14D078A20CD3291256F34")
            self.assertTrue(input_end_date.is_displayed(), msg="End Date input is not displayed.")
            input_end_date.send_keys(end_date)
            time.sleep(5)

            coupon_expiry_date = self.data["test_add_pricing_rules"]["Coupon_Expiry_Date"]
            input_coupon_expiry_date = self.driver.find_element(By.ID, "headerTab_A2511C5ED6C64CE393C940A0566CA3C5")
            self.assertTrue(input_coupon_expiry_date.is_displayed(), msg="Coupon Expiry Date input is not displayed.")
            input_coupon_expiry_date.send_keys(coupon_expiry_date)
            time.sleep(5)

            discount_type = self.data["test_add_pricing_rules"]["Discount_Type"]
            input_discount_type = self.driver.find_element(By.ID, "headerTab_81CA40B331EE47D794C5E67F5A8047BA")
            self.assertTrue(input_discount_type.is_displayed(),
                            msg="Discount Type input is not displayed.")
            input_discount_type.send_keys(discount_type)
            time.sleep(5)

            no_of_coupons = self.data["test_add_pricing_rules"]["No_of_Coupons"]
            input_no_of_coupons = self.driver.find_element(By.ID, "headerTab_3FFFB46E755C48E188486B12F71AD653")
            self.assertTrue(input_no_of_coupons.is_displayed(),
                            msg="No of Coupons input is not displayed.")
            input_no_of_coupons.send_keys(no_of_coupons)
            time.sleep(5)

            gift_voucher_type = self.data["test_add_pricing_rules"]["Gift_Voucher_Type"]
            input_gift_voucher_type = self.driver.find_element(By.ID, "headerTab_E0B20B2826D34F1DB24B98163F1870D1")
            self.assertTrue(input_gift_voucher_type.is_displayed(),
                            msg="Gift Voucher Type input is not displayed.")
            input_gift_voucher_type.send_keys(gift_voucher_type)
            time.sleep(5)

            minimum_qty = self.data["test_add_pricing_rules"]["Minimum_Qty"]
            input_minimum_qty = self.driver.find_element(By.ID, "headerTab_B7CFAF12181644B6A38196DEA23700E1")
            self.assertTrue(input_minimum_qty.is_displayed(),
                            msg="Minimum Quantity input is not displayed.")
            input_minimum_qty.send_keys(minimum_qty)
            time.sleep(5)

            maximum_qty = self.data["test_add_pricing_rules"]["Maximum_Qty"]
            input_maximum_qty = self.driver.find_element(By.ID, "headerTab_9BB4F090B970452FB3398F80C091C60D")
            self.assertTrue(input_maximum_qty.is_displayed(),
                            msg="Maximum Quantity input is not displayed.")
            input_maximum_qty.send_keys(maximum_qty)
            time.sleep(5)

            discount_x_qty = self.data["test_add_pricing_rules"]["Discount_X_Qty"]
            input_discount_x_qty = self.driver.find_element(By.ID, "headerTab_72C66F3E59114363BEE65D4595D3E2B7")
            self.assertTrue(input_discount_x_qty.is_displayed(),
                            msg="Discount X Quantity input is not displayed.")
            input_discount_x_qty.send_keys(discount_x_qty)
            time.sleep(5)

            discount_y_qty = self.data["test_add_pricing_rules"]["Discount_Y_Qty"]
            input_discount_y_qty = self.driver.find_element(By.ID, "headerTab_C5466B6E083D4E52847868F792FB1B7C")
            self.assertTrue(input_discount_y_qty.is_displayed(),
                            msg="Discount Y Quantity input is not displayed.")
            input_discount_y_qty.send_keys(discount_y_qty)
            time.sleep(5)

            minimum_bill_amount = self.data["test_add_pricing_rules"]["Minimum_Bill_Amount"]
            input_minimum_bill_amount = self.driver.find_element(By.ID, "headerTab_C7CCB554D5CD4D40ACA88FC28C8FFC6C")
            self.assertTrue(input_minimum_bill_amount.is_displayed(),
                            msg="Minimum Bill Amount input is not displayed.")
            input_minimum_bill_amount.send_keys(minimum_bill_amount)
            time.sleep(5)

            maximum_bill_amount = self.data["test_add_pricing_rules"]["Maximum_Bill_Amount"]
            input_maximum_bill_amount = self.driver.find_element(By.ID,
                                                                 "headerTab_94738DCF997A4F16AEED3069A43604AF")
            self.assertTrue(input_maximum_bill_amount.is_displayed(),
                            msg="Minimum Bill Amount input is not displayed.")
            input_maximum_bill_amount.send_keys(maximum_bill_amount)
            time.sleep(5)

            pos_sales_type = self.data["test_add_pricing_rules"]["POS_Sales_Type"]
            input_pos_sales_type = self.driver.find_element(By.ID,
                                                            "headerTab_318C3C5AA0034EE2B8D0FB8589D85B83")
            self.assertTrue(input_pos_sales_type.is_displayed(),
                            msg="POS Sales Type input is not displayed.")
            input_pos_sales_type.send_keys(pos_sales_type)
            time.sleep(5)

            fixed_unit_price = self.data["test_add_pricing_rules"]["Fixed_Unit_Price"]
            input_fixed_unit_price = self.driver.find_element(By.ID,
                                                              "headerTab_42B7DDEF58614DB4AE3C1F65BA214E4E")
            self.assertTrue(input_fixed_unit_price.is_displayed(),
                            msg="POS Sales Type input is not displayed.")
            input_fixed_unit_price.send_keys(fixed_unit_price)
            time.sleep(5)

            active_check = self.driver.find_element(By.ID, "headerTab_D9A5F490B80B4FEE9C99B303D6AAB6D9")
            self.assertTrue(active_check.is_displayed(), msg="Active Check is not displayed.")
            if active_check.is_selected():
                pass
            else:
                active_check.click()

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_type and input_name and input_start_date is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
