from CommonImportsPkg.common_imports import *



class TestAutomationApp:
    def __init__(self, app):
        self.app = app
        self.setup_routes()


    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/run_tests', methods=['POST'])
        def run_tests():
            if request.method == 'POST':
                file_path = request.form['file_path']
                # print(file_path)
                if file_path:
                    with open(file_path, 'r') as json_file:
                        self.data = json.load(json_file)
                        # print(self.data)
                    # self.data = json.loads(request.form['data'])
                    # print(self.data)
                    if self.data:
                        point_of_sale_test = PointOfSaleTest(data=self.data)
                        park_bill_test = ParkBillTest(data=self.data)
                        cash_management_test = CashManagementTest(data=self.data)
                        sales_history_test = SalesHistoryTest(data=self.data)
                        close_till_test = CloseTillTest(data=self.data)
                        add_brand_test = AddBrandTest(data=self.data)
                        add_business_unit_test = AddBusinessUnitTest(data=self.data)
                        add_customers_test = AddCustomersTest(data=self.data)
                        add_email_templates_test = AddEmailTemplatesTest(data=self.data)
                        add_image_library_test = AddImageLibraryTest(data=self.data)
                        add_pos_orders_test = AddPOSOrdersTest(data=self.data)
                        add_pricing_rules_test = AddPricingRulesTest(data=self.data)
                        add_product_catalogue_test = AddProductCatalogueTest(data=self.data)
                        add_product_category_test = AddProductCategoryTest(data=self.data)
                        add_products_test = AddProductsTest(data=self.data)
                        add_return_reasons_test = AddReturnReasonsTest(data=self.data)
                        add_rfid_tag_test = AddRFIDTagTest(data=self.data)
                        add_storage_location_test = AddStorageLocationTest(data=self.data)
                        add_supplier_category_test = AddSupplierCategoryTest(data=self.data)
                        add_supplier_test = AddSupplierTest(data=self.data)
                        add_tax_category_test = AddTaxCategoryTest(data=self.data)
                        add_tax_test = AddTaxTest(data=self.data)
                        add_till_test = AddTillTest(data=self.data)
                        add_user_test = AddUserTest(data=self.data)
                        amount_wise_nob_report_test = AmountWiseNOBReportTest(data=self.data)
                        current_stock_report_test = CurrentStockReportTest(data=self.data)
                        daily_sales_report_test = DailySalesReportTest(data=self.data)


                        # suite_pos = unittest.TestSuite([point_of_sale_test, park_bill_test, cash_management_test, sales_history_test, add_brand_test])
                        suite_pos = unittest.TestSuite([sales_history_test])

                        runner = HTMLTestRunner(descriptions=True, report_title="CWCloud Unittest Results")
                        result = runner.run(suite_pos)

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




app = Flask(__name__)
app.secret_key = 'This is secret key for test platform'
my_app = TestAutomationApp(app)


if __name__ == "__main__":
    app.run(debug=True)
