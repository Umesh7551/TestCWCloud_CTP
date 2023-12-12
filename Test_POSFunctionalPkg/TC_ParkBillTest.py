from CommonImportsPkg.common_imports import *


class ParkBillTest(unittest.TestCase):
    def __init__(self, methodName='test_park_bill', data=None):
        super(ParkBillTest, self).__init__(methodName)
        self.data = data
        self.test_name = methodName

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_helper = Login(self.driver, self.data, self)

    def tearDown(self):
        self.driver.close()

    def test_park_bill(self):
        if self.data:
            self.login_helper.login()
            # self.driver.maximize_window()
            # Step 1: Open the URL
            # self.driver.get("https://test.cwcloud.in/")
            # self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
            # time.sleep(5)
            # Step 4: Enter username in the username input box
            # username = self.data['test_park_bill']['username']
            # password = self.data['test_park_bill']['password']
            # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
            # username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
            # username_input.send_keys(username)

            # Step 5: Enter password in the password input box
            # password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
            # password_input.send_keys(password)

            # Step 6: Click on the login button
            # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
            # login_button.click()
            # time.sleep(5)
            # self.assertEqual(self.driver.current_url, "https://test-app.cwcloud.in:8412/my-apps")

            # Step 6: Select POS
            # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
            pos = self.driver.find_element(By.XPATH, "//h4[text()='POS']")
            self.assertTrue(pos.is_displayed(), msg="POS is not displayed.")
            pos.click()
            time.sleep(5)
            # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/")
            # self.driver.implicitly_wait(5)

            # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/")
            # # Loop through the handles to find the handle of the third window
            # for handle1 in all_handles:
            #     if handle1 != main_window and handle1 != handle1:
            #         self.driver.switch_to.window(handle1)
            #         break

            # Get the current window handle (main window)
            main_window = self.driver.current_window_handle

            # Get all window handles (including the main window)
            all_handles = self.driver.window_handles

            # Switch to the new window
            for handle in all_handles:
                if handle != main_window:
                    self.driver.switch_to.window(handle)
                    break
            # Click on Till
            time.sleep(5)
            till = self.driver.find_element(By.XPATH, "//div[@class='ant-card-body']")
            till.click()
            # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/open-till-component")
            # insert amount into Amount Input box
            json_amount = self.data['test_park_bill']['amount']
            # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
            # amount.send_keys(json_amount)

            # insert note into note input box
            json_note = self.data['test_park_bill']['note']
            # note = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
            # note.send_keys(json_note)

            # Click open till button
            # open_till_button = self.driver.find_element(By.XPATH, "//button[@id='step3']")
            # open_till_button.click()

            # pos_search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for products by code/name']")
            # pos_search_input.send_keys("Blue Water Bottle")
            # Wait for the input element to be present and visible
            wait = WebDriverWait(self.driver, 20)
            pos_search_input = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Search for products by code/name']")))

            json_pos_search_input = self.data['test_park_bill']['pos_search_input']
            # Now you can interact with the input element
            pos_search_input.send_keys(json_pos_search_input)
            # Simulate pressing the Enter keyole
            pos_search_input.send_keys(Keys.RETURN)
            time.sleep(5)

            # Increase and Decrease Quantity buttons are showing on double-clicking

            # increase_qty = self.driver.find_element(By.XPATH, "//span[@title='Increase Qty']")
            # increase_qty = self.driver.find_element(By.XPATH, "//span[@class='anticon anticon-plus']")
            # Perform a double click
            # action_chains = ActionChains(self.driver)
            # action_chains.double_click(increase_qty).perform()
            # time.sleep(10)
            #
            # decrease_qty = self.driver.find_element(By.XPATH, "//span[@class='anticon anticon-minus']")
            # decrease_qty.click()

            # Select More Actions Drop down box
            more_actions_select = self.driver.find_element(By.XPATH,
                                                           "//div[@class='ant-select selecItem ant-select-single ant-select-show-arrow']")
            more_actions_select.click()

            park_bill = self.driver.find_element(By.XPATH, "//div[text()='Park Bill']")
            park_bill.click()
            time.sleep(5)

            yes_button_onpopup = self.driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
            # yes_button_onpopup = self.driver.find_element(By.XPATH, "//span[text()='Yes']")
            if yes_button_onpopup.is_displayed() and yes_button_onpopup.is_enabled():
                yes_button_onpopup.click()

            else:
                no_button_onpopup = self.driver.find_element(By.XPATH, "//span[text()='No']")
                no_button_onpopup.click()

            parked_bills_menu = self.driver.find_element(By.XPATH, "//span[text()='Parked bills']")
            parked_bills_menu.click()
            time.sleep(5)

            right_arrow = self.driver.find_element(By.XPATH, "//span[@class='anticon anticon-right']")
            if right_arrow.is_displayed():
                right_arrow.click()
                time.sleep(5)
                retrieve_sale = self.driver.find_element(By.XPATH, "//p[text()='Retrieve sale']")
                if retrieve_sale.is_displayed():
                    retrieve_sale.click()
                    time.sleep(5)
                    # point_of_sale = self.driver.find_element(By.XPATH, "//span[text()='Point of Sale']")
                    # point_of_sale.click()
                    # time.sleep(5)
                    pay_button = self.driver.find_element(By.XPATH, "//button[@id='step11']")
                    pay_button.click()
                    # self.driver.implicitly_wait(10)
                    time.sleep(10)
                    # Cash Button
                    cash_button = self.driver.find_element(By.XPATH, "//button[text()='Cash']")
                    cash_button.click()
                    if cash_button.is_displayed() and cash_button.is_enabled():
                        pass
                    else:
                        # Card Button
                        card_button = self.driver.find_element(By.XPATH, "//button[text()='Card']")
                        card_button.click()

                    # Add Payment Button
                    add_payment = self.driver.find_element(By.XPATH, "//span[text()='Add Payment']")
                    add_payment.click()

                    # Complete Order Button
                    # complete_order = self.driver.find_element(By.XPATH, "//span[text()='Complete Order']")
                    # complete_order.click()
                else:
                    discard_sale = self.driver.find_element(By.XPATH, "//p[text()='Discard sale']")
                    discard_sale.click()
                    time.sleep(5)
            else:
                no_data = self.driver.find_element(By.XPATH, "//div[text()='No Data']")
                if no_data.is_displayed():
                    self.driver.find_element(By.XPATH, "//span[text()='Point of Sale']").click()
            # # Create a Select object
            # select = Select(more_actions_select)
            #
            # # Select an option by visible text (replace 'Your Role Text' with the actual text of the role you want to select)
            # select.select_by_visible_text("Park Bill")
            time.sleep(5)
            flash(f"You have passed { self.test_name.upper() } Test case.", "success")
        else:
            flash(f"You have not passed { self.test_name.upper() } Test case.", "error")
