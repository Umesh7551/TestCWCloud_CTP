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
                # print(request.form)
                # Access modal form data from request.form
                modal_data = {}
                for key in request.form:
                    if key.startswith('modal_'):
                        modal_data[key.replace('modal_', '')] = request.form[key]
                # print(modal_data)

                if file_path:
                    with open(file_path, 'r') as json_file:
                        self.data = json.load(json_file)
                        # print(self.data)

                    if 'test_' + test_case_name in self.data:
                        test_data = self.data['test_' + test_case_name]
                        # print("Test data before updating: ", test_data)
                        # Combine test_data with modal_data
                        test_data.update(modal_data)
                        # print("Test data after updating: ", test_data)
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

        @app.route('/get_data/<test_case>')
        def get_data(test_case):
            # Get the optional 'file_name' parameter from the query string
            file_name = request.args.get('file_name', 'testdata.json')

            # Construct the path to the JSON file based on the provided file name
            json_file_path = os.path.join(os.path.dirname(__file__), file_name)

            if os.path.exists(json_file_path):
                with open(json_file_path, 'r') as json_file:
                    data = json.load(json_file)

                    if 'test_' + test_case in data:
                        return jsonify(data['test_' + test_case])
                    else:
                        return jsonify({'error': 'Test case not found'})
            else:
                return jsonify({'error': 'JSON file not found'})



        # @app.route('/get_data/<test_case>')
        # def get_data(test_case):
        #     # Assuming data.json is in the 'json_data' directory relative to app.py
        #     # json_file_path = os.path.join(os.path.dirname(__file__), 'testdata.json')
        #
        #     # Assuming data.json is a file in the same directory as app.py
        #     with open('testdata.json', 'r') as json_file:
        #     # with open(json_file_path, 'r') as json_file:
        #         data = json.load(json_file)
        #         # print(data)
        #     if 'test_' + test_case in data:
        #         # print(test_case)
        #         test_case = 'test_' + test_case
        #         # print(test_case)
        #
        #         return jsonify(data[test_case])
        #     else:
        #         return jsonify({'error': 'Test case not found'})


        # @app.route('/update_data/<test_case>', methods=['POST'])
        # def update_data(test_case):
        #     # Load existing data from the JSON file
        #     with open('testdata.json', 'r') as json_file:
        #         existing_data = json.load(json_file)
        #         if 'test_' + test_case in existing_data:
        #             test_case = 'test_' + test_case
        #             # Update the data with the submitted form data
        #             form_data = request.get_json()
        #             existing_data[test_case].update(form_data)
        #
        #     # Save the updated data back to the JSON file
        #     with open('testdata.json', 'w') as json_file:
        #         json.dump(existing_data, json_file, indent=2)
        #
        #     # return jsonify({'message': 'Data updated successfully'})
        #     flash("Data updated successfully", "modal_success")
        #     return render_template("index.html")
            # return jsonify({"status": "success", "message": "Data updated successfully"})
            # return jsonify({'message': 'Data updated successfully'})


app = Flask(__name__)
app.secret_key = 'This is secret key for test platform.'
my_app = TestAutomationApp(app)

if __name__ == "__main__":
    app.run(debug=True)
