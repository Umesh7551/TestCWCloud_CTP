import datetime
import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import json
import time
import unittest
from HtmlTestRunner import HTMLTestRunner
from PIL import Image, ImageTk
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CW Test Platform [CTP]")
        # self.root.resizable(False, False)
        self.root.geometry('400x300')
        self.root.iconbitmap(r'logocw.ico')
        self.heading_label = ttk.Label(root, text="Welcome to CW Test Platform [CTP]", font=50, width=50)
        self.heading_label.grid(row=0, column=0, padx=40, pady=10)

        self.load_button = ttk.Button(root, text="Load JSON File", width=20, command=self.load_json)
        self.load_button.place(x=40, y=50)

        self.start_button = ttk.Button(root, text='Start Test', command=self.run_tests, width=20)
        self.start_button.place(x=180, y=50)

        self.text_label = ttk.Label(root, text="Powered By")
        self.text_label.place(x=140, y=100)
        # Create a PhotoImage object
        # image = ImageTk.PhotoImage(PIL.Image.open("logo.png"))  # Replace "path_to_your_image.png" with the path to your image
        # Load the image using PIL
        image = Image.open("static/images/logo.png")

        # Convert the PIL image to a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(root, image=photo)
        # self.image_label = tk.Label(root, image=image)
        self.image_label.photo = photo
        self.image_label.place(x=50, y=130)
        # self.image_label.grid(row=4, column=2)
        # Initialize data variable to store the loaded JSON data
        self.data = None

    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'r') as json_file:
                self.data = json.load(json_file)
                if self.data is not None:
                    messagebox.showinfo("Success", "JSON File loaded successfully!!!")
                else:
                    messagebox.showerror("Error", "Please select valid file!!!")
            # # Run unittest test cases using the data from the JSON file
            # self.run_tests(data)

    def run_tests(self):
        # Implement your unittest test cases here
        # You can create test cases and use the data from the JSON file for testing
        if self.data:
            # Run unittest test cases using the data from the JSON file
            self.run_unittest_tests(self.data)
        else:
            messagebox.showerror("Error", "Please First select JSON file!!!")

    def run_unittest_tests(self, data):
        # Example unittest test case
        class TestPOSData(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def tearDown(self):
                self.driver.close()

            @unittest.SkipTest
            def test_point_of_sale(self):
                # Implement test logic using data['test_login']
                self.driver.maximize_window()
                # Step 1: Open the URL
                # self.driver.get("https://test.cwcloud.in/")
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                self.assertEqual(self.driver.current_url, "https://test-auth.cwcloud.in:8412/sign-in")
                # Step 2: Click on the "Login" link text
                # login_link = self.driver.find_element(By.LINK_TEXT, "Login")
                # login_link = self.driver.find_element(By.XPATH, "//span[@class='ff-Inter text-xs text-darkBlack mr-4 xl:mr-10 hover:opacity-70 transition-all duration-200 ease-in hidden sm:block']")
                # login_link.click()
                # self.assertEqual(self.driver.current_url, "https://test-auth.cwcloud.in:8412/sign-in")
                # Step 3: Switch to the new tab or window
                # Get the current window handle (main window)
                # main_window = self.driver.current_window_handle
                #
                # # Get all window handles (including the main window)
                # all_handles = self.driver.window_handles
                #
                # # Switch to the new window
                # for handle in all_handles:
                #     if handle != main_window:
                #         self.driver.switch_to.window(handle)
                #         break

                # Now you're in the new tab/window.
                time.sleep(10)
                username = data['test_point_of_sale']['username']
                password = data['test_point_of_sale']['password']
                # Step 4: Enter username in the username input box
                # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
                username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
                self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
                username_input.send_keys(username)

                # Step 5: Enter password in the password input box
                password_input = self.driver.find_element(By.XPATH,
                                                          "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
                self.assertTrue(password_input.is_displayed(), msg="Password input box is not displayed.")
                password_input.send_keys(password)

                # Step 6: Click on the login button
                login_button = self.driver.find_element(By.XPATH,
                                                        "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
                self.assertTrue(login_button.is_displayed(), msg="Login Button is not displayed.")
                login_button.click()
                time.sleep(10)
                # self.assertEqual(self.driver.current_url, "https://test-app.cwcloud.in:8412/my-apps")

                # Step 6: Select POS
                # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
                pos = self.driver.find_element(By.XPATH, "//h4[text()='POS']")
                self.assertTrue(pos.is_displayed(), msg="POS Article is not displayed.")
                # pos = self.driver.find_element(By.XPATH, "//h4[@class='text-[#101828] font-semibold ff-inter text-[18px]']")
                pos.click()
                time.sleep(10)
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
                time.sleep(10)

                till = self.driver.find_element(By.XPATH, "//div[@class='ant-card-body']")
                till.click()
                # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/open-till-component")
                # insert amount into Amount Input box
                json_amount = data['test_point_of_sale']['amount']
                # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # amount.send_keys(json_amount)

                # insert note into note input box
                json_note = data['test_point_of_sale']['note']
                # note = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # note.send_keys(json_note)

                # Click open till button
                # open_till_button = self.driver.find_element(By.XPATH, "//button[@id='step3']")
                # open_till_button.click()

                # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/pos")
                # logging.info("Login Test Passed")

                # pos_search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Search for products by code/name']")
                # pos_search_input.send_keys("Blue Water Bottle")

                wait = WebDriverWait(self.driver, 20)
                search_customer = wait.until(
                    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter customer number/name']")))
                # Search Customer Name or Number
                # search_customer = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter customer number/name']")
                # search_customer = self.driver.find_element(By.XPATH, "//input[@class='ant-input']")
                # search_customer.click()
                # if search_customer.is_displayed():
                #     json_customer_search = data['test_login']['customer_search']
                #     # popup_search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
                #     popup_search = self.driver.find_element(By.XPATH, "//input[@class='ant-input ant-input-lg']")
                #     popup_search.send_keys(json_customer_search)
                #     # print(popup_search.text)
                #     popup_search.send_keys(Keys.RETURN)
                #     if popup_search.is_displayed():
                #         # Select searched customer
                #         self.driver.find_element(By.XPATH, "//div[@class='ant-col ant-col-17 ant-col-offset-1']").click()
                #     else:
                #         # Add New Customer
                #         self.driver.find_element(By.XPATH, "//div[@class='ant-row ant-row-center']").click()
                #         time.sleep(5)
                #         #First Name
                #         json_first_name = data['test_point_of_sale']['firstname']
                #         first_name = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_name']")
                #         first_name.clear()
                #         first_name.send_keys(json_first_name)
                #
                #         # Last Name
                #         json_last_name = data['test_point_of_sale']['lastname']
                #         last_name = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_lastName']")
                #         last_name.send_keys(json_last_name)
                #
                #         #Email
                #         json_email = data['test_point_of_sale']['email']
                #         email = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_email']")
                #         email.send_keys(json_email)
                #
                #         # Contact Number
                #         json_phone = data['test_point_of_sale']['phone']
                #         phone = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_mobile']")
                #         phone.send_keys(json_phone)
                #
                #         # Pincode
                #         json_pincode = data['test_point_of_sale']['pincode']
                #         pincode = self.driver.find_element(By.XPATH, "//input[@id='addCustomer_pincode']")
                #         pincode.send_keys(json_pincode)
                #
                #         # Create New Customer Button
                #         create_new_customer_button = self.driver.find_element(By.XPATH, "//button[@class='ant-btn customerDetailsSubmitBtnBtn']")
                #         create_new_customer_button.click()

                # Wait for the input element to be present and visible
                wait = WebDriverWait(self.driver, 20)
                pos_search_input = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//input[@placeholder='Search for products by code/name']")))

                # Now you can interact with the input element
                json_pos_search_input = data['test_point_of_sale']['pos_search_input']
                pos_search_input.send_keys(json_pos_search_input)
                # Simulate pressing the Enter keyole
                pos_search_input.send_keys(Keys.RETURN)
                time.sleep(20)

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

                # Search Customer Name or Number
                # search_customer = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter customer number/name']")
                # search_customer.click()
                #
                # popup_search = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
                # popup_search.send_keys("Umesh")
                # popup_search.send_keys(Keys.RETURN)

                # Wait for some time for the search result to appear
                # time.sleep(10)

                pay_button = self.driver.find_element(By.XPATH, "//button[@id='step11']")
                pay_button.click()
                # self.driver.implicitly_wait(10)
                time.sleep(10)
                # Cash Button
                cash_button = self.driver.find_element(By.XPATH, "//button[text()='Cash']")
                cash_button.click()
                if cash_button.is_enabled():
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

                # Handle New Chrome Window for print Reciept
                new_window_handle = None

                for handle in all_handles:
                    if handle != main_window:
                        new_window_handle = handle
                        break

                if new_window_handle:
                    self.driver.switch_to.window(new_window_handle)
                time.sleep(10)
                # save_button = self.driver.find_element(By.XPATH, "//cr-button[text()='Save']")
                # save_button.click()

                self.driver.switch_to.window(main_window)
                messagebox.showinfo("Success", "You have passed Point of Sale test case. ")

                # You can add more test cases for 'test_signup', 'test_park_bill', 'test_cashManagement', etc.

            # @unittest.SkipTest
            def test_park_bill(self):
                self.driver.maximize_window()

                # Step 1: Open the URL
                # self.driver.get("https://test.cwcloud.in/")
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                # Step 4: Enter username in the username input box
                username = data['test_park_bill']['username']
                password = data['test_park_bill']['password']
                # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
                username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
                username_input.send_keys(username)

                # Step 5: Enter password in the password input box
                password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
                password_input.send_keys(password)

                # Step 6: Click on the login button
                login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
                login_button.click()
                time.sleep(5)
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
                json_amount = data['test_park_bill']['amount']
                # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # amount.send_keys(json_amount)

                # insert note into note input box
                json_note = data['test_park_bill']['note']
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

                json_pos_search_input = data['test_park_bill']['pos_search_input']
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
                        complete_order = self.driver.find_element(By.XPATH, "//span[text()='Complete Order']")
                        complete_order.click()
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
                messagebox.showinfo("Success", "You have passed parked bill test case.")

            @unittest.SkipTest
            def test_cashManagement(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(30)
                username = data['test_cashManagement']['username']
                password = data['test_cashManagement']['password']
                # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
                # username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
                # username_input.send_keys(username)

                # Step 5: Enter password in the password input box
                # password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
                # password_input.send_keys(password)

                # Step 6: Click on the login button
                # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
                # login_button.click()
                # Step 6: Select POS
                # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
                pos = self.driver.find_element(By.XPATH, "//h4[text()='POS']")
                if pos.is_displayed():
                    pos.click()
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
                time.sleep(20)
                # till = self.driver.find_element(By.XPATH, "//div[@class='ant-card ant-card-bordered']")
                # till.click()
                # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/open-till-component")
                # insert amount into Amount Input box
                # json_amount = data['test_cashManagement']['amount']
                # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # amount.send_keys(json_amount)

                # insert note into note input box
                # json_note = data['test_cashManagement']['note']
                # note = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # note.send_keys(json_note)

                # Click open till button
                # open_till_button = self.driver.find_element(By.XPATH, "//button[@id='step3']")
                # open_till_button.click()

                time.sleep(10)

                menu_cashManagement = self.driver.find_element(By.XPATH, "//span[text()='Cash Management']")
                if menu_cashManagement.is_displayed():
                    menu_cashManagement.click()
                    time.sleep(10)
                    remove_cash = self.driver.find_element(By.XPATH, "//span[text()='Remove Cash']")
                    add_cash = self.driver.find_element(By.XPATH, "//span[text()='Add Cash']")

                    # if remove_cash:
                    #     # Click the "Remove Cash" button
                    #     # remove_cash.click()
                    #     # Wait for the associated pop-up to appear (you may need to adjust the wait time)
                    #     time.sleep(10)
                    #     # Now, interact with elements in the "Remove Cash" pop-up
                    #     cashOut = self.driver.find_element(By.XPATH, "//input[@id='cashOut']")
                    #     if cashOut.is_selected():
                    #         json_amount = data['test_cashManagement']['amount']
                    #         amount = self.driver.find_element(By.XPATH, "//input[@id='amount']")
                    #         amount.send_keys(json_amount)
                    #         time.sleep(5)
                    #         json_note = data['test_cashManagement']['note']
                    #         note = self.driver.find_element(By.XPATH, "//input[@id='note']")
                    #         note.send_keys(json_note)
                    #         time.sleep(5)
                    #     else:
                    #         pettyCashOut = self.driver.find_element(By.XPATH, "//input[@id='pettyCashOut']")
                    #         if pettyCashOut.is_selected():
                    #             time.sleep(5)
                    #             json_amount = data['test_cashManagement']['amount']
                    #             amount = self.driver.find_element(By.XPATH, "//input[@id='amount']")
                    #             amount.send_keys(json_amount)
                    #             time.sleep(5)
                    #             json_note = data['test_cashManagement']['note']
                    #             note = self.driver.find_element(By.XPATH, "//input[@id='note']")
                    #             note.send_keys(json_note)
                    #             time.sleep(5)
                    #     # remove_cash_button = self.driver.find_element(By.XPATH, "//span[text()='Remove Cash']")
                    #     # remove_cash_button.click()

                    if add_cash:
                        # Click the "Add Cash" button
                        # add_cash.click()
                        # Wait for the associated pop-up to appear (you may need to adjust the wait time)
                        time.sleep(10)

                        # Now, interact with elements in the "Add Cash" pop-up
                        cashIn = self.driver.find_element(By.XPATH, "//input[@id='cashIn']")
                        if cashIn.is_selected():
                            json_amount = data['test_cashManagement']['amount']
                            amount = self.driver.find_element(By.XPATH, "//input[@id='amount']")
                            amount.send_keys(json_amount)
                            time.sleep(5)
                            json_note = data['test_cashManagement']['note']
                            note = self.driver.find_element(By.XPATH, "//input[@id='note']")
                            note.send_keys(json_note)
                            time.sleep(5)
                        else:
                            pettyCashIn = self.driver.find_element(By.XPATH, "//input[@id='pettyCashIn']")
                            if pettyCashIn.is_selected():
                                json_amount = data['test_cashManagement']['amount']
                                amount = self.driver.find_element(By.XPATH, "//input[@id='amount']")
                                amount.send_keys(json_amount)
                                time.sleep(5)
                                json_note = data['test_cashManagement']['note']
                                note = self.driver.find_element(By.XPATH, "//input[@id='note']")
                                note.send_keys(json_note)
                                time.sleep(5)

                        # add_cash_button = self.driver.find_element(By.XPATH, "//span[text()='Add Cash']")
                        # add_cash_button.click()

            @unittest.SkipTest
            def test_salesHistory(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(30)
                username = data['test_salesHistory']['username']
                password = data['test_salesHistory']['password']
                # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
                # username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
                # username_input.send_keys(username)

                # Step 5: Enter password in the password input box
                # password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
                # password_input.send_keys(password)

                # Step 6: Click on the login button
                # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
                # login_button.click()
                # Step 6: Select POS
                # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
                pos = self.driver.find_element(By.XPATH, "//h4[text()='POS']")
                if pos.is_displayed():
                    pos.click()
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
                time.sleep(20)
                # till = self.driver.find_element(By.XPATH, "//div[@class='ant-card ant-card-bordered']")
                # till.click()
                # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/open-till-component")
                # insert amount into Amount Input box
                # json_amount = data['test_salesHistory']['amount']
                # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # amount.send_keys(json_amount)

                # insert note into note input box
                # json_note = data['test_salesHistory']['note']
                # note = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # note.send_keys(json_note)

                # Click open till button
                # open_till_button = self.driver.find_element(By.XPATH, "//button[@id='step3']")
                # open_till_button.click()

                time.sleep(10)
                # menu_salesHistory = self.driver.find_element(By.XPATH, "//span[text()='Sales History']")
                # if menu_salesHistory.is_displayed():
                #     menu_salesHistory.click()
                #     time.sleep(5)
                #  Search Customer Name
                json_search_customer = data["test_salesHistory"]["search_customer"]
                search_customer = self.driver.find_element(By.XPATH, "//input[@class='ant-input ant-input-lg']")
                search_customer.send_keys(json_search_customer)
                search_customer.send_keys(Keys.RETURN)
                time.sleep(5)
                # Select Date
                current_datetime = datetime.datetime.now()
                current_date = current_datetime.date()
                formatted_date = current_date.strftime("%Y-%m-%d")
                datepicker = self.driver.find_element(By.XPATH, "//input[@placeholder='Choose date range']")
                datepicker.send_keys(formatted_date)
                # Search Document Number
                json_document_no = data["test_salesHistory"]["document_no"]
                document_no = self.driver.find_element(By.XPATH,
                                                       "//input[@class='ant-input ant-input-lg salesHistory-doc-input']")
                document_no.send_keys(json_document_no)
                # Select Right Arrow

                # right_arrow = self.driver.find_element(By.XPATH, "//span[@class='anticon anticon-right']")
                right_arrow = self.driver.find_element(By.XPATH, "//span[@role='img']")
                no_data = self.driver.find_element(By.XPATH, "//div[@class='ant-empty-description']").text
                if right_arrow.is_displayed():
                    right_arrow.click()
                    time.sleep(5)
                    print_reciept = self.driver.find_element(By.XPATH, "//p[text()='Print receipt']")
                    sales_return = self.driver.find_element(By.XPATH, "//p[text()='Sales Return']")

                    if print_reciept.is_displayed():
                        print_reciept.click()
                    else:
                        pass

                    if sales_return.is_displayed():
                        sales_return.click()
                        remove_button = self.driver.find_element(By.XPATH, "//span[text()='Remove']")
                        return_button = self.driver.find_element(By.XPATH,
                                                                 "//button[@class='ant-btn focusDashboardCard']")
                        if remove_button.is_displayed() and return_button.is_displayed():
                            time.sleep(5)
                            remove_button.click()

                        else:
                            return_button.click()

                    else:
                        pass

                else:
                    if no_data == "No Data":
                        # Go to Point of Sale Page
                        menu_point_of_sale = self.driver.find_element(By.XPATH, "//span[text()='Point of Sale']")
                        menu_point_of_sale.click()

            @unittest.SkipTest
            def test_closeTill(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(30)
                username = data['test_closeTill']['username']
                password = data['test_closeTill']['password']
                # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
                # username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
                # username_input.send_keys(username)

                # Step 5: Enter password in the password input box
                # password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
                # password_input.send_keys(password)

                # Step 6: Click on the login button
                # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
                # login_button.click()
                # Step 6: Select POS
                # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
                pos = self.driver.find_element(By.XPATH, "//h4[text()='POS']")
                if pos.is_displayed():
                    pos.click()
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
                time.sleep(20)
                # till = self.driver.find_element(By.XPATH, "//div[@class='ant-card ant-card-bordered']")
                # till.click()
                # self.assertEqual(self.driver.current_url, "https://test-pos.cwcloud.in:8412//?appId=1015&name=POS#/open-till-component")
                # insert amount into Amount Input box
                # json_amount = data['test_salesHistory']['amount']
                # amount = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # amount.send_keys(json_amount)

                # insert note into note input box
                # json_note = data['test_salesHistory']['note']
                # note = self.driver.find_element(By.XPATH, "//input[@class='ant-input transactionAmtInput']")
                # note.send_keys(json_note)

                # Click open till button
                # open_till_button = self.driver.find_element(By.XPATH, "//button[@id='step3']")
                # open_till_button.click()

                time.sleep(10)

                close_till_all = self.driver.find_element(By.XPATH, "")
                if close_till_all.is_displayed():
                    close_till_all.click()

                back_button = self.driver.find_element(By.XPATH, "")
                close_till_button = self.driver.find_element(By.XPATH, "")
                if back_button.is_displayed() and back_button.is_enabled():
                    back_button.click()

                else:
                    close_till_button.click()
                    time.sleep(10)
                    self.assertEqual(self.driver.current_url, "https://test-auth.cwcloud.in:8412/sign-in")

        # class for Store Admin test cases
        class TestStoreAdminProductsData(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def tearDown(self):
                self.driver.close()

            @unittest.SkipTest
            def test_addProducts(self):
                self.driver.maximize_window()
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(30)
                username = data['test_addProducts']['username']
                password = data['test_addProducts']['password']
                # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
                # username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
                # username_input.send_keys(username)

                # Step 5: Enter password in the password input box
                # password_input = self.driver.find_element(By.XPATH, "//input[@class=' w-full h-[40px] sm:h-[40px] px-3 py-1 border-[1px] border-[#dadada] text-[#101828] rounded placeholder:text-[#98A2B3] text-xs ff-inter font-normal outline-none']")
                # password_input.send_keys(password)

                # Step 6: Click on the login button
                # login_button = self.driver.find_element(By.XPATH, "//button[@class='flex items-center justify-center mb-2 xs:mt-[20px] sm:mt-[20px] w-full h-[50px] sm:h-[50px] px-4 py-2 text-white bg-[#91C507] text-[13px] ff-inter font-bold outline-none rounded']")
                # login_button.click()
                # Step 6: Select POS
                # pos = self.driver.find_element(By.XPATH, "//article[@class='bg-white mb-2 sm:mb-0 md:w-[180px] lg:w-[180px] sm:w-[200px] xs:w-full rounded-[12px] px-3 py-3 mr-2 sm:mr-4 justify-between relative'][1]")
                store_admin = self.driver.find_element(By.XPATH, "//h4[text()='Store Admin']")
                # Check if the element is displayed
                self.assertTrue(store_admin.is_displayed(), msg="Store Admin is not displayed")
                store_admin.click()
                time.sleep(10)

                menu_products = self.driver.find_element(By.XPATH, "//span[text()='Products']")
                self.assertTrue(menu_products.is_displayed(), msg="Products Menu is not Displayed")
                menu_products.click()

                sidebar_menu_product = self.driver.find_element(By.XPATH, "//span[text()='Product']")
                self.assertTrue(sidebar_menu_product.is_displayed(), msg="Product menu is not displayed.")
                sidebar_menu_product.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New Button is not displayed")
                add_new_button.click()
                time.sleep(10)

                product_info = data["test_addProducts"]["product_info"]
                product_name = product_info["Product Name"]
                product_category = product_info["Product Category"]
                uom = product_info["UOM"]
                tax_category = product_info["Tax Category"]
                sales_price = product_info["Sales Price"]
                list_price = product_info["List Price"]
                purchase_price = product_info["Purchase Price"]
                upc = product_info["UPC"]
                product_description = product_info["Product Description"]
                image_url = product_info["Image URL"]
                product_catalogue = product_info["Product Catalogue"]

                input_product_name = self.driver.find_element(By.ID, "headerTab_05DF4D54F56544E7BB875B7CFB935C8C")
                self.assertTrue(input_product_name.is_displayed(), msg="Product Name Input box is not displayed")
                input_product_name.clear()
                input_product_name.send_keys(product_name)
                time.sleep(5)

                input_product_category = self.driver.find_element(By.ID, "headerTab_C836ADF14C7046CAB505735A9C75A9A2")
                self.assertTrue(input_product_category.is_displayed(), msg="Product Category is not displayed.")
                input_product_category.clear()
                input_product_category.send_keys(product_category)
                time.sleep(5)

                input_uom = self.driver.find_element(By.ID, "headerTab_311BAEAB192E4CED9C6375C24E5FCB4A")
                self.assertTrue(input_uom.is_displayed(), msg="UOM is not displayed.")
                input_uom.clear()
                input_uom.send_keys(uom)
                time.sleep(5)

                input_tax_category = self.driver.find_element(By.ID, "headerTab_C4AE5CADA4AA46B583BE475719287EAF")
                self.assertTrue(input_tax_category.is_displayed(), msg="Tax Category is not displayed.")
                input_tax_category.send_keys(tax_category)
                time.sleep(5)

                input_sales_price = self.driver.find_element(By.ID, "headerTab_9401293BAC5A432F81EC52E65AEAC96E")
                self.assertTrue(input_sales_price.is_displayed(), msg="Sales Price is not displayed.")
                input_sales_price.clear()
                input_sales_price.send_keys(sales_price)
                time.sleep(5)

                input_list_price = self.driver.find_element(By.ID, "headerTab_1026DF342BBD4DA0A678C2BAC4AE2600")
                self.assertTrue(input_list_price.is_displayed(), msg="List Price is not Displayed.")
                input_list_price.send_keys(list_price)
                time.sleep(5)
                input_purchase_price = self.driver.find_element(By.ID, "headerTab_842952C5B7A94B01BE5B2B61D3EC7E36")
                self.assertTrue(input_purchase_price.is_displayed(), msg="Purchase Price is not displayed.")
                input_purchase_price.send_keys(purchase_price)
                time.sleep(5)

                input_upc = self.driver.find_element(By.ID, "headerTab_95761154135347DCBF37F158165AE03E")
                self.assertTrue(input_upc.is_displayed(), msg="UPC is not displayed.")
                input_upc.clear()
                input_upc.send_keys(upc)
                time.sleep(5)

                input_product_description = self.driver.find_element(By.ID,
                                                                     "headerTab_A367F6AC04954C6CA4076E72343253CB")
                self.assertTrue(input_product_description.is_displayed(), msg="Product Description is not displayed.")
                input_product_description.clear()
                input_product_description.send_keys(product_description)
                time.sleep(5)

                input_image_url = self.driver.find_element(By.XPATH, "//span[text()='Upload']")
                self.assertTrue(input_image_url.is_displayed(), msg="Image Upload is not displayed.")
                # input_image_url.clear()
                input_image_url.send_keys(image_url)
                time.sleep(5)

                input_product_catalogue = self.driver.find_element(By.ID, "headerTab_D3F455D32BCA4802816CC0CEFB89D64F")
                self.assertTrue(input_product_catalogue.is_displayed(), msg="Product Catalogue is not displayed.")
                input_product_catalogue.clear()
                input_product_catalogue.send_keys(product_catalogue)
                time.sleep(5)

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel button is not displayed.")
                if input_product_name is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            @unittest.SkipTest
            def test_addProductCategory(self):
                self.driver.maximize_window()
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(10)
                username = data['test_addProductCategory']['username']
                password = data['test_addProductCategory']['password']
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

                sidebar_menu_product_category = self.driver.find_element(By.XPATH, "//span[text()='Product Category']")
                self.assertTrue(sidebar_menu_product_category.is_displayed(),
                                msg="Product Category menu is not displayed.")
                sidebar_menu_product_category.click()
                time.sleep(5)

                # Add New Button
                add_new_button = self.driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                category_code = data["test_addProductCategory"]["Category Code"]
                input_category_code = self.driver.find_element(By.ID, "headerTab_DCDD6A1D18CD4FF29A65AD6CB6626080")
                self.assertTrue(input_category_code.is_displayed(), msg="Category code Input box is not displayed.")
                input_category_code.send_keys(category_code)
                time.sleep(5)

                category_name = data["test_addProductCategory"]["Category Name"]
                input_category_name = self.driver.find_element(By.ID, "headerTab_09862BBB54134EA88CD96A1120BA7470")
                self.assertTrue(input_category_name.is_displayed(), msg="Category Name input box is not displayed.")
                input_category_name.send_keys(category_name)
                time.sleep(5)

                parent_category = data["test_addProductCategory"]["Parent Category"]
                input_parent_category = self.driver.find_element(By.ID, "headerTab_864BED62888C409B91883A2C59AE6EE3")
                self.assertTrue(input_parent_category.is_displayed(), msg="Parent Category input is not displayed.")
                input_parent_category.send_keys(parent_category)
                time.sleep(5)

                category_description = data["test_addProductCategory"]["Category Description"]
                input_category_description = self.driver.find_element(By.ID,
                                                                      "headerTab_1F2F4DC8A00343CC9791790D57E1B087")
                self.assertTrue(input_category_description.is_displayed(),
                                msg="Category Description input box is not displayed.")
                input_category_description.send_keys(category_description)
                time.sleep(5)

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not displayed")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if category_code and category_name is not None:
                    save_button.click()
                    time.sleep(5)
                else:
                    cancel_button.click()
                    time.sleep(5)

            @unittest.SkipTest
            def test_addProductCatalogue(self):
                self.driver.maximize_window()
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(30)
                username = data['test_addProductCatalogue']['username']
                password = data['test_addProductCatalogue']['password']
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

                sidebar_menu_product_catalogue = self.driver.find_element(By.XPATH,
                                                                          "//span[text()='Product Catalogue']")
                self.assertTrue(sidebar_menu_product_catalogue.is_displayed(),
                                msg="Product Catalogue menu is not displayed.")
                sidebar_menu_product_catalogue.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                product_catalogue = data['test_addProductCatalogue']['Product Catalogue Name']
                input_product_catalogue = self.driver.find_element(By.ID, "headerTab_02C771DA4EAC43B1B4DFA1B26CDB05A7")
                self.assertTrue(input_product_catalogue.is_displayed(),
                                msg="Product Catalogue input box is not displayed.")
                input_product_catalogue.send_keys(product_catalogue)
                time.sleep(5)

                active_checkbox = self.driver.find_element(By.ID, "headerTab_339E009F5745408FB2ADF8C83E05373D")
                self.assertTrue(active_checkbox.is_selected(), msg="Active Check box is not Selected.")
                if not active_checkbox.is_selected():
                    # If it's not selected, select the checkbox
                    active_checkbox.click()

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_product_catalogue is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            @unittest.SkipTest
            def test_addBrand(self):
                self.driver.maximize_window()
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(30)
                username = data['test_addBrand']['username']
                password = data['test_addBrand']['password']
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

                sidebar_menu_brand = self.driver.find_element(By.XPATH,
                                                              "//span[text()='Brand']")
                self.assertTrue(sidebar_menu_brand.is_displayed(),
                                msg="Brand menu is not displayed.")
                sidebar_menu_brand.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                brand_name = data["test_addBrand"]["Brand Name"]
                input_brand_name = self.driver.find_element(By.ID, "headerTab_406034723F6E4DC4BC8352D364E3A188")
                self.assertTrue(input_brand_name.is_displayed(), msg="Brand Name input box is not displayed.")
                input_brand_name.send_keys(brand_name)
                time.sleep(5)

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_brand_name is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            @unittest.SkipTest
            def test_addImageLibrary(self):
                self.driver.maximize_window()
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(30)
                username = data['test_addImageLibrary']['username']
                password = data['test_addImageLibrary']['password']
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

                sidebar_menu_image_library = self.driver.find_element(By.XPATH,
                                                                      "//span[text()='Image Library']")
                self.assertTrue(sidebar_menu_image_library.is_displayed(),
                                msg="Image Library menu is not displayed.")
                sidebar_menu_image_library.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                image_name = data["test_addImageLibrary"]["Image"]
                input_image_name = self.driver.find_element(By.ID, "")
                self.assertTrue(input_image_name.is_displayed(), msg="Image Name input box is not displayed.")
                input_image_name.send_keys(image_name)
                time.sleep(5)

                description = data["test_addImageLibrary"]["Description"]
                input_description = self.driver.find_element(By.ID, "headerTab_9D891ED6164E4CEDBEA4B3A8C078FFD6")
                self.assertTrue(input_description.is_displayed(), msg="Description input box is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                image_group = data["test_addImageLibrary"]["Image Group"]
                input_image_group = self.driver.find_element(By.ID, "headerTab_E7E96A631EE44F3FB601A462F70B2AD3")
                self.assertTrue(input_image_group.is_displayed(), msg="Image Group Combo box is not displayed.")
                input_image_group.send_keys(image_group)
                time.sleep(5)

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_image_name and input_description and input_image_group is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            @unittest.SkipTest
            def test_addRFIDTag(self):
                self.driver.maximize_window()
                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addRFIDTag']['username']
                password = data['test_addRFIDTag']['password']
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

                product_code = data["test_addRFIDTag"]["Product Code"]
                input_product_code = self.driver.find_element(By.ID, "headerTab_6BEBA63D3D014D9CBF0C74F7E5D0FDC9")
                self.assertTrue(input_product_code.is_displayed(), msg="Product Code input is not displayed.")
                input_product_code.send_keys(product_code)
                time.sleep(5)

                product = data["test_addRFIDTag"]["Product"]
                input_product = self.driver.find_element(By.ID, "headerTab_B456D14F3DC54EFE8378FFE88597149A")
                self.assertTrue(input_product.is_displayed(), msg="Product Input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                tag_value = data["test_addRFIDTag"]["Tag Value"]
                input_tag_value = self.driver.find_element(By.ID, "headerTab_C048011FA52F409DB461EAE659DD004F")
                self.assertTrue(input_tag_value.is_displayed(), msg="Tag Value Input is not displayed.")
                input_tag_value.send_keys(tag_value)
                time.sleep(5)

                tag_type = data["test_addRFIDTag"]["Tag Type"]
                input_tag_type = self.driver.find_element(By.ID, "headerTab_9E89133760594284B76F9A044408EC10")
                self.assertTrue(input_tag_type.is_displayed(), msg="Tag Type input is not displayed.")
                input_tag_type.send_keys(tag_type)
                time.sleep(5)

                tagging_date = data["test_addRFIDTag"]["Tagging Date"]
                input_tagging_date = self.driver.find_element(By.ID, "headerTab_B70961444E0A45938756807DDCE4E883")
                self.assertTrue(input_tagging_date.is_displayed(), msg="Tagging Date input is not displayed.")
                input_tagging_date.send_keys(tagging_date)
                time.sleep(5)

                batch_number = data["test_addRFIDTag"]["Batch Number"]
                input_batch_number = self.driver.find_element(By.ID, "headerTab_3676DE90C3D542D0A0E69F906666B0FC")
                self.assertTrue(input_batch_number.is_displayed(), msg="Batch Number input box is not displayed.")
                input_batch_number.send_keys(batch_number)
                time.sleep(5)

                batch = data["test_addRFIDTag"]["Batch"]
                input_batch = self.driver.find_element(By.ID, "headerTab_34531C4CC21A41CCB107FDCCE8A4020E")
                self.assertTrue(input_batch.is_displayed(), msg="Batch input is not displayed.")
                input_batch.send_keys(batch)
                time.sleep(5)

                location = data["test_addRFIDTag"]["Location"]
                input_location = self.driver.find_element(By.ID, "headerTab_79D49C5DBFB34C898BC5479E73A09BFF")
                self.assertTrue(input_location.is_displayed(), msg="Location input is not displayed.")
                input_location.send_keys(location)
                time.sleep(5)

                tag_status = data["test_addRFIDTag"]["Tag Status"]
                input_tag_status = self.driver.find_element(By.ID, "headerTab_A4335C2B76D94CE5BEAAC5814AF3401F")
                self.assertTrue(input_tag_status.is_displayed(), msg="Tag Status input is not displayed.")
                input_tag_status.send_keys(tag_status)
                time.sleep(5)

                last_scanned_date = data["test_addRFIDTag"]["Last Scanned Date"]
                input_last_scanned_date = self.driver.find_element(By.ID, "headerTab_8D866234F3374BC3A8CF3CBF360C3239")
                self.assertTrue(input_last_scanned_date.is_displayed(), msg="Last Scanned Date input is not displayed.")
                input_last_scanned_date.send_keys(last_scanned_date)
                time.sleep(5)

                scanned_by = data["test_addRFIDTag"]["Scanned By"]
                input_scanned_by = self.driver.find_element(By.ID, "headerTab_7273A3F525634450B1703500ED870758")
                self.assertTrue(input_scanned_by.is_displayed(), msg="Scanned By input is not displayed.")
                input_scanned_by.send_keys(scanned_by)
                time.sleep(5)

                expiry_date = data["test_addRFIDTag"]["Expiry Date"]
                input_expiry_date = self.driver.find_element(By.ID, "headerTab_1288173DC4FC43FFA40D5638DB6DAA67")
                self.assertTrue(input_expiry_date.is_displayed(), msg="Expiry Date input is not displayed.")
                input_expiry_date.send_keys(expiry_date)
                time.sleep(5)

                custom_attributes = data["test_addRFIDTag"]["Custom Attributes"]
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

        # class for Store Admin test cases
        class TestStoreAdminSalesData(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def tearDown(self):
                self.driver.close()

            @unittest.SkipTest
            def test_posOrders(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_posOrders']['username']
                password = data['test_posOrders']['password']
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

                menu_sales = self.driver.find_element(By.XPATH, "//span[text()='Sales']")
                self.assertTrue(menu_sales.is_displayed(), msg="Sales Menu is not Displayed")
                menu_sales.click()
                time.sleep(5)

                sidebar_menu_pos_orders = self.driver.find_element(By.XPATH,
                                                                   "//span[text()='POS Orders']")
                self.assertTrue(sidebar_menu_pos_orders.is_displayed(),
                                msg="Pos Orders menu is not displayed.")
                sidebar_menu_pos_orders.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                store = data["test_posOrders"]["Store"]
                input_store = self.driver.find_element(By.ID, "headerTab_4364D3A8153E4B5A96EFBAAFA884A257")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                sale_type = data["test_posOrders"]["Sale Type"]
                input_sale_type = self.driver.find_element(By.ID, "headerTab_4870F8FD52FD491E91D23A51E47C835D")
                self.assertTrue(input_sale_type.is_displayed(), msg="Sale Type input is not displayed.")
                input_sale_type.send_keys(sale_type)
                time.sleep(5)

                document_type = data["test_posOrders"]["Document Type"]
                input_document_type = self.driver.find_element(By.ID, "headerTab_F099D992F66C4328840B015336C388D9")
                self.assertTrue(input_document_type.is_displayed(), msg="Document Type input is not displayed.")
                input_document_type.send_keys(document_type)
                time.sleep(5)

                document_no = data["test_posOrders"]["Document No"]
                input_document_no = self.driver.find_element(By.ID, "headerTab_514DB285761544BFB842D31AD90490D5")
                self.assertTrue(input_document_no.is_displayed(), msg="Document Number input is not displayed")
                input_document_no.send_keys(document_no)
                time.sleep(5)

                order_date = data["test_posOrders"]["Order Date"]
                input_order_date = self.driver.find_element(By.ID, "headerTab_A999CD069E704FB889A7348DEEC20AE2")
                self.assertTrue(input_order_date.is_displayed(), msg="Order date input is not displayed.")
                input_sale_type.send_keys(order_date)
                time.sleep(5)

                order_time = data["test_posOrders"]["Order Time"]
                input_order_time = self.driver.find_element(By.ID, "headerTab_474B0303FE73478194D0FA96E9487BDF")
                self.assertTrue(input_order_time.is_displayed(), msg="Order Time input is not displayed.")
                input_order_time.send_keys(order_time)
                time.sleep(5)

                b2c_customer = data["test_posOrders"]["B2C Customer"]
                input_b2c_customer = self.driver.find_element(By.ID, "headerTab_C1889B9E3ECB4A6ABE088526465CBB28")
                self.assertTrue(input_b2c_customer.is_displayed(), msg="B2C Customer input is not displayed.")
                input_b2c_customer.send_keys(b2c_customer)
                time.sleep(5)

                price_list = data["test_posOrders"]["Price_List"]
                input_price_list = self.driver.find_element(By.ID, "headerTab_E01845685600402097E7D7E582706F1A")
                self.assertTrue(input_price_list.is_displayed(), msg="Price List input is not displayed.")
                input_price_list.send_keys(price_list)
                time.sleep(5)

                payment_method = data["test_posOrders"]["Payment Method"]
                input_payment_method = self.driver.find_element(By.ID, "headerTab_578D3AF8FDB6424EA807B1375619ADF8")
                self.assertTrue(input_payment_method.is_displayed(), msg="Payment Method input is not displayed.")
                input_payment_method.send_keys(payment_method)
                time.sleep(5)

                sales_rep = data["test_posOrders"]["Sales Rep"]
                input_sales_rep = self.driver.find_element(By.ID, "headerTab_B22065C7EB1E4AFF8FFA6FA6EB3797DC")
                self.assertTrue(input_sales_rep.is_displayed(), msg="Sales Rep input is not displayed.")
                input_sales_rep.send_keys(sales_rep)
                time.sleep(5)

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_store and input_document_type and input_document_no and input_order_date and input_price_list is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            @unittest.SkipTest
            def test_customers(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_customers']['username']
                password = data['test_customers']['password']
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

                registered_store = data["test_customers"]["Registered Store"]
                input_registered_store = self.driver.find_element(By.ID, "headerTab_2353CF69FBB94A8C8C2F9C55F785B8CF")
                self.assertTrue(input_registered_store.is_displayed(), msg="Registered Store input is not displayed.")
                input_registered_store.send_keys(registered_store)
                time.sleep(5)

                active_check = self.driver.find_element(By.ID, "headerTab_3BAFE2386E9947CAA5875571B42DE999")
                if active_check.is_selected():
                    pass
                else:
                    active_check.click()

                firstname = data["test_customers"]["First Name"]
                input_firstname = self.driver.find_element(By.ID, "headerTab_1B540617B4374162BCCE219EF7D15365")
                self.assertTrue(input_firstname.is_displayed(), msg="First Name input is not displayed.")
                input_firstname.send_keys(firstname)
                time.sleep(5)

                name = data["test_customers"]["Name"]
                input_name = self.driver.find_element(By.ID, "headerTab_3510E858B362493EBE47062864E0001B")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                lastname = data["test_customers"]["Last Name"]
                input_lastname = self.driver.find_element(By.ID, "headerTab_F73EDEEFC2454F2D98AAB99219032244")
                self.assertTrue(input_lastname.is_displayed(), msg="Last Name input is not displayed.")
                input_lastname.send_keys(lastname)
                time.sleep(5)

                mobile = data["test_customers"]["Mobile No"]
                input_mobile = self.driver.find_element(By.ID, "headerTab_90DDABD2BFD1446B8B6142A3D88D5728")
                self.assertTrue(input_mobile.is_displayed(), msg="Mobile input is not displayed.")
                input_mobile.send_keys(mobile)
                time.sleep(5)

                country_code = data["test_customers"]["Country Code"]
                input_country_code = self.driver.find_element(By.ID, "headerTab_4D66FA76BD134195B307D7BF15B530BA")
                self.assertTrue(input_country_code.is_displayed(), msg="Country Code input is not displayed.")
                input_country_code.send_keys(country_code)
                time.sleep(5)

                email = data["test_customers"]["Email"]
                input_email = self.driver.find_element(By.ID, "headerTab_8B96C59CACE54500AB145D9DCC5F3107")
                self.assertTrue(input_email.is_displayed(), msg="Email input is not displayed.")
                input_email.send_keys(email)
                time.sleep(5)

                pincode = data["test_customers"]["Pincode"]
                input_pincode = self.driver.find_element(By.ID, "headerTab_4C336FDDC5FE4C2694B10943C144A312")
                self.assertTrue(input_pincode.is_displayed(), msg="Pincode input is not displayed.")
                input_pincode.send_keys(pincode)
                time.sleep(5)

                default_customer = data["test_customers"]["Default Customer"]
                input_default_customer = self.driver.find_element(By.ID, "headerTab_883F14CAFEF041AFB0F51E88A76F42F1")
                self.assertTrue(input_default_customer.is_displayed(), msg="Default Customer input is not displayed.")
                input_default_customer.send_keys(default_customer)
                time.sleep(5)

                credit_limit = data["test_customers"]["Credit Limit"]
                input_credit_limit = self.driver.find_element(By.ID, "headerTab_B8CFAF37257D4E90A726318ACD695F16")
                self.assertTrue(input_credit_limit.is_displayed(), msg="Credit Limit input is not displayed.")
                input_credit_limit.send_keys(credit_limit)
                time.sleep(5)

                payment_method = data["test_customers"]["Payment Method"]
                input_payment_method = self.driver.find_element(By.ID, "headerTab_CDBFB8C224F4448BB6595CA41DA0FDE9")
                self.assertTrue(input_payment_method.is_displayed(), msg="Payment Method input is not displayed.")
                input_payment_method.send_keys(payment_method)
                time.sleep(5)

                loyalty_level = data["test_customers"]["Loyalty Level"]
                input_loyalty_level = self.driver.find_element(By.ID, "headerTab_F7AE3393AA5B4A5B8C81A3086846F393")
                self.assertTrue(input_loyalty_level.is_displayed(), msg="Loyalty Level input is not displayed.")
                input_loyalty_level.send_keys(loyalty_level)
                time.sleep(5)

                loyalty_balance = data["test_customers"]["Loyalty Balance"]
                input_loyalty_balance = self.driver.find_element(By.ID, "headerTab_4489B4824A1C4F6F9682A063E332511D")
                self.assertTrue(input_loyalty_balance.is_displayed(), msg="Loyalty balance input is not displayed.")
                input_loyalty_balance.send_keys(loyalty_balance)
                time.sleep(5)

                last_visit_date = data["test_customers"]["Last Visit Date"]
                input_last_visit_date = self.driver.find_element(By.ID, "headerTab_A0CC26764EEC4045AC22FEA60F7E99F4")
                self.assertTrue(input_last_visit_date.is_displayed(), msg="Last Visit Date input is not displayed.")
                input_last_visit_date.send_keys(last_visit_date)
                time.sleep(5)

                last_billing_amount = data["test_customers"]["Last Billing Amount"]
                input_last_billing_amount = self.driver.find_element(By.ID,
                                                                     "headerTab_E36A6F84E8974643B783EAC340FE89F8")
                self.assertTrue(input_last_billing_amount.is_displayed(),
                                msg="Last Billing Amount input is not displayed.")
                input_last_billing_amount.send_keys(last_billing_amount)
                time.sleep(5)

                average_basket_value = data["test_customers"]["Average Basket Value"]
                input_average_basket_value = self.driver.find_element(By.ID,
                                                                      "headerTab_EC71BA75384B471981B11D3CBB9773A3")
                self.assertTrue(input_average_basket_value.is_displayed(),
                                msg="Average Basket value input is not displayed.")
                input_average_basket_value.send_keys(average_basket_value)
                time.sleep(5)

                no_of_visits = data["test_customers"]["No of Visits"]
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

        # class for Store Admin test cases
        class TestStoreAdminPurchaseData(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def tearDown(self):
                self.driver.close()

            def test_addsupplier(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addsupplier']['username']
                password = data['test_addsupplier']['password']
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

                business_unit = data["test_addsupplier"]["Business Unit"]
                input_business_unit = self.driver.find_element(By.ID, "headerTab_765FDEFCD5524686A3E1EBAB8E898740")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                supplier_code = data["test_addsupplier"]["Supplier Code"]
                input_supplier_code = self.driver.find_element(By.ID, "headerTab_52957BB4CB314F78B240E4D3856E8F2A")
                self.assertTrue(input_supplier_code.is_displayed(), msg="Supplier Code input is not displayed.")
                input_supplier_code.send_keys(supplier_code)
                time.sleep(5)

                name = data["test_addsupplier"]["Name"]
                input_name = self.driver.find_element(By.ID, "headerTab_98DC62FB03F84DDD947683A67A3DE902")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                supplier_category = data["test_addsupplier"]["Supplier Category"]
                input_supplier_category = self.driver.find_element(By.ID, "headerTab_98DC62FB03F84DDD947683A67A3DE902")
                self.assertTrue(input_supplier_category.is_displayed(), msg="Supplier Category input is not displayed.")
                input_supplier_category.send_keys(supplier_category)
                time.sleep(5)

                price_list = data["test_addsupplier"]["Price List"]
                input_price_list = self.driver.find_element(By.ID, "headerTab_1D6ABCCC41D341E08855D7CDC28B2EA6")
                self.assertTrue(input_price_list.is_displayed(), msg="Price List input is not displayed.")
                input_price_list.send_keys(price_list)
                time.sleep(5)

                description = data["test_addsupplier"]["Description"]
                input_description = self.driver.find_element(By.ID, "headerTab_80E0A44C5C9E4A94B0F9F31060F00991")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                reference_no = data["test_addsupplier"]["Reference_no"]
                input_reference_no = self.driver.find_element(By.ID, "headerTab_43B906199766449EB67B0FC39B87B44A")
                self.assertTrue(input_reference_no.is_displayed(), msg="Reference_no input is not displayed.")
                input_reference_no.send_keys(reference_no)
                time.sleep(5)

                gst_no = data["test_addsupplier"]["GST_No"]
                input_gst_no = self.driver.find_element(By.ID, "headerTab_20F2AD84DFB14D96AB7B5C08355211BB")
                self.assertTrue(input_gst_no.is_displayed(), msg="GST_no input is not displayed.")
                input_gst_no.send_keys(gst_no)
                time.sleep(5)

                payment_method = data["test_addsupplier"]["Payment_Method"]
                input_payment_method = self.driver.find_element(By.ID, "headerTab_BE13C5AE33A9486A81373A20DB06D7A4")
                self.assertTrue(input_payment_method.is_displayed(), msg="Payment Method input is not displayed.")
                input_payment_method.send_keys(payment_method)
                time.sleep(5)

                local_purchase_check = self.driver.find_element(By.ID, "headerTab_61A9AB12CEFE4DBEA8F3D5B3E694311E")
                if local_purchase_check.is_selected():
                    pass
                else:
                    local_purchase_check.click()

                payment_terms = data["test_addsupplier"]["Payment_Terms"]
                input_payment_terms = self.driver.find_element(By.ID, "headerTab_A317B4ECAA2A45E5AE240F70C031A8A9")
                self.assertTrue(input_payment_terms.is_displayed(), msg="Payment Terms input is not displayed.")
                input_payment_terms.send_keys(payment_terms)
                time.sleep(5)

                currency = data["test_addsupplier"]["Currency"]
                input_currency = self.driver.find_element(By.ID, "headerTab_9DA9E495F62F41959BE77685B5EB2B2C")
                self.assertTrue(input_currency.is_displayed(), msg="Currency input is not displayed.")
                input_currency.send_keys(currency)
                time.sleep(5)

                lead_days = data["test_addsupplier"]["Lead_Days"]
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

            def test_purchase_order(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_purchase_order']['username']
                # username_input = self.driver.find_element(By.XPATH, "//input[@class='mb-4 w-full h-[40px] sm:h-[40px] rounded px-3 py-1 text-[#101828] placeholder:text-[#98A2B3] border-[0.5px] border-[#DaDaDa] text-xs ff-inter font-normal outline-none']")
                username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']")
                self.assertTrue(username_input.is_displayed(), msg="Username input box is not displayed.")
                username_input.send_keys(username)
                time.sleep(5)

                # Step 5: Enter password in the password input box
                password = data['test_purchase_order']['password']
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

                business_unit = data["test_purchase_order"]["Business_Unit"]
                input_business_unit = self.driver.find_element(By.ID, "headerTab_40D1EE8DA564487D9373AD3DBF21F5C4")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                date = data["test_purchase_order"]["Date"]
                input_date = self.driver.find_element(By.ID, "headerTab_14784A1CE0E74C65947CF72C73F0CC84")
                self.assertTrue(input_date.is_displayed(), msg="Date input is not displayed.")
                input_date.send_keys(date)
                time.sleep(5)

                supplier = data["test_purchase_order"]["Supplier"]
                input_supplier = self.driver.find_element(By.ID, "headerTab_9B8D684D9D6340BDB1C1665FDEF9D810")
                self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
                input_supplier.send_keys(supplier)
                time.sleep(5)

                supplier_address = data["test_purchase_order"]["Supplier_Address"]
                input_supplier_address = self.driver.find_element(By.ID, "headerTab_C52D2B62DA794C1480228699BC39D009")
                self.assertTrue(input_supplier_address.is_displayed(), msg="Supplier Address input is not displayed.")
                input_supplier_address.send_keys(supplier_address)
                time.sleep(5)

                delivery_location = data["test_purchase_order"]["Delivery_Location"]
                input_delivery_location = self.driver.find_element(By.ID, "headerTab_03BA9FF390A448D98467057400A508A2")
                self.assertTrue(input_delivery_location.is_displayed(), msg="Delivery Location input is not displayed.")
                input_delivery_location.send_keys(delivery_location)
                time.sleep(5)

                storage_location = data["test_purchase_order"]["Storage_Location"]
                input_storage_location = self.driver.find_element(By.ID, "headerTab_F4C464FF229D4F799C28238DA9E4B525")
                self.assertTrue(input_storage_location.is_displayed(), msg="Storage Location input is not displayed.")
                input_storage_location.send_keys(storage_location)
                time.sleep(5)

                payment_terms = data["test_purchase_order"]["Payment_Terms"]
                input_payment_terms = self.driver.find_element(By.ID, "headerTab_48DFDB66892741B3A8AE4D361454F43F")
                self.assertTrue(input_payment_terms.is_displayed(), msg="Payment Terms input is not displayed.")
                input_payment_terms.send_keys(payment_terms)
                time.sleep(5)

                price_list = data["test_purchase_order"]["Price_List"]
                input_price_list = self.driver.find_element(By.ID, "headerTab_2466B04BCED24C04AE6FE5EF5FAD5FE4")
                self.assertTrue(input_price_list.is_displayed(), msg="Price List input is not displayed.")
                input_price_list.send_keys(price_list)
                time.sleep(5)

                supplier_reference = data["test_purchase_order"]["Supplier_reference"]
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

        # class for Store Admin test cases
        class TestStoreAdminInventoryData(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def tearDown(self):
                self.driver.close()

            def test_quick_goods_receipt(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_quick_goods_receipt']['username']
                password = data['test_quick_goods_receipt']['password']
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

                sidebar_menu_quick_goods_receipt = self.driver.find_element(By.XPATH,
                                                                            "//span[text()='Quick Goods Receipt']")
                self.assertTrue(sidebar_menu_quick_goods_receipt.is_displayed(),
                                msg="Quick Goods Receipt menu is not displayed.")
                sidebar_menu_quick_goods_receipt.click()
                time.sleep(5)

                business_unit = data["test_quick_goods_receipt"]["Business_Unit"]
                input_business_unit = self.driver.find_element(By.ID, "businessunit")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                supplier = data["test_quick_goods_receipt"]["Supplier"]
                input_supplier = self.driver.find_element(By.ID, "supplier")
                self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
                input_supplier.send_keys(supplier)
                time.sleep(5)

                purchase_order = data["test_quick_goods_receipt"]["Purchase_order"]
                input_purchase_order = self.driver.find_element(By.ID, "po")
                self.assertTrue(input_purchase_order.is_displayed(), msg="Purchase Order input is not displayed.")
                input_purchase_order.send_keys(purchase_order)
                time.sleep(5)

                supplier_invoice_no = data["test_quick_goods_receipt"]["Supplier_invoice_no"]
                input_supplier_invoice_no = self.driver.find_element(By.ID, "po")
                self.assertTrue(input_supplier_invoice_no.is_displayed(),
                                msg="Supplier Invoice No input is not displayed.")
                input_supplier_invoice_no.send_keys(supplier_invoice_no)
                time.sleep(5)

                remarks = data["test_quick_goods_receipt"]["Remarks"]
                input_remarks = self.driver.find_element(By.ID, "remarks")
                self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
                input_remarks.send_keys(remarks)
                time.sleep(5)

                date = data["test_quick_goods_receipt"]["Date"]
                input_date = self.driver.find_element(By.ID, "date")
                self.assertTrue(input_date.is_displayed(), msg="Date input is not displayed.")
                input_date.send_keys(date)
                time.sleep(5)

                fetch_button = self.driver.find_element(By.ID, "step7")
                self.assertTrue(fetch_button.is_displayed(), msg="Fetch Button is not displayed.")
                if input_business_unit and input_supplier and input_supplier_invoice_no and input_date and input_purchase_order is not None:
                    fetch_button.click()

            def test_quick_stock_count(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_quick_stock_count']['username']
                password = data['test_quick_stock_count']['password']
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

                business_unit = data["test_quick_stock_count"]["Business_Unit"]
                input_business_unit = self.driver.find_element(By.ID, "businessunit")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                type = data["test_quick_stock_count"]["Type"]
                input_type = self.driver.find_element(By.ID, "ctype")
                self.assertTrue(input_type.is_displayed(), msg="Type input is not displayed.")
                input_type.send_keys(type)
                time.sleep(5)

                remarks = data["test_quick_stock_count"]["Remarks"]
                input_remarks = self.driver.find_element(By.ID, "remarks")
                self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
                input_remarks.send_keys(remarks)
                time.sleep(5)

                date = data["test_quick_stock_count"]["Date"]
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

            def test_quick_wastage_entry(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_quick_wastage_entry']['username']
                password = data['test_quick_wastage_entry']['password']
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

                sidebar_menu_quick_wastage_entry = self.driver.find_element(By.XPATH,
                                                                            "//span[text()='Quick Wastage Entry']")
                self.assertTrue(sidebar_menu_quick_wastage_entry.is_displayed(),
                                msg="Quick Wastage Entry menu is not displayed.")
                sidebar_menu_quick_wastage_entry.click()
                time.sleep(5)

                business_unit = data["test_quick_wastage_entry"]["Business_Unit"]
                input_business_unit = self.driver.find_element(By.ID, "businessunit")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                wastage_type = data["test_quick_wastage_entry"]["Wastage_Type"]
                input_wastage_type = self.driver.find_element(By.ID, "wastageType")
                self.assertTrue(input_wastage_type.is_displayed(), msg="Wastage Type input is not displayed.")
                input_wastage_type.send_keys(wastage_type)
                time.sleep(5)

                remarks = data["test_quick_wastage_entry"]["Remarks"]
                input_remarks = self.driver.find_element(By.ID, "remarks")
                self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
                input_remarks.send_keys(remarks)
                time.sleep(5)

                date = data["test_quick_wastage_entry"]["Date"]
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

            def test_quick_stock_issue(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_quick_stock_issue']['username']
                password = data['test_quick_stock_issue']['password']
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

                sidebar_menu_quick_stock_issue = self.driver.find_element(By.XPATH,
                                                                          "//span[text()='Quick Stock Issue']")
                self.assertTrue(sidebar_menu_quick_stock_issue.is_displayed(),
                                msg="Quick Stock Issue menu is not displayed.")
                sidebar_menu_quick_stock_issue.click()
                time.sleep(5)

                source = data["test_quick_stock_issue"]["Source"]
                input_source = self.driver.find_element(By.ID, "source")
                self.assertTrue(input_source.is_displayed(), msg="Source input is not displayed.")
                input_source.send_keys(source)
                time.sleep(5)

                destination = data["test_quick_stock_issue"]["Destination"]
                input_destination = self.driver.find_element(By.ID, "destination")
                self.assertTrue(input_destination.is_displayed(), msg="Destination input is not displayed.")
                input_destination.send_keys(destination)
                time.sleep(5)

                stock_request = data["test_quick_stock_issue"]["Stock_Request"]
                input_stock_request = self.driver.find_element(By.ID, "po")
                self.assertTrue(input_stock_request.is_displayed(), msg="Stock Request input is not displayed.")
                input_stock_request.send_keys(stock_request)
                time.sleep(5)

                remarks = data["test_quick_stock_issue"]["Remarks"]
                input_remarks = self.driver.find_element(By.ID, "remarks")
                self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
                input_remarks.send_keys(remarks)
                time.sleep(5)

                date = data["test_quick_stock_issue"]["Date"]
                input_date = self.driver.find_element(By.ID, "date")
                self.assertTrue(input_date.is_displayed(), msg="Date input is not displayed.")
                input_date.send_keys(date)
                time.sleep(5)

                fetch_button = self.driver.find_element(By.ID, "step6")
                self.assertTrue(fetch_button.is_displayed(), msg="Fetch Button is not displayed.")
                if input_source and input_destination and input_stock_request and input_remarks and input_date is not None:
                    fetch_button.click()

            def test_quick_stock_receipt(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_quick_stock_receipt']['username']
                password = data['test_quick_stock_receipt']['password']
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

                sidebar_menu_quick_stock_receipt = self.driver.find_element(By.XPATH,
                                                                            "//span[text()='Quick Stock Issue']")
                self.assertTrue(sidebar_menu_quick_stock_receipt.is_displayed(),
                                msg="Quick Stock Receipt menu is not displayed.")
                sidebar_menu_quick_stock_receipt.click()
                time.sleep(5)

                source = data["test_quick_stock_receipt"]["Source"]
                input_source = self.driver.find_element(By.ID, "source")
                self.assertTrue(input_source.is_displayed(), msg="Source input is not displayed.")
                input_source.send_keys(source)
                time.sleep(5)

                destination = data["test_quick_stock_receipt"]["Destination"]
                input_destination = self.driver.find_element(By.ID, "destination")
                self.assertTrue(input_destination.is_displayed(), msg="Destination input is not displayed.")
                input_destination.send_keys(destination)
                time.sleep(5)

                stock_issue = data["test_quick_stock_receipt"]["Stock_Issue"]
                input_stock_issue = self.driver.find_element(By.ID, "stockIssue")
                self.assertTrue(input_stock_issue.is_displayed(), msg="Stock Request input is not displayed.")
                input_stock_issue.send_keys(stock_issue)
                time.sleep(5)

                remarks = data["test_quick_stock_receipt"]["Remarks"]
                input_remarks = self.driver.find_element(By.ID, "remarks")
                self.assertTrue(input_remarks.is_displayed(), msg="Remarks input is not displayed.")
                input_remarks.send_keys(remarks)
                time.sleep(5)

                date = data["test_quick_stock_receipt"]["Date"]
                input_date = self.driver.find_element(By.ID, "date")
                self.assertTrue(input_date.is_displayed(), msg="Date input is not displayed.")
                input_date.send_keys(date)
                time.sleep(5)

                fetch_button = self.driver.find_element(By.ID, "step6")
                self.assertTrue(fetch_button.is_displayed(), msg="Fetch Button is not displayed.")
                if input_source and input_destination and input_stock_issue and input_remarks and input_date is not None:
                    fetch_button.click()

        # class for Store Admin test cases
        class TestStoreAdminReportsData(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def tearDown(self):
                self.driver.close()

            def test_Sales_by_Product_Report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_Sales_by_Product_Report']['username']
                password = data['test_Sales_by_Product_Report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_sales_by_product_report = self.driver.find_element(By.XPATH,
                                                                                "//span[text()='Sales By Product Report']")
                self.assertTrue(sidebar_menu_sales_by_product_report.is_displayed(),
                                msg="Sales By Product Report menu is not displayed.")
                sidebar_menu_sales_by_product_report.click()
                time.sleep(5)

                store = data['test_Sales_by_Product_Report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                product = data['test_Sales_by_Product_Report']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store and input_product is not None:
                    run_button.click()

            def test_Sales_by_Product_Category(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_Sales_by_Product_Category']['username']
                password = data['test_Sales_by_Product_Category']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_sales_by_product_category = self.driver.find_element(By.XPATH,
                                                                                  "//span[text()='Sales by Product Category Report']")
                self.assertTrue(sidebar_menu_sales_by_product_category.is_displayed(),
                                msg="Sales By Product Category menu is not displayed.")
                sidebar_menu_sales_by_product_category.click()
                time.sleep(5)

                store = data['test_Sales_by_Product_Report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                product_category = data['test_Sales_by_Product_Report']['Product_Category']
                input_product_category = self.driver.find_element(By.ID, "m_product_category_id")
                self.assertTrue(input_product_category.is_displayed(), msg="Product Category input is not displayed.")
                input_product_category.send_keys(product_category)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store and input_product_category is not None:
                    run_button.click()

            def test_Sales_by_Customer_Report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_Sales_by_Customer_Report']['username']
                password = data['test_Sales_by_Customer_Report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_sales_by_customer_report = self.driver.find_element(By.XPATH,
                                                                                 "//span[text()='Sales by Customer Report']")
                self.assertTrue(sidebar_menu_sales_by_customer_report.is_displayed(),
                                msg="Sales By Customer Report menu is not displayed.")
                sidebar_menu_sales_by_customer_report.click()
                time.sleep(5)

                store = data['test_Sales_by_Customer_Report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                customer = data['test_Sales_by_Customer_Report']['Customer']
                input_customer = self.driver.find_element(By.ID, "b2c_customer_id")
                self.assertTrue(input_customer.is_displayed(), msg="Customer input is not displayed.")
                input_customer.send_keys(customer)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store and input_customer is not None:
                    run_button.click()

            def test_Sales_By_Payment_Mode_Report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_Sales_By_Payment_Mode_Report']['username']
                password = data['test_Sales_By_Payment_Mode_Report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_sales_by_payment_mode_report = self.driver.find_element(By.XPATH,
                                                                                     "//span[text()='Sales By Payment Mode Report']")
                self.assertTrue(sidebar_menu_sales_by_payment_mode_report.is_displayed(),
                                msg="Sales By Payment Mode Report menu is not displayed.")
                sidebar_menu_sales_by_payment_mode_report.click()
                time.sleep(5)

                store = data['test_Sales_By_Payment_Mode_Report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store is not None:
                    run_button.click()

            def test_Daily_Sales_Report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_Daily_Sales_Report']['username']
                password = data['test_Daily_Sales_Report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_daily_sales_report = self.driver.find_element(By.XPATH,
                                                                           "//span[text()='Daily Sales Report']")
                self.assertTrue(sidebar_menu_daily_sales_report.is_displayed(),
                                msg="Daily Salles Report menu is not displayed.")
                sidebar_menu_daily_sales_report.click()
                time.sleep(5)

                store = data['test_Daily_Sales_Report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store is not None:
                    run_button.click()

            def test_amount_wise_nob_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_amount_wise_nob_report']['username']
                password = data['test_amount_wise_nob_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_amount_wise_nob_report = self.driver.find_element(By.XPATH,
                                                                               "//span[text()='Amount Wise NOB Report']")
                self.assertTrue(sidebar_menu_amount_wise_nob_report.is_displayed(),
                                msg="Amount Wise NOB Report menu is not displayed.")
                sidebar_menu_amount_wise_nob_report.click()
                time.sleep(5)

                store = data['test_amount_wise_nob_report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store is not None:
                    run_button.click()

            def test_hourly_sales_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_hourly_sales_report']['username']
                password = data['test_hourly_sales_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_hourly_sales_report = self.driver.find_element(By.XPATH,
                                                                            "//span[text()='Hourly Sales Report']")
                self.assertTrue(sidebar_menu_hourly_sales_report.is_displayed(),
                                msg="Hourly Sales Report menu is not displayed.")
                sidebar_menu_hourly_sales_report.click()
                time.sleep(5)

                store = data['test_hourly_sales_report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                product = data['test_hourly_sales_report']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store is not None:
                    run_button.click()

            def test_tax_summery_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_tax_summery_report']['username']
                password = data['test_tax_summery_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_hourly_sales_report = self.driver.find_element(By.XPATH,
                                                                            "//span[text()='Tax Summary Report']")
                self.assertTrue(sidebar_menu_hourly_sales_report.is_displayed(),
                                msg="Tax Summery Report menu is not displayed.")
                sidebar_menu_hourly_sales_report.click()
                time.sleep(5)

                store = data['test_tax_summery_report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store is not None:
                    run_button.click()

            def test_sales_tax_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_sales_tax_report']['username']
                password = data['test_sales_tax_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_sales_tax_report = self.driver.find_element(By.XPATH,
                                                                         "//span[text()='Sales Tax Report']")
                self.assertTrue(sidebar_menu_sales_tax_report.is_displayed(),
                                msg="Sales Tax Report menu is not displayed.")
                sidebar_menu_sales_tax_report.click()
                time.sleep(5)

                store = data['test_sales_tax_report']['Store']
                input_store = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_store is not None:
                    run_button.click()

            def test_wastage_summery_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_wastage_summery_report']['username']
                password = data['test_wastage_summery_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_wastage_summery_report = self.driver.find_element(By.XPATH,
                                                                               "//span[text()='Wastage Summary Report']")
                self.assertTrue(sidebar_menu_wastage_summery_report.is_displayed(),
                                msg="Wastage Summery Report menu is not displayed.")
                sidebar_menu_wastage_summery_report.click()
                time.sleep(5)

                business_unit = data['test_wastage_summery_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                storage_location = data['test_wastage_summery_report']['Storage_Location']
                input_storage_location = self.driver.find_element(By.ID, "m_warehouse")
                self.assertTrue(input_storage_location.is_displayed(), msg="Storage Location input is not displayed.")
                input_storage_location.send_keys(storage_location)
                time.sleep(5)

                product = data['test_wastage_summery_report']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_stock_ledger_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_stock_ledger_report']['username']
                password = data['test_stock_ledger_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_stock_ledger_report = self.driver.find_element(By.XPATH,
                                                                            "//span[text()='Stock Ledger Report']")
                self.assertTrue(sidebar_menu_stock_ledger_report.is_displayed(),
                                msg="Stock Ledger Report menu is not displayed.")
                sidebar_menu_stock_ledger_report.click()
                time.sleep(5)

                business_unit = data['test_stock_ledger_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                storage_location = data['test_stock_ledger_report']['Storage_Location']
                input_storage_location = self.driver.find_element(By.ID, "m_warehouse")
                self.assertTrue(input_storage_location.is_displayed(), msg="Storage Location input is not displayed.")
                input_storage_location.send_keys(storage_location)
                time.sleep(5)

                product_category = data['test_stock_ledger_report']['Product_Category']
                input_product_category = self.driver.find_element(By.ID, "m_product_category")
                self.assertTrue(input_product_category.is_displayed(), msg="Product Category input is not displayed.")
                input_product_category.send_keys(product_category)
                time.sleep(5)

                product = data['test_stock_ledger_report']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_in_transit_stock_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_in_transit_stock_report']['username']
                password = data['test_in_transit_stock_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_in_transit_stock_report = self.driver.find_element(By.XPATH,
                                                                                "//span[text()='In Transit Stock Report']")
                self.assertTrue(sidebar_menu_in_transit_stock_report.is_displayed(),
                                msg="In Transit Stock Report menu is not displayed.")
                sidebar_menu_in_transit_stock_report.click()
                time.sleep(5)

                business_unit = data['test_in_transit_stock_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_inventory_adjustment_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_inventory_adjustment_report']['username']
                password = data['test_inventory_adjustment_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_inventory_adjustment_report = self.driver.find_element(By.XPATH,
                                                                                    "//span[text()='Inventory Adjustment Report']")
                self.assertTrue(sidebar_menu_inventory_adjustment_report.is_displayed(),
                                msg="Inventory Adjustment Report menu is not displayed.")
                sidebar_menu_inventory_adjustment_report.click()
                time.sleep(5)

                business_unit = data['test_inventory_adjustment_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                product_category = data['test_inventory_adjustment_report']['Product_Category']
                input_product_category = self.driver.find_element(By.ID, "m_product_category_id")
                self.assertTrue(input_product_category.is_displayed(), msg="Product Category input is not displayed.")
                input_product_category.send_keys(product_category)
                time.sleep(5)

                product = data['test_inventory_adjustment_report']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_stock_position_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_stock_position_report']['username']
                password = data['test_stock_position_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_stock_position_report = self.driver.find_element(By.XPATH,
                                                                              "//span[text()='Stock Position Report']")
                self.assertTrue(sidebar_menu_stock_position_report.is_displayed(),
                                msg="Stock Position Report menu is not displayed.")
                sidebar_menu_stock_position_report.click()
                time.sleep(5)

                business_unit = data['test_stock_position_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                storage_location = data['test_stock_position_report']['Storage_Location']
                input_storage_location = self.driver.find_element(By.ID, "WarehouseID")
                self.assertTrue(input_storage_location.is_displayed(), msg="Storage Location input is not displayed.")
                input_storage_location.send_keys(storage_location)
                time.sleep(5)

                product = data['test_stock_position_report']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_stock_aging_report_retail(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_stock_aging_report_retail']['username']
                password = data['test_stock_aging_report_retail']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_stock_aging_report_retail = self.driver.find_element(By.XPATH,
                                                                                  "//span[text()='Stock Aging Report Retail']")
                self.assertTrue(sidebar_menu_stock_aging_report_retail.is_displayed(),
                                msg="Stock Aging Report Retail menu is not displayed.")
                sidebar_menu_stock_aging_report_retail.click()
                time.sleep(5)

                business_unit = data['test_stock_aging_report_retail']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                supplier = data['test_stock_aging_report_retail']['Supplier']
                input_supplier = self.driver.find_element(By.ID, "p_supplier_id")
                self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
                input_supplier.send_keys(supplier)
                time.sleep(5)

                product_category = data['test_stock_aging_report_retail']['Product_Category']
                input_product_category = self.driver.find_element(By.ID, "m_product_category_id")
                self.assertTrue(input_product_category.is_displayed(), msg="Product Category input is not displayed.")
                input_product_category.send_keys(product_category)
                time.sleep(5)

                product = data['test_stock_aging_report_retail']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_low_stock_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_low_stock_report']['username']
                password = data['test_low_stock_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_low_stock_report = self.driver.find_element(By.XPATH,
                                                                         "//span[text()='Low Stock Report']")
                self.assertTrue(sidebar_menu_low_stock_report.is_displayed(),
                                msg="Low Stock Report menu is not displayed.")
                sidebar_menu_low_stock_report.click()
                time.sleep(5)

                business_unit = data['test_low_stock_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                storage_location = data['test_low_stock_report']['Storage_Location']
                input_storage_location = self.driver.find_element(By.ID, "m_warehouse")
                self.assertTrue(input_storage_location.is_displayed(), msg="Storage Location input is not displayed.")
                input_storage_location.send_keys(storage_location)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_current_stock_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_current_stock_report']['username']
                password = data['test_current_stock_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_current_stock_report = self.driver.find_element(By.XPATH,
                                                                             "//span[text()='Current Stock Report']")
                self.assertTrue(sidebar_menu_current_stock_report.is_displayed(),
                                msg="Current Stock Report menu is not displayed.")
                sidebar_menu_current_stock_report.click()
                time.sleep(5)

                business_unit = data['test_current_stock_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                storage_location = data['test_current_stock_report']['Storage_Location']
                input_storage_location = self.driver.find_element(By.ID, "m_warehouse")
                self.assertTrue(input_storage_location.is_displayed(), msg="Storage Location input is not displayed.")
                input_storage_location.send_keys(storage_location)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_product_wastage_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_product_wastage_report']['username']
                password = data['test_product_wastage_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_product_wastage_report = self.driver.find_element(By.XPATH,
                                                                               "//span[text()='Product Wastage Report']")
                self.assertTrue(sidebar_menu_product_wastage_report.is_displayed(),
                                msg="Current Stock Report menu is not displayed.")
                sidebar_menu_product_wastage_report.click()
                time.sleep(5)

                business_unit = data['test_product_wastage_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_stock_movement_report_retail(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_stock_movement_report_retail']['username']
                password = data['test_stock_movement_report_retail']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_stock_movement_report_retail = self.driver.find_element(By.XPATH,
                                                                                     "//span[text()='Stock Movement Report (Retail)']")
                self.assertTrue(sidebar_menu_stock_movement_report_retail.is_displayed(),
                                msg="Stock Movement Report Retail menu is not displayed.")
                sidebar_menu_stock_movement_report_retail.click()
                time.sleep(5)

                business_unit = data['test_stock_movement_report_retail']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                product_category = data['test_stock_movement_report_retail']['Product_Category']
                input_product_category = self.driver.find_element(By.ID, "m_product_category_id")
                self.assertTrue(input_product_category.is_displayed(), msg="Product Category input is not displayed.")
                input_product_category.send_keys(product_category)
                time.sleep(5)

                product = data['test_stock_movement_report_retail']['Product']
                input_product = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product.is_displayed(), msg="Product input is not displayed.")
                input_product.send_keys(product)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_pending_stock_issue_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_pending_stock_issue_report']['username']
                password = data['test_pending_stock_issue_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_pending_stock_issue_report = self.driver.find_element(By.XPATH,
                                                                                   "//span[text()='Pending Stock Issue Report']")
                self.assertTrue(sidebar_menu_pending_stock_issue_report.is_displayed(),
                                msg="Pending Stock Issue Report menu is not displayed.")
                sidebar_menu_pending_stock_issue_report.click()
                time.sleep(5)

                business_unit = data['test_pending_stock_issue_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_purchase_summary_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_purchase_summary_report']['username']
                password = data['test_purchase_summary_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_purchase_summary_report = self.driver.find_element(By.XPATH,
                                                                                "//span[text()='Purchase Summary Report']")
                self.assertTrue(sidebar_menu_purchase_summary_report.is_displayed(),
                                msg="Purchase Summary Report menu is not displayed.")
                sidebar_menu_purchase_summary_report.click()
                time.sleep(5)

                business_unit = data['test_purchase_summary_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                order_status = data['test_purchase_summary_report']['Order_Status']
                input_order_status = self.driver.find_element(By.ID, "docstatus")
                self.assertTrue(input_order_status.is_displayed(), msg="Order Status input is not displayed.")
                input_order_status.send_keys(order_status)
                time.sleep(5)

                supplier = data['test_purchase_summary_report']['Supplier']
                input_supplier = self.driver.find_element(By.ID, "p_supplier_id")
                self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
                input_supplier.send_keys(supplier)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_purchase_by_product_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_purchase_by_product_report']['username']
                password = data['test_purchase_by_product_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_purchase_by_product_report = self.driver.find_element(By.XPATH,
                                                                                   "//span[text()='Purchase By Product Report']")
                self.assertTrue(sidebar_menu_purchase_by_product_report.is_displayed(),
                                msg="Purchase Summary Report menu is not displayed.")
                sidebar_menu_purchase_by_product_report.click()
                time.sleep(5)

                business_unit = data['test_purchase_by_product_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                supplier = data['test_purchase_by_product_report']['Supplier']
                input_supplier = self.driver.find_element(By.ID, "p_supplier_id")
                self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
                input_supplier.send_keys(supplier)
                time.sleep(5)

                product_name = data['test_purchase_by_product_report']['Product_Name']
                input_product_name = self.driver.find_element(By.ID, "m_product_id")
                self.assertTrue(input_product_name.is_displayed(), msg="Product Name input is not displayed.")
                input_product_name.send_keys(product_name)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_purchase_by_supplier_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_purchase_by_supplier_report']['username']
                password = data['test_purchase_by_supplier_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_purchase_by_supplier_report = self.driver.find_element(By.XPATH,
                                                                                    "//span[text()='Purchase By Supplier Report']")
                self.assertTrue(sidebar_menu_purchase_by_supplier_report.is_displayed(),
                                msg="Purchase By Supplier Report menu is not displayed.")
                sidebar_menu_purchase_by_supplier_report.click()
                time.sleep(5)

                business_unit = data['test_purchase_by_supplier_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                supplier = data['test_purchase_by_supplier_report']['Supplier']
                input_supplier = self.driver.find_element(By.ID, "p_supplier_id")
                self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
                input_supplier.send_keys(supplier)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_purchase_tax_summary_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_purchase_tax_summary_report']['username']
                password = data['test_purchase_tax_summary_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_purchase_by_product_report = self.driver.find_element(By.XPATH,
                                                                                   "//span[text()='Purchase Tax Summary Report']")
                self.assertTrue(sidebar_menu_purchase_by_product_report.is_displayed(),
                                msg="Purchase Tax Summary Report menu is not displayed.")
                sidebar_menu_purchase_by_product_report.click()
                time.sleep(5)

                business_unit = data['test_purchase_tax_summary_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                tax_category = data['test_purchase_tax_summary_report']['Tax_Category']
                input_tax_category = self.driver.find_element(By.ID, "cs_tax_id")
                self.assertTrue(input_tax_category.is_displayed(), msg="Tax Category input is not displayed.")
                input_tax_category.send_keys(tax_category)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

            def test_supplier_statement_report(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_supplier_statement_report']['username']
                password = data['test_supplier_statement_report']['password']
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

                menu_reports = self.driver.find_element(By.XPATH, "//span[text()='Reports']")
                self.assertTrue(menu_reports.is_displayed(), msg="Reports Menu is not Displayed")
                menu_reports.click()
                time.sleep(5)

                sidebar_menu_supplier_statement_report = self.driver.find_element(By.XPATH,
                                                                                  "//span[text()='Supplier Statement Report']")
                self.assertTrue(sidebar_menu_supplier_statement_report.is_displayed(),
                                msg="Supplier Statement Report menu is not displayed.")
                sidebar_menu_supplier_statement_report.click()
                time.sleep(5)

                business_unit = data['test_supplier_statement_report']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "cs_bunit_id")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                supplier = data['test_supplier_statement_report']['Supplier']
                input_supplier = self.driver.find_element(By.ID, "p_supplier_id")
                self.assertTrue(input_supplier.is_displayed(), msg="Supplier input is not displayed.")
                input_supplier.send_keys(supplier)
                time.sleep(5)

                run_button = self.driver.find_element(By.XPATH, "//span[text()='Run']")
                self.assertTrue(run_button.is_displayed(), msg="Run button is not displayed.")
                if input_business_unit is not None:
                    run_button.click()

        # class for Store Admin test cases
        class TestStoreAdminSettingsData(unittest.TestCase):
            def setUp(self):
                self.driver = webdriver.Chrome()

            def tearDown(self):
                self.driver.close()

            def test_addBusiness_unit(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addBusiness_unit']['username']
                password = data['test_addBusiness_unit']['password']
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

                business_unit_id = data["test_addBusiness_unit"]["Business_unit_id"]
                input_business_unit_id = self.driver.find_element(By.ID, "headerTab_01BE43C2E97742A6A4048A5AD7AE8995")
                self.assertTrue(input_business_unit_id.is_displayed(), msg="Business Unit ID input is not displayed.")
                input_business_unit_id.send_keys(business_unit_id)
                time.sleep(5)

                name = data["test_addBusiness_unit"]["Name"]
                input_name = self.driver.find_element(By.ID, "headerTab_4D6B14DB22364215ADF09FC23E3483F1")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                description = data["test_addBusiness_unit"]["Description"]
                input_description = self.driver.find_element(By.ID, "headerTab_BDC6B7BF5CB844A8803628E9E2D0F08E")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                type = data["test_addBusiness_unit"]["Type"]
                input_type = self.driver.find_element(By.ID, "headerTab_E28CA6746CD74D5187C6AE3127E83974")
                self.assertTrue(input_type.is_displayed(), msg="Type input is not displayed.")
                input_type.send_keys(type)
                time.sleep(5)

                parent_business_unit = data["test_addBusiness_unit"]["Parent_Business_Unit"]
                input_parent_business_unit = self.driver.find_element(By.ID,
                                                                      "headerTab_AD346BE71E244CCEA9F7CC549EEC3CDA")
                self.assertTrue(input_parent_business_unit.is_displayed(),
                                msg="Parent Business Unit input is not displayed.")
                input_parent_business_unit.send_keys(parent_business_unit)
                time.sleep(5)

                legal_entity = data["test_addBusiness_unit"]["Legal_Entity"]
                input_legal_entity = self.driver.find_element(By.ID, "headerTab_47D85D2F9BDA45FF9F5C081633BBE7AE")
                self.assertTrue(input_legal_entity.is_displayed(), msg="Legal Entity input is not displayed.")
                input_legal_entity.send_keys(legal_entity)
                time.sleep(5)

                gst_no = data["test_addBusiness_unit"]["GST_No"]
                input_gst_no = self.driver.find_element(By.ID, "headerTab_7D3FB0064E2F4804A855BB8F8D14D1E2")
                self.assertTrue(input_gst_no.is_displayed(), msg="GST No input is not displayed.")
                input_gst_no.send_keys(gst_no)
                time.sleep(5)

                currency = data["test_addBusiness_unit"]["Currency"]
                input_currency = self.driver.find_element(By.ID, "headerTab_94F9DE8CCC4D4460A1900A8C4A1ACF75")
                self.assertTrue(input_currency.is_displayed(), msg="Currency input is not displayed.")
                input_currency.send_keys(currency)
                time.sleep(5)

                external_bunit_ref = data["test_addBusiness_unit"]["External_Bunit_ref"]
                input_external_bunit_ref = self.driver.find_element(By.ID, "headerTab_6965D8D307D340BFA38C14E033EEAB8E")
                self.assertTrue(input_external_bunit_ref.is_displayed(), msg="Currency input is not displayed.")
                input_external_bunit_ref.send_keys(external_bunit_ref)
                time.sleep(5)

                latitude = data["test_addBusiness_unit"]["Latitude"]
                input_latitude = self.driver.find_element(By.ID, "headerTab_1726DBCFE8464A50A2E6C3CB1FC533AC")
                self.assertTrue(input_latitude.is_displayed(), msg="Latitude input is not displayed.")
                input_latitude.send_keys(latitude)
                time.sleep(5)

                longitude = data["test_addBusiness_unit"]["Longitude"]
                input_longitude = self.driver.find_element(By.ID, "headerTab_C1B99AD7C25A40A18B69B61AE44BC7C7")
                self.assertTrue(input_longitude.is_displayed(), msg="Longitude input is not displayed.")
                input_longitude.send_keys(longitude)
                time.sleep(5)

                image_url = data["test_addBusiness_unit"]["Image_url"]
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

            def test_addStorage_location(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addStorage_location']['username']
                password = data['test_addStorage_location']['password']
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

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_storage_location = self.driver.find_element(By.XPATH, "//span[text()='Storage Location']")
                self.assertTrue(sidebar_menu_storage_location.is_displayed(),
                                msg="Storage Location menu is not displayed.")
                sidebar_menu_storage_location.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                business_unit = data['test_addStorage_location']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "headerTab_409B6D159F984629BB664FDEC90B1936")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                value = data['test_addStorage_location']['Value']
                input_value = self.driver.find_element(By.ID, "headerTab_5ADE8D2E8C0149C5BFFCC270BB238548")
                self.assertTrue(input_value.is_displayed(), msg="Value input is not displayed.")
                input_value.send_keys(value)
                time.sleep(5)

                name = data['test_addStorage_location']['Name']
                input_name = self.driver.find_element(By.ID, "headerTab_8FF51B00ABCE45D59FD2BC18671550AA")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                storage_capacity = data['test_addStorage_location']['Storage_Capacity']
                input_storage_capacity = self.driver.find_element(By.ID, "headerTab_04A9A8C3F1494BDF874D5028EFE75295")
                self.assertTrue(input_storage_capacity.is_displayed(), msg="Storage Capacity input is not displayed.")
                input_storage_capacity.send_keys(storage_capacity)
                time.sleep(5)

                active_check = self.driver.find_element(By.ID, "headerTab_44F0C43B0466459A879D384057BEE1F9")
                self.assertTrue(active_check.is_displayed(), msg="Active Check box is not displayed.")
                if not active_check.is_selected():
                    active_check.click()

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_business_unit and input_value and input_name is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_addTill(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addTill']['username']
                password = data['test_addTill']['password']
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

                store = data['test_addTill']['Store']
                input_store = self.driver.find_element(By.ID, "headerTab_7FE7DEA08CD846AF9AFFEFB152C4B234")
                self.assertTrue(input_store.is_displayed(), msg="Store input is not displayed.")
                input_store.send_keys(store)
                time.sleep(5)

                pos_type = data['test_addTill']['POS_Type']
                input_pos_type = self.driver.find_element(By.ID, "headerTab_521F1546BCF24539B800B3FE6417F92C")
                self.assertTrue(input_pos_type.is_displayed(), msg="Pos Type input is not displayed.")
                input_pos_type.send_keys(pos_type)
                time.sleep(5)

                till_id = data['test_addTill']['Till_ID']
                input_till_id = self.driver.find_element(By.ID, "headerTab_8FF51B00ABCE45D59FD2BC18671550AA")
                self.assertTrue(input_till_id.is_displayed(), msg="Till ID input is not displayed.")
                input_till_id.send_keys(till_id)
                time.sleep(5)

                name = data['test_addTill']['Name']
                input_name = self.driver.find_element(By.ID, "headerTab_2BFAD20AC82E42CBB295A7E72386A7CA")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                description = data['test_addTill']['Description']
                input_description = self.driver.find_element(By.ID, "headerTab_5DBB7666597A4AB4B45BF239EF239F68")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                next_order_number = data['test_addTill']['Next_Order_Number']
                input_next_order_number = self.driver.find_element(By.ID, "headerTab_CFCE0A38E8ED4511AC74D68BD77F2D17")
                self.assertTrue(input_next_order_number.is_displayed(), msg="Description input is not displayed.")
                input_next_order_number.send_keys(next_order_number)
                time.sleep(5)

                prefix = data['test_addTill']['Prefix']
                input_prefix = self.driver.find_element(By.ID, "headerTab_2350596E8BC94DB484B121448DA8EFD3")
                self.assertTrue(input_prefix.is_displayed(), msg="Prefix input is not displayed.")
                input_prefix.send_keys(prefix)
                time.sleep(5)

                suffix = data['test_addTill']['Suffix']
                input_suffix = self.driver.find_element(By.ID, "headerTab_28A68B46C8694CD08F5DBA2EDFEF9D95")
                self.assertTrue(input_suffix.is_displayed(), msg="Suffix input is not displayed.")
                input_suffix.send_keys(suffix)
                time.sleep(5)

                access_controller = data['test_addTill']['Access_Controller']
                input_access_controller = self.driver.find_element(By.ID, "headerTab_67EBFF9CE4AB48B4BE20409D2B6D8FB9")
                self.assertTrue(input_access_controller.is_displayed(), msg="Access Controller input is not displayed.")
                input_access_controller.send_keys(access_controller)
                time.sleep(5)

                enable_paynow_check = self.driver.find_element(By.ID, "headerTab_759A7EECAB264992B74BFCF455D641A5")
                if not enable_paynow_check.is_selected():
                    enable_paynow_check.click()

                kot_print_template = data['test_addTill']['KOT_Print_Template']
                input_kot_print_template = self.driver.find_element(By.ID, "headerTab_F4D0FD94C81242E88028BFCCA06EDE13")
                self.assertTrue(input_kot_print_template.is_displayed(),
                                msg="KOT Print Template input is not displayed.")
                input_kot_print_template.send_keys(kot_print_template)
                time.sleep(5)

                status = data['test_addTill']['Status']
                input_status = self.driver.find_element(By.ID, "headerTab_18F1AD63A40E4ABFB3832F568C5EC2C8")
                self.assertTrue(input_status.is_displayed(),
                                msg="Status input is not displayed.")
                input_status.send_keys(status)
                time.sleep(5)

                logged_in_cashier = data['test_addTill']['Logged_in_Cashier']
                input_logged_in_cashier = self.driver.find_element(By.ID, "headerTab_011BF7B786424F3A948092D3D0A9CE24")
                self.assertTrue(input_logged_in_cashier.is_displayed(),
                                msg="Logged In Cashier input is not displayed.")
                input_logged_in_cashier.send_keys(logged_in_cashier)
                time.sleep(5)

                enable_rfid_check = self.driver.find_element(By.ID, "headerTab_D60187E388584AFA8752E23D469C88A2")
                self.assertTrue(enable_rfid_check.is_displayed(), msg="Enable RFID Check box is not displayed.")
                if not enable_rfid_check.is_selected():
                    enable_rfid_check.click()

                cancel_kot_print_template = data['test_addTill']['Cancel_KOT_Print_Template']
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

            def test_addTax_Category(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addTax_Category']['username']
                password = data['test_addTax_Category']['password']
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

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_tax_category = self.driver.find_element(By.XPATH, "//span[text()='Tax Category']")
                self.assertTrue(sidebar_menu_tax_category.is_displayed(), msg="Tax Category menu is not displayed.")
                sidebar_menu_tax_category.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                business_unit = data['test_addTax_Category']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "headerTab_3D64DCD5949449A68576ACE794200D5D")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                name = data['test_addTax_Category']['Name']
                input_name = self.driver.find_element(By.ID, "headerTab_7DA02A5644AE424EB3B4CB308144CE27")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                description = data['test_addTax_Category']['Description']
                input_description = self.driver.find_element(By.ID, "headerTab_F724B12D741A4FF0A6B293808713658D")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                intra_region_tax = data['test_addTax_Category']['Intra_Region_Tax']
                input_intra_region_tax = self.driver.find_element(By.ID, "headerTab_4AFDB8C5C1BE4A3DBFEBBAE45205AEF2")
                self.assertTrue(input_intra_region_tax.is_displayed(), msg="Intra Region Tax input is not displayed.")
                input_intra_region_tax.send_keys(intra_region_tax)
                time.sleep(5)

                inter_region_tax = data['test_addTax_Category']['Inter_Region_Tax']
                input_inter_region_tax = self.driver.find_element(By.ID, "headerTab_646A99E284794CC4A811921C16C24CEB")
                self.assertTrue(input_inter_region_tax.is_displayed(), msg="Inter Region Tax input is not displayed.")
                input_inter_region_tax.send_keys(inter_region_tax)
                time.sleep(5)

                is_default_check = self.driver.find_element(By.ID, "headerTab_81D0B599D6FF4A4A9EF97EF1B24DF1DF")
                if not is_default_check.is_selected():
                    is_default_check.click()

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_business_unit and input_name is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_addTax(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addTax']['username']
                password = data['test_addTax']['password']
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

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_tax = self.driver.find_element(By.XPATH, "//span[text()='Tax']")
                self.assertTrue(sidebar_menu_tax.is_displayed(), msg="Tax menu is not displayed.")
                sidebar_menu_tax.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                business_unit = data['test_addTax']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "headerTab_DFD3F62756804A85B45F107FA2BDA845")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                name = data['test_addTax']['Name']
                input_name = self.driver.find_element(By.ID, "headerTab_7DF2751B3FFC41ECAEFF6437499439A1")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                tax_category = data['test_addTax']['Tax_Category']
                input_tax_category = self.driver.find_element(By.ID, "headerTab_973974F051234486A457D13DCBC6F16C")
                self.assertTrue(input_tax_category.is_displayed(), msg="Tax Category input is not displayed.")
                input_tax_category.send_keys(tax_category)
                time.sleep(5)

                rate = data['test_addTax']['Rate']
                input_rate = self.driver.find_element(By.ID, "headerTab_B04D8168AAA44E1A98E79D7DBC7593BB")
                self.assertTrue(input_rate.is_displayed(), msg="Rate input is not displayed.")
                input_rate.send_keys(rate)
                time.sleep(5)

                parent_tax_rate = data['test_addTax']['Parent_Tax_Rate']
                input_parent_tax_rate = self.driver.find_element(By.ID, "headerTab_AB3C0217E29D46C0B724813E2B50D2E0")
                self.assertTrue(input_parent_tax_rate.is_displayed(), msg="Parent Tax Rate input is not displayed.")
                input_parent_tax_rate.send_keys(parent_tax_rate)
                time.sleep(5)

                description = data['test_addTax']['Description']
                input_description = self.driver.find_element(By.ID, "headerTab_5BE3F41C5F904E6298351B164B2D21C6")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                is_default_check = self.driver.find_element(By.ID, "headerTab_B80E5787B5B548E48843C37E346D5CE3")
                if not is_default_check.is_selected():
                    is_default_check.click()

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_business_unit and input_name and input_tax_category and input_rate is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_addSupplier_Category(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addSupplier_Category']['username']
                password = data['test_addSupplier_Category']['password']
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

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_supplier_category = self.driver.find_element(By.XPATH,
                                                                          "//span[text()='Supplier Category']")
                self.assertTrue(sidebar_menu_supplier_category.is_displayed(),
                                msg="Supplier Category menu is not displayed.")
                sidebar_menu_supplier_category.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='Add New']")
                self.assertTrue(add_new_button.is_displayed(), msg="Add New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                business_unit = data['test_addSupplier_Category']['Business_Unit']
                input_business_unit = self.driver.find_element(By.ID, "headerTab_92EB5F77E8AB463988C4210330135C5A")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                code = data['test_addSupplier_Category']['Code']
                input_code = self.driver.find_element(By.ID, "headerTab_BDB41292781044BC8D385C7F11249461")
                self.assertTrue(input_code.is_displayed(), msg="Code input is not displayed.")
                input_code.send_keys(code)
                time.sleep(5)

                category_name = data['test_addSupplier_Category']['Category_Name']
                input_category_name = self.driver.find_element(By.ID, "headerTab_AA15BE6AB52C43AAAE5A12ED46012E5D")
                self.assertTrue(input_category_name.is_displayed(), msg="Category Name input is not displayed.")
                input_category_name.send_keys(category_name)
                time.sleep(5)

                default_check = self.driver.find_element(By.ID, "headerTab_31119DADA57D4D68ABA36936671675D0")
                if not default_check.is_selected():
                    default_check.click()

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_business_unit and input_code and input_category_name is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_POS_Settings(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_POS_Settings']['username']
                password = data['test_POS_Settings']['password']
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
                time.sleep(5)

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_pos_settings = self.driver.find_element(By.XPATH, "//span[text()='POS Settings']")
                self.assertTrue(sidebar_menu_pos_settings.is_displayed(), msg="POS Settings menu is not displayed.")
                sidebar_menu_pos_settings.click()
                time.sleep(5)
                #Payments
                enable_cash_check = self.driver.find_element(By.ID, "mainForm_enableCash")
                self.assertTrue(enable_cash_check.is_displayed(), msg="Enable Cash Check is not displayed.")
                if not enable_cash_check.is_selected():
                    enable_cash_check.click()

                enable_card_check = self.driver.find_element(By.ID, "mainForm_enableCard")
                self.assertTrue(enable_card_check.is_displayed(), msg="Enable Card Check is not displayed.")
                if not enable_card_check.is_selected():
                    enable_card_check.click()

                # Check if enable_card_integration is displayed and selected
                enable_card_integration = self.driver.find_element(By.ID, "mainForm_enableCardIntegration")
                self.assertTrue(enable_card_integration.is_displayed(), msg="Enable Card Integration is not displayed.")
                if not enable_card_integration.is_selected():
                    enable_card_integration.click()

                # Check if input_payment_combo_box is displayed
                payment_combo_box = data["test_POS_Settings"]["Payment_Mode"]
                input_payment_combo_box = self.driver.find_element(By.ID, "mainForm_enableCardIntegrationValue")
                self.assertTrue(input_payment_combo_box.is_displayed(), msg="Payment Combo Box is not displayed.")
                input_payment_combo_box.send_keys(payment_combo_box)
                # Customer
                customer_search_check = self.driver.find_element(By.ID, "mainForm_showCustomerSearch")
                self.assertTrue(customer_search_check.is_displayed(), msg="Customer Search Check box is not displayed.")
                if not customer_search_check.is_selected():
                    customer_search_check.click()

                customer_search = data["test_POS_Settings"]["Customer_Search"]
                customer_search_combo = self.driver.find_element(By.ID, "mainForm_showCustomerSearchValue")
                self.assertTrue(customer_search_combo.is_displayed(), msg="Customer Search Combo is not displayed.")
                customer_search_combo.send_keys()

                search_by_check = self.driver.find_element(By.ID, "mainForm_defaultCustomerSearch")
                self.assertTrue(search_by_check.is_displayed(), msg="Search by check box is not displayed.")
                if not search_by_check.is_selected():
                    search_by_check.click()

                by_name_check = self.driver.find_element(By.ID, "mainForm_byName")
                self.assertTrue(by_name_check.is_displayed(), msg="By Name Check box is not displayed")
                if not by_name_check.is_selected():
                    by_name_check.click()

                by_number_check = self.driver.find_element(By.ID, "mainForm_byNumber")
                self.assertTrue(by_number_check.is_displayed(), msg="By Number Check box is not displayed")
                if not by_number_check.is_selected():
                    by_number_check.click()
                # Cash Register
                enable_shift_open = self.driver.find_element(By.ID, "mainForm_showTillOpening")
                self.assertTrue(enable_shift_open.is_displayed(), msg="Enable Shift Open Check box is not displayed")
                if not enable_shift_open.is_selected():
                    enable_shift_open.click()

                enable_shift_close = self.driver.find_element(By.ID, "mainForm_shiftClose")
                self.assertTrue(enable_shift_close.is_displayed(), msg="Enable Shift Close Check box is not displayed")
                if not enable_shift_close.is_selected():
                    enable_shift_close.click()

                allow_petty_cash = self.driver.find_element(By.ID, "mainForm_pettyCash")
                self.assertTrue(allow_petty_cash.is_displayed(), msg="Allow Petty Cash Check box is not displayed")
                if not allow_petty_cash.is_selected():
                    allow_petty_cash.click()

                allow_cash_in = self.driver.find_element(By.ID, "mainForm_cashIn")
                self.assertTrue(allow_cash_in.is_displayed(), msg="Allow Cash In Check box is not displayed")
                if not allow_cash_in.is_selected():
                    allow_cash_in.click()

                allow_cash_out = self.driver.find_element(By.ID, "mainForm_cashOut")
                self.assertTrue(allow_cash_out.is_displayed(), msg="Allow Cash Out Check box is not displayed")
                if not allow_cash_out.is_selected():
                    allow_cash_out.click()
                #POS
                allow_return_refund = self.driver.find_element(By.ID, "mainForm_allowReturnRefund")
                self.assertTrue(allow_return_refund.is_displayed(), msg="Allow Return and Refund Check box is not displayed")
                if not allow_return_refund.is_selected():
                    allow_return_refund.click()

                allow_bill_parking = self.driver.find_element(By.ID, "mainForm_allowBillParking")
                self.assertTrue(allow_bill_parking.is_displayed(),
                                msg="Allow Bill Parking Check box is not displayed")
                if not allow_bill_parking.is_selected():
                    allow_bill_parking.click()

                show_sales_return = self.driver.find_element(By.ID, "mainForm_showSalesReturn")
                self.assertTrue(show_sales_return.is_displayed(),
                                msg="Show Sales Return Check box is not displayed")
                if not show_sales_return.is_selected():
                    show_sales_return.click()

                allow_return_exchange = self.driver.find_element(By.ID, "mainForm_showSalesReturn")
                self.assertTrue(allow_return_exchange.is_displayed(),
                                msg="Allow Return Exchange Check box is not displayed")
                if not allow_return_exchange.is_selected():
                    allow_return_exchange.click()

                show_product_images = self.driver.find_element(By.ID, "mainForm_showImage")
                self.assertTrue(show_product_images.is_displayed(),
                                msg="Show Product Images Check box is not displayed")
                if not show_product_images.is_selected():
                    show_product_images.click()
                # Sale Type
                cash_and_carry = self.driver.find_element(By.ID, "mainForm_cashCarry")
                self.assertTrue(cash_and_carry.is_displayed(),
                                msg="Cash and Carry Check box is not displayed")
                if not cash_and_carry.is_selected():
                    cash_and_carry.click()

                save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if enable_cash_check:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_addPricing_Rules(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addPricing_Rules']['username']
                password = data['test_addPricing_Rules']['password']
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

                type = data["test_addPricing_Rules"]["Type"]
                input_type = self.driver.find_element(By.ID, "headerTab_B3A125482C994AD784298943261113AF")
                self.assertTrue(input_type.is_displayed(), msg="Type input is not displayed.")
                input_type.send_keys(type)
                time.sleep(5)

                name = data["test_addPricing_Rules"]["Name"]
                input_name = self.driver.find_element(By.ID, "headerTab_1E2751866DC846728765C9C883C79E6A")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                printed_name = data["test_addPricing_Rules"]["Printed_Name"]
                input_printed_name = self.driver.find_element(By.ID, "headerTab_15D5EA483D2A43D794E3FF500D8D9DA3")
                self.assertTrue(input_printed_name.is_displayed(), msg="Printed Name input is not displayed.")
                input_printed_name.send_keys(printed_name)
                time.sleep(5)

                description = data["test_addPricing_Rules"]["Description"]
                input_description = self.driver.find_element(By.ID, "headerTab_3A6C9325FFEC42ACAC9E1BE83248F789")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                start_date = data["test_addPricing_Rules"]["Start_Date"]
                input_start_date = self.driver.find_element(By.ID, "headerTab_6184E60E039B474B96D37D32A6C3C70C")
                self.assertTrue(input_start_date.is_displayed(), msg="Start Date input is not displayed.")
                input_start_date.send_keys(start_date)
                time.sleep(5)

                end_date = data["test_addPricing_Rules"]["End_Date"]
                input_end_date = self.driver.find_element(By.ID, "headerTab_6184E60E039B474B96D37D32A6C3C70C")
                self.assertTrue(input_end_date.is_displayed(), msg="End Date input is not displayed.")
                input_end_date.send_keys(end_date)
                time.sleep(5)

                coupon_expiry_date = data["test_addPricing_Rules"]["Coupon_Expiry_Date"]
                input_coupon_expiry_date = self.driver.find_element(By.ID, "headerTab_A2511C5ED6C64CE393C940A0566CA3C5")
                self.assertTrue(input_coupon_expiry_date.is_displayed(), msg="Coupon Expiry Date input is not displayed.")
                input_coupon_expiry_date.send_keys(coupon_expiry_date)
                time.sleep(5)

                discount_type = data["test_addPricing_Rules"]["Discount_Type"]
                input_discount_type = self.driver.find_element(By.ID, "headerTab_81CA40B331EE47D794C5E67F5A8047BA")
                self.assertTrue(input_discount_type.is_displayed(),
                                msg="Discount Type input is not displayed.")
                input_discount_type.send_keys(discount_type)
                time.sleep(5)

                no_of_coupons = data["test_addPricing_Rules"]["No_of_Coupons"]
                input_no_of_coupons = self.driver.find_element(By.ID, "headerTab_3FFFB46E755C48E188486B12F71AD653")
                self.assertTrue(input_no_of_coupons.is_displayed(),
                                msg="No of Coupons input is not displayed.")
                input_no_of_coupons.send_keys(no_of_coupons)
                time.sleep(5)

                gift_voucher_type = data["test_addPricing_Rules"]["Gift_Voucher_Type"]
                input_gift_voucher_type = self.driver.find_element(By.ID, "headerTab_E0B20B2826D34F1DB24B98163F1870D1")
                self.assertTrue(input_gift_voucher_type.is_displayed(),
                                msg="Gift Voucher Type input is not displayed.")
                input_gift_voucher_type.send_keys(gift_voucher_type)
                time.sleep(5)

                minimum_qty = data["test_addPricing_Rules"]["Minimum_Qty"]
                input_minimum_qty = self.driver.find_element(By.ID, "headerTab_B7CFAF12181644B6A38196DEA23700E1")
                self.assertTrue(input_minimum_qty.is_displayed(),
                                msg="Minimum Quantity input is not displayed.")
                input_minimum_qty.send_keys(minimum_qty)
                time.sleep(5)

                maximum_qty = data["test_addPricing_Rules"]["Maximum_Qty"]
                input_maximum_qty = self.driver.find_element(By.ID, "headerTab_B7CFAF12181644B6A38196DEA23700E1")
                self.assertTrue(input_maximum_qty.is_displayed(),
                                msg="Maximum Quantity input is not displayed.")
                input_maximum_qty.send_keys(maximum_qty)
                time.sleep(5)

                discount_x_qty = data["test_addPricing_Rules"]["Discount_X_Qty"]
                input_discount_x_qty = self.driver.find_element(By.ID, "headerTab_72C66F3E59114363BEE65D4595D3E2B7")
                self.assertTrue(input_discount_x_qty.is_displayed(),
                                msg="Discount X Quantity input is not displayed.")
                input_discount_x_qty.send_keys(discount_x_qty)
                time.sleep(5)

                discount_y_qty = data["test_addPricing_Rules"]["Discount_Y_Qty"]
                input_discount_y_qty = self.driver.find_element(By.ID, "headerTab_C5466B6E083D4E52847868F792FB1B7C")
                self.assertTrue(input_discount_y_qty.is_displayed(),
                                msg="Discount Y Quantity input is not displayed.")
                input_discount_y_qty.send_keys(discount_y_qty)
                time.sleep(5)

                minimum_bill_amount = data["test_addPricing_Rules"]["Minimum_Bill_Amount"]
                input_minimum_bill_amount = self.driver.find_element(By.ID, "headerTab_C7CCB554D5CD4D40ACA88FC28C8FFC6C")
                self.assertTrue(input_minimum_bill_amount.is_displayed(),
                                msg="Minimum Bill Amount input is not displayed.")
                input_minimum_bill_amount.send_keys(minimum_bill_amount)
                time.sleep(5)

                maximum_bill_amount = data["test_addPricing_Rules"]["Maximum_Bill_Amount"]
                input_maximum_bill_amount = self.driver.find_element(By.ID,
                                                                     "headerTab_94738DCF997A4F16AEED3069A43604AF")
                self.assertTrue(input_maximum_bill_amount.is_displayed(),
                                msg="Minimum Bill Amount input is not displayed.")
                input_maximum_bill_amount.send_keys(maximum_bill_amount)
                time.sleep(5)

                pos_sales_type = data["test_addPricing_Rules"]["POS_Sales_Type"]
                input_pos_sales_type = self.driver.find_element(By.ID,
                                                                     "headerTab_318C3C5AA0034EE2B8D0FB8589D85B83")
                self.assertTrue(input_pos_sales_type.is_displayed(),
                                msg="POS Sales Type input is not displayed.")
                input_pos_sales_type.send_keys(pos_sales_type)
                time.sleep(5)

                fixed_unit_price = data["test_addPricing_Rules"]["Fixed_Unit_Price"]
                input_fixed_unit_price = self.driver.find_element(By.ID,
                                                                "headerTab_42B7DDEF58614DB4AE3C1F65BA214E4E")
                self.assertTrue(input_fixed_unit_price.is_displayed(),
                                msg="POS Sales Type input is not displayed.")
                input_fixed_unit_price.send_keys(fixed_unit_price)
                time.sleep(5)

                active_check = self.driver.find_element(By.ID, "headerTab_D9A5F490B80B4FEE9C99B303D6AAB6D9")
                self.assertTrue(active_check.is_displayed(), msg="Active Check is not displayed.")
                if not active_check.is_selected():
                    active_check.click()

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_type and input_name and input_start_date is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_addUser(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addUser']['username']
                password = data['test_addUser']['password']
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

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_user = self.driver.find_element(By.XPATH, "//span[text()='User']")
                self.assertTrue(sidebar_menu_user.is_displayed(),
                                msg="User menu is not displayed.")
                sidebar_menu_user.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='New']")
                self.assertTrue(add_new_button.is_displayed(), msg="New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                business_unit = data["test_addUser"]["Business_Unit"]
                input_business_unit = self.driver.find_element(By.ID, "control-hooks_bunitname")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                first_name = data["test_addUser"]["FirstName"]
                input_first_name = self.driver.find_element(By.ID, "control-hooks_firstname")
                self.assertTrue(input_first_name.is_displayed(), msg="First Name input is not displayed.")
                input_first_name.send_keys(first_name)
                time.sleep(5)

                last_name = data["test_addUser"]["LastName"]
                input_last_name = self.driver.find_element(By.ID, "control-hooks_lastname")
                self.assertTrue(input_last_name.is_displayed(), msg="Last Name input is not displayed.")
                input_last_name.send_keys(last_name)
                time.sleep(5)

                user_name = data["test_addUser"]["UserName"]
                input_user_name = self.driver.find_element(By.ID, "control-hooks_username")
                self.assertTrue(input_user_name.is_displayed(), msg="User Name input is not displayed.")
                input_user_name.send_keys(user_name)
                time.sleep(5)

                home_dashboard = data["test_addUser"]["Home_Dashboard"]
                input_home_dashboard = self.driver.find_element(By.ID, "control-hooks_home_dashboard_id")
                self.assertTrue(input_home_dashboard.is_displayed(), msg="Home Dashboard input is not displayed.")
                input_home_dashboard.send_keys(home_dashboard)
                time.sleep(5)

                home_window = data["test_addUser"]["Home_Window"]
                input_home_window = self.driver.find_element(By.ID, "control-hooks_home_window_id")
                self.assertTrue(input_home_window.is_displayed(), msg="Home Window input is not displayed.")
                input_home_window.send_keys(home_window)
                time.sleep(5)

                home_report = data["test_addUser"]["Home_Report"]
                input_home_report = self.driver.find_element(By.ID, "control-hooks_home_report_id")
                self.assertTrue(input_home_report.is_displayed(), msg="Home Window input is not displayed.")
                input_home_report.send_keys(home_report)
                time.sleep(5)

                admin_check = self.driver.find_element(By.ID, "control-hooks_isactive")
                self.assertTrue(admin_check.is_displayed(), msg="Admin Check box is not displayed.")
                if not admin_check.is_selected():
                    admin_check.click()
                else:
                    pass

                # auto_generate_password_check = self.driver.find_element(By.ID, "")
                # self.assertTrue(auto_generate_password_check.is_displayed(), msg="Admin Check box is not displayed.")
                # if not auto_generate_password_check.is_selected():
                #     auto_generate_password_check.click()
                # else:
                #     pass


                email = data["test_addUser"]["Email"]
                input_email = self.driver.find_element(By.ID, "control-hooks_email")
                self.assertTrue(input_email.is_displayed(), msg="Email input is not displayed.")
                input_email.send_keys(email)
                time.sleep(5)

                description = data["test_addUser"]["Description"]
                input_description = self.driver.find_element(By.ID, "control-hooks_description")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                save_button = self.driver.find_element(By.XPATH, "//span[text()='Save']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_business_unit and input_first_name and input_last_name and input_user_name is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_addReturn_Reasons(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addReturn_Reasons']['username']
                password = data['test_addReturn_Reasons']['password']
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

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_return_reason = self.driver.find_element(By.XPATH, "//span[text()='Return Reason']")
                self.assertTrue(sidebar_menu_return_reason.is_displayed(),
                                msg="Return Reason menu is not displayed.")
                sidebar_menu_return_reason.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='New']")
                self.assertTrue(add_new_button.is_displayed(), msg="New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                search_key = data["test_addReturn_Reasons"]["Search_Key"]
                input_search_key = self.driver.find_element(By.ID, "headerTab_B7E5EDABEBC744D4A0D3A833976D9AB5")
                self.assertTrue(input_search_key.is_displayed(), msg="Search Key input is not displayed.")
                input_search_key.send_keys(search_key)
                time.sleep(5)

                name = data["test_addReturn_Reasons"]["Name"]
                input_name = self.driver.find_element(By.ID, "headerTab_DF1455B50DAF4766BDCE2E3D2A200DC5")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                active_check = self.driver.find_element(By.ID, "headerTab_AA3A8B7C64394167AA35A4B971AD6890")
                self.assertTrue(active_check.is_displayed(), msg="Active Check box is not displayed.")
                if not active_check.is_selected():
                    active_check.click()
                else:
                    pass

                description = data["test_addReturn_Reasons"]["Description"]
                input_description = self.driver.find_element(By.ID, "headerTab_A56B505BC1BE4FD2B7464AE36B055143")
                self.assertTrue(input_description.is_displayed(), msg="Description input is not displayed.")
                input_description.send_keys(description)
                time.sleep(5)

                customer_return_check = self.driver.find_element(By.ID, "headerTab_F13A676C6B524EA98E4F311E7CA96515")
                self.assertTrue(customer_return_check.is_displayed(), msg="Customer Return Check box is not displayed.")
                if not customer_return_check.is_selected():
                    customer_return_check.click()
                else:
                    pass

                supplier_return_check = self.driver.find_element(By.ID, "headerTab_58BEB24E5F1E410EBB09C11A7A351826")
                self.assertTrue(supplier_return_check.is_displayed(), msg="Supplier Return Check box is not displayed.")
                if not supplier_return_check.is_selected():
                    supplier_return_check.click()
                else:
                    pass

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_search_key and input_name is not None:
                    save_button.click()
                else:
                    cancel_button.click()

            def test_addEmail_Templates(self):
                self.driver.maximize_window()

                self.driver.get("https://test-auth.cwcloud.in:8412/sign-in")
                time.sleep(5)
                username = data['test_addEmail_Templates']['username']
                password = data['test_addEmail_Templates']['password']
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

                menu_settings = self.driver.find_element(By.XPATH, "//span[text()='Settings']")
                self.assertTrue(menu_settings.is_displayed(), msg="Settings Menu is not Displayed")
                menu_settings.click()
                time.sleep(5)

                sidebar_menu_email_templates = self.driver.find_element(By.XPATH, "//span[text()='Email Templates']")
                self.assertTrue(sidebar_menu_email_templates.is_displayed(),
                                msg="Email Templates menu is not displayed.")
                sidebar_menu_email_templates.click()
                time.sleep(5)

                add_new_button = self.driver.find_element(By.XPATH, "//span[text()='New']")
                self.assertTrue(add_new_button.is_displayed(), msg="New button is not displayed.")
                add_new_button.click()
                time.sleep(5)

                business_unit = data["test_addEmail_Templates"]["Business_Unit"]
                input_business_unit = self.driver.find_element(By.ID, "headerTab_14B7879D3815481293B738A105C016BC")
                self.assertTrue(input_business_unit.is_displayed(), msg="Business Unit input is not displayed.")
                input_business_unit.send_keys(business_unit)
                time.sleep(5)

                name = data["test_addEmail_Templates"]["Name"]
                input_name = self.driver.find_element(By.ID, "headerTab_26146484C46744C5BAFA43181D36EEAA")
                self.assertTrue(input_name.is_displayed(), msg="Name input is not displayed.")
                input_name.send_keys(name)
                time.sleep(5)

                subject = data["test_addEmail_Templates"]["Subject"]
                input_subject = self.driver.find_element(By.ID, "headerTab_E768126E2C70413D86C1806B1AB207DA")
                self.assertTrue(input_subject.is_displayed(), msg="Subject input is not displayed.")
                input_subject.send_keys(subject)
                time.sleep(5)

                from_email = data["test_addEmail_Templates"]["From_Email"]
                input_from_email = self.driver.find_element(By.ID, "headerTab_F507A749DFE94E46A2F24BC7BA63ABB6")
                self.assertTrue(input_from_email.is_displayed(), msg="From Email input is not displayed.")
                input_from_email.send_keys(from_email)
                time.sleep(5)

                reply_to = data["test_addEmail_Templates"]["Reply_To"]
                input_reply_to = self.driver.find_element(By.ID, "headerTab_D4E52CF55E684D699F9D826F343DD6EA")
                self.assertTrue(input_reply_to.is_displayed(), msg="Reply to input is not displayed.")
                input_reply_to.send_keys(reply_to)
                time.sleep(5)

                to_email = data["test_addEmail_Templates"]["To_Email"]
                input_to_email = self.driver.find_element(By.ID, "headerTab_2B6CB7B0340447338A94D40EC3348491")
                self.assertTrue(input_to_email.is_displayed(), msg="To Email input is not displayed.")
                input_to_email.send_keys(to_email)
                time.sleep(5)

                cc_email = data["test_addEmail_Templates"]["CC_Email"]
                input_cc_email = self.driver.find_element(By.ID, "headerTab_8E8FE1C2F5804E12A11B527481A6A8A4")
                self.assertTrue(input_cc_email.is_displayed(), msg="CC Email input is not displayed.")
                input_cc_email.send_keys(cc_email)
                time.sleep(5)

                save_button = self.driver.find_element(By.XPATH, "//button[@id='step1']")
                self.assertTrue(save_button.is_displayed(), msg="Save Button is not Displayed.")
                cancel_button = self.driver.find_element(By.XPATH, "//span[text()='Cancel']")
                self.assertTrue(cancel_button.is_displayed(), msg="Cancel Button is not displayed.")
                if input_business_unit is not None:
                    save_button.click()
                else:
                    cancel_button.click()

        # Run the unittest test cases
        point_of_sale_suite = unittest.TestLoader().loadTestsFromTestCase(TestPOSData)
        # store_admin_products_suite = unittest.TestLoader().loadTestsFromTestCase(TestStoreAdminProductsData)
        # store_admin_sales_suite = unittest.TestLoader().loadTestsFromTestCase(TestStoreAdminSalesData)
        # store_admin_purchase_suite = unittest.TestLoader().loadTestsFromTestCase(TestStoreAdminPurchaseData)
        # store_admin_inventory_suite = unittest.TestLoader().loadTestsFromTestCase(TestStoreAdminInventoryData)
        # store_admin_reports_suite = unittest.TestLoader().loadTestsFromTestCase(TestStoreAdminReportsData)
        # store_admin_settings_suite = unittest.TestLoader().loadTestsFromTestCase(TestStoreAdminSettingsData)
        # Create a test suite and add loaded test cases to it
        # test_suite = unittest.TestSuite([point_of_sale_suite, store_admin_products_suite, store_admin_sales_suite, store_admin_purchase_suite, store_admin_inventory_suite, store_admin_reports_suite, store_admin_settings_suite])
        # unittest.TextTestRunner(verbosity=2).run(test_suite)
        unittest.TextTestRunner(verbosity=2).run(point_of_sale_suite)
        # # Set up the HTMLTestRunner
        # output_directory = os.path.expanduser("~") + "/Downloads/"
        # html_runner = HtmlTestRunner.HTMLTestRunner(
        #     # output=output_directory + 'test_reports',  # Output directory for the HTML report
        #     output='test_reports',  # Output directory for the HTML report
        #     add_timestamp=True
        #     # report_title='Test Automation Report',  # Title for the report
        #     # descriptions=True
        # )
        # #
        # # # Run the unittest test cases and generate the HTML report
        # html_runner.run(point_of_sale_suite)

        # Set the output file name and location
        # outfile = open("TestReport.html", "w")
        #
        # # Configure HTMLTestRunner
        # testRunner = HtmlTestRunner.HTMLTestRunner(stream=outfile)
        #
        # # Run the test suite
        # testRunner.run(point_of_sale_suite)




# Code for Quiting Window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TestAutomationApp(root)
    center_window(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()