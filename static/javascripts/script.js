document.getElementById('test_case').addEventListener('change', function() {
  var selectedTestCase = this.value;
  var selectedFileName = document.getElementById('file_path').value.split('\\').pop(); // Extracting file name from file path
//  var selectedFileName = document.getElementById('file_path').value; // Extracting file name from file path
  console.log(selectedFileName)
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
          modalContent += '<input type="text" class="form-control" id="' + key + '" name="' + "modal_"+ key + '" value="' + data[key] + '">';
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

function submitForm() {
    const fileInput = document.getElementById('file_path');
    const testCaseSelect = document.getElementById('test_case');
    const formData = new FormData();

    formData.append('file_path', fileInput.files[0]);
    formData.append('test_case', testCaseSelect.value);

    // Add the modal form data to the request body
    const modalInputs = document.querySelectorAll('#testCaseDetails input');
    modalInputs.forEach(input => {
        formData.append(input.id, input.name, input.value);
    });

    // Use AJAX to send the form data to the Flask application
    $.ajax({
        type: 'POST',
        url: '/run_tests',
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            // Handle the response as needed
            console.log(response);
        },
        error: function (error) {
            // Handle errors
            console.error(error);
        }
    });
}



//function submitForm() {
//        const fileInput = document.getElementById('file_path');
//        const testCaseSelect = document.getElementById('test_case');
//        const formData = new FormData();
//
//        // Append file input and test case select values
//        formData.append('file_path', fileInput.files[0]);
//        formData.append('test_case', testCaseSelect.value);
//
//        // Append data from modal form inputs
//        const modalInputs = document.querySelectorAll('#testCaseDetails input');
//        modalInputs.forEach(input => {
//            formData.append(input.id, input.name, input.value);
//            //console.log(formData)
//        });
//
//        // Use AJAX to send the form data to Flask application
//        $.ajax({
//            type: 'POST',
//            url: '/run_tests',
//            data: formData,
//            processData: false,
//            contentType: false,
//            success: function (response) {
//                // Handle the response as needed
//                console.log(response);
//            },
//            error: function (error) {
//                // Handle errors
//                console.error(error);
//            }
//        });
//    }
//
//    // Additional code to handle modal display and form input updates
//    document.getElementById('test_case').addEventListener('change', function () {
//        // Your existing code to update modal content based on the selected test case
//    });
//
//    // Additional code to handle modal dismissal and form input updates
//    $('#myModal').on('hidden.bs.modal', function () {
//        // Your existing code to handle modal dismissal
//    });