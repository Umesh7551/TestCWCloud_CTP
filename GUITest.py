from CommonImportsPkg.common_imports import *

from Test_POSFunctionalPkg.TC_CashManagementTest import CashManagementTest
from Test_POSFunctionalPkg.TC_ParkBillTest import ParkBillTest
from Test_POSFunctionalPkg.TC_PointOfSaleTest import PointOfSaleTest
from Test_POSFunctionalPkg.TC_SalesHistoryTest import SalesHistoryTest
from Test_StoreAdminFunctionalPkg.TC_AddBrandTest import AddBrandTest


class TestAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CW Test Platform [CTP]")
        # self.root.resizable(False, False)
        self.root.geometry('400x300')
        # self.root.iconbitmap('/logocw.ico')
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
        image = Image.open("logo.png")

        # Convert the PIL image to a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(root, image=photo)
        # self.image_label = tk.Label(root, image=image)
        self.image_label.photo = photo
        self.image_label.place(x=50, y=130)
        # self.image_label.grid(row=4, column=2)
        # Initialize data variable to store the loaded JSON data
        # global data
        # self.data = None

    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'r') as json_file:
                self.data = json.load(json_file)
                # Store the loaded JSON data in a global variable or pass it to the test execution function
                # data = self.data
                # print(self.data)
                if self.data != None:
                    messagebox.showinfo("Success", "JSON File loaded successfully!!!")
                else:
                    messagebox.showerror("Error", "Please select valid file!!!")


    def run_tests(self):
        if self.data:
            # Create an instance of PointOfSaleTest and pass the data
            point_of_sale_test = PointOfSaleTest(data=self.data)
            park_bill_test = ParkBillTest(data=self.data)
            cash_management_test = CashManagementTest(data=self.data)
            sales_history_test = SalesHistoryTest(data=self.data)
            add_brand_test = AddBrandTest(data=self.data)

            # Create a test suite with the specific test case
            # suite_pos = unittest.TestSuite([park_bill_test])
            suite_pos = unittest.TestSuite([point_of_sale_test, park_bill_test, cash_management_test, sales_history_test, add_brand_test])

            # Run the tests
            # result = unittest.TextTestRunner().run(suite_pos)

            # Specify the path for the HTML report
            # report_file = 'test_report.html'

            # Open the report file in write mode
            # with open(report_file, 'w') as report:
            # Create an HTMLTestRunner instance
            runner = HTMLTestRunner(descriptions=True, report_title="CWCloud Unittest Results")

            # Run the tests and generate the HTML report
            result = runner.run(suite_pos)

            # Display a message box with the test results
            if result.wasSuccessful():
                messagebox.showinfo("Test Results", "All tests passed successfully!")
            else:
                messagebox.showerror("Test Results", "Some tests failed. Please check the console for details.")
        else:
            messagebox.showerror("Error", "Please first select JSON file!!!")


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