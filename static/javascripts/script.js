document.getElementById('test_case').addEventListener('change', function() {
  var selectedTestCase = this.value;
  var selectedFileName = document.getElementById('file_path').value.split('\\').pop(); // Extracting file name from file path
  if (selectedTestCase !== '') {
    // Make an AJAX request to the Flask backend to get data for the selected test case
    fetch('/get_data/' + selectedTestCase + '?file_name=' + selectedFileName)
      .then(response => response.json())
      .then(data => {
        // Update the modal content with input elements for the data
        modalContent = ''
        for (var key in data) {
          modalContent += '<div class="form-group">';
          modalContent += '<label for="' + key + '">' + key + ':</label>';
          modalContent += '<input type="text" class="form-control" id="' + key + '" name="' + key + '" value="' + data[key] + '">';
          modalContent += '</div>';

        }
        document.getElementById('testCaseDetails').innerHTML = modalContent;


        //Update the modal title with the test case name
        document.getElementById('myModalTitle').textContent = 'Test Case Details: ' + selectedTestCase.toUpperCase();

        // Show the modal
        $('#myModal').modal('show');
      })
      .catch(error => console.error('Error:', error));
  }
});
