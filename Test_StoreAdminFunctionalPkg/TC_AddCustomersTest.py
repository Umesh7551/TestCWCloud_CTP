from CommonImportsPkg.common_imports import *
from login import Login


class AddCustomersTest(unittest.TestCase):
    def __init__(self, methodName='test_customers', data=None):
        super(AddCustomersTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_customers(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # username = self.data['test_customers']['username']
            # password = self.data['test_customers']['password']
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

            menu_sales = self.driver.find_element(By.XPATH, "//span[text()='Sales']")
            self.assertTrue(menu_sales.is_displayed(), msg="Sales Menu is not Displayed")
            menu_sales.click()
            time.sleep(5)

            sidebar_menu_customers = self.driver.find_element(By.XPATH,
                                                              "//span[text()='Customers']")
            self.assertTrue(sidebar_menu_customers.is_displayed(),
                            msg="Customers menu is not displayed.")
            sidebar_menu_customers.click()
            time.sleep(5)

            add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
            self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
            add_new_button.click()
            time.sleep(5)

            registered_store = self.data["test_customers"]["Registered Store"]
            input_registered_store = self.driver.find_element(By.ID, "headerTab_2353CF69FBB94A8C8C2F9C55F785B8CF")
            self.assertTrue(input_registered_store.is_displayed(), msg="Registered Store input is not displayed.")
            input_registered_store.send_keys(registered_store)
            time.sleep(5)

            active_check = self.driver.find_element(By.ID, "headerTab_3BAFE2386E9947CAA5875571B42DE999")
            if active_check.is_selected():
                pass
            else:
                active_check.click()

            firstname = self.data["test_customers"]["First Name"]
            input_firstname = self.driver.find_element(By.ID, "headerTab_1B540617B4374162BCCE219EF7D15365")
            self.assertTrue(input_firstname.is_displayed(), msg="First Name input is not displayed.")
            input_firstname.send_keys(firstname)
            time.sleep(5)

            name = self.data["test_customers"]["Name"]
            input_name = self.driver.find_element(By.ID, "headerTab_3510E858B362493EBE47062864E0001B")
            self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
            input_name.send_keys(name)
            time.sleep(5)

            lastname = self.data["test_customers"]["Last Name"]
            input_lastname = self.driver.find_element(By.ID, "headerTab_F73EDEEFC2454F2D98AAB99219032244")
            self.assertTrue(input_lastname.is_displayed(), msg="Last Name input is not displayed.")
            input_lastname.send_keys(lastname)
            time.sleep(5)

            mobile = self.data["test_customers"]["Mobile No"]
            input_mobile = self.driver.find_element(By.ID, "headerTab_90DDABD2BFD1446B8B6142A3D88D5728")
            self.assertTrue(input_mobile.is_displayed(), msg="Mobile input is not displayed.")
            input_mobile.send_keys(mobile)
            time.sleep(5)

            country_code = self.data["test_customers"]["Country Code"]
            input_country_code = self.driver.find_element(By.ID, "headerTab_4D66FA76BD134195B307D7BF15B530BA")
            self.assertTrue(input_country_code.is_displayed(), msg="Country Code input is not displayed.")
            input_country_code.send_keys(country_code)
            time.sleep(5)

            email = self.data["test_customers"]["Email"]
            input_email = self.driver.find_element(By.ID, "headerTab_8B96C59CACE54500AB145D9DCC5F3107")
            self.assertTrue(input_email.is_displayed(), msg="Email input is not displayed.")
            input_email.send_keys(email)
            time.sleep(5)

            pincode = self.data["test_customers"]["Pincode"]
            input_pincode = self.driver.find_element(By.ID, "headerTab_4C336FDDC5FE4C2694B10943C144A312")
            self.assertTrue(input_pincode.is_displayed(), msg="Pincode input is not displayed.")
            input_pincode.send_keys(pincode)
            time.sleep(5)

            default_customer = self.data["test_customers"]["Default Customer"]
            input_default_customer = self.driver.find_element(By.ID, "headerTab_883F14CAFEF041AFB0F51E88A76F42F1")
            self.assertTrue(input_default_customer.is_displayed(), msg="Default Customer input is not displayed.")
            input_default_customer.send_keys(default_customer)
            time.sleep(5)

            credit_limit = self.data["test_customers"]["Credit Limit"]
            input_credit_limit = self.driver.find_element(By.ID, "headerTab_B8CFAF37257D4E90A726318ACD695F16")
            self.assertTrue(input_credit_limit.is_displayed(), msg="Credit Limit input is not displayed.")
            input_credit_limit.send_keys(credit_limit)
            time.sleep(5)

            payment_method = self.data["test_customers"]["Payment Method"]
            input_payment_method = self.driver.find_element(By.ID, "headerTab_CDBFB8C224F4448BB6595CA41DA0FDE9")
            self.assertTrue(input_payment_method.is_displayed(), msg="Payment Method input is not displayed.")
            input_payment_method.send_keys(payment_method)
            time.sleep(5)

            loyalty_level = self.data["test_customers"]["Loyalty Level"]
            input_loyalty_level = self.driver.find_element(By.ID, "headerTab_F7AE3393AA5B4A5B8C81A3086846F393")
            self.assertTrue(input_loyalty_level.is_displayed(), msg="Loyalty Level input is not displayed.")
            input_loyalty_level.send_keys(loyalty_level)
            time.sleep(5)

            loyalty_balance = self.data["test_customers"]["Loyalty Balance"]
            input_loyalty_balance = self.driver.find_element(By.ID, "headerTab_4489B4824A1C4F6F9682A063E332511D")
            self.assertTrue(input_loyalty_balance.is_displayed(), msg="Loyalty balance input is not displayed.")
            input_loyalty_balance.send_keys(loyalty_balance)
            time.sleep(5)

            last_visit_date = self.data["test_customers"]["Last Visit Date"]
            input_last_visit_date = self.driver.find_element(By.ID, "headerTab_A0CC26764EEC4045AC22FEA60F7E99F4")
            self.assertTrue(input_last_visit_date.is_displayed(), msg="Last Visit Date input is not displayed.")
            input_last_visit_date.send_keys(last_visit_date)
            time.sleep(5)

            last_billing_amount = self.data["test_customers"]["Last Billing Amount"]
            input_last_billing_amount = self.driver.find_element(By.ID,
                                                                 "headerTab_E36A6F84E8974643B783EAC340FE89F8")
            self.assertTrue(input_last_billing_amount.is_displayed(),
                            msg="Last Billing Amount input is not displayed.")
            input_last_billing_amount.send_keys(last_billing_amount)
            time.sleep(5)

            average_basket_value = self.data["test_customers"]["Average Basket Value"]
            input_average_basket_value = self.driver.find_element(By.ID,
                                                                  "headerTab_EC71BA75384B471981B11D3CBB9773A3")
            self.assertTrue(input_average_basket_value.is_displayed(),
                            msg="Average Basket value input is not displayed.")
            input_average_basket_value.send_keys(average_basket_value)
            time.sleep(5)

            no_of_visits = self.data["test_customers"]["No of Visits"]
            input_no_of_visits = self.driver.find_element(By.ID,
                                                          "headerTab_8F3DFA5E17B94CAAB49A239F296E35D5")
            self.assertTrue(input_no_of_visits.is_displayed(),
                            msg="Number of Visits input is not displayed.")
            input_no_of_visits.send_keys(no_of_visits)
            time.sleep(5)

            save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
            self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
            cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
            self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
            if input_name is not None:
                save_button.click()
            else:
                cancel_button.click()
            flash(f"You have passed {self.test_name.upper()} Test case.", "success")
        else:
            flash(f"You have not passed {self.test_name.upper()} Test case.", "error")
