from CommonImportsPkg.common_imports import *


# logging.basicConfig(filename="CWCloudTest.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
class TestAutomationApp:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def get_test_cases(self):
        # Get the list of test cases dynamically
        test_cases = ['point_of_sale', 'park_bill', 'cash_management', 'sales_history', 'close_till', 'add_brand',
                      'add_business_unit', 'add_customers', 'add_email_templates', 'add_image_library', 'add_pos_orders',
                      'add_pricing_rules', 'add_product_catalogue', 'add_product_category', 'add_products', 'add_return_reasons',
                      'add_rfid_tag', 'add_storage_location', 'add_supplier_category', 'add_supplier', 'add_tax_category',
                      'add_tax', 'add_till', 'add_user', 'amount_wise_nob_report', 'current_stock_report',
                      'daily_sales_report', 'hourly_sales_report', 'in_transit_stock_report', 'inventory_adjustment_report',
                      'low_stock_report', 'pending_stock_issue_report', 'pos_settings', 'product_wastage_report', 'purchase_by_product_report',
                      'purchase_by_supplier_report', 'purchase_order', 'purchase_summary_report', 'purchase_tax_summary_report',
                      'quick_goods_receipt', 'quick_purchase_order', 'quick_stock_count', 'quick_stock_issue', 'quick_stock_receipt',
                      'quick_wastage_entry', 'sales_by_customer_report', 'sales_by_payment_mode_report', 'sales_by_product_category',
                      'sales_by_prdouct_report', 'sales_tax_report', 'stock_aging_report_retail', 'stock_ledger_report', 'stock_movement_report_retail',
                      'stock_position_report', 'supplier_statement_report', 'tax_summary_report', 'wastage_summary_report'
                      ]
        return test_cases

    def get_test_class(self, test_case_name):
        # Convert test case name to class name (assuming CamelCase convention)
        class_name = ''.join(word.capitalize() for word in test_case_name.split('_'))
        # print(class_name)
        # Add 'Test' to the class name
        class_name += 'Test'
        # print(class_name)
        # Import the module dynamically
        # module = importlib.import_module('CommonImportsPkg.common_imports')
        module = importlib.import_module('CommonImportsPkg.common_imports')

        # print(module)
        # Get the class from the module
        # print(getattr(module, class_name))
        return getattr(module, class_name)



    def setup_routes(self):
        @self.app.route('/')
        def index():
            test_cases = self.get_test_cases()
            return render_template('index.html', test_cases=test_cases)

        @self.app.route('/run_tests', methods=['POST'])
        def run_tests():
            if request.method == 'POST':
                file_path = request.form['file_path']
                test_case_name = request.form['test_case']
                # print(file_path)
                if file_path:
                    with open(file_path, 'r') as json_file:
                        self.data = json.load(json_file)
                        # print(self.data)
                    # self.data = json.loads(request.form['data'])
                    # print(self.data)
                    if self.data and test_case_name:
                        # point_of_sale = PointOfSaleTest(data=self.data)
                        # park_bill = ParkBillTest(data=self.data)
                        # suite_pos = unittest.TestSuite([point_of_sale_test, park_bill_test, cash_management_test, sales_history_test, add_brand_test])
                        # suite_pos = unittest.TestSuite([point_of_sale, park_bill])
                        #
                        # runner = HTMLTestRunner(descriptions=True, report_title="CWCloud Unittest Results")
                        # result = runner.run(suite_pos)

                        test_class = self.get_test_class(test_case_name)
                        test_instance = test_class(data=self.data)

                        suite = unittest.TestSuite([test_instance])
                        runner = HTMLTestRunner(descriptions=True, report_title="CWCloud Unittest Results")
                        result = runner.run(suite)

                        if result.wasSuccessful():
                            flash("All Tests passed Successfully", "success")
                            return render_template("index.html")
                            # return jsonify({"status": "success", "message": "All tests passed successfully!"})
                        else:
                            flash("Some tests failed. Please check the console for details.", "error")
                            return render_template("index.html")
                            # return jsonify({"status": "error", "message": "Some tests failed. Please check the console for details."})
                    else:
                        flash("Please first select a JSON file!", )
                        return render_template("index.html")
                        # return jsonify({"status": "error", "message": "Please first select a JSON file!"})

        # @self.app.route('/get_test_case_data', methods=['POST'])
        # def get_test_case_data():
        #     if request.method == 'POST':
        #         test_case_name = request.form['test_case']
        #         # Assuming your JSON files are stored in a directory named 'test_data'
        #         # file_path = f'test_data/{test_case_name.lower()}.json'
        #         file_path = 'testdata.json'
        #         try:
        #             with open(file_path, 'r') as json_file:
        #                 data = json.load(json_file)
        #                 # print(data)
        #             return jsonify({'status': 'success', 'data': data})
        #         except FileNotFoundError:
        #             return jsonify({'status': 'error', 'message': 'JSON file not found'})


app = Flask(__name__)
app.secret_key = 'This is secret key for test platform.'
my_app = TestAutomationApp(app)

if __name__ == "__main__":
    app.run(debug=True)
