/* Add this script at the end of your index.html file */
    // Function to fetch JSON data based on the selected test case
    function loadTestData() {
        var test_case = document.getElementById('test_case').value;
//        var file_path = document.getElementById('file_path').value;

        // Send an AJAX request to the server to get the JSON data
        fetch('/get_test_case_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'test_case': test_case,

            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Check if data is an array before using forEach
//                if (Array.isArray(data.data)) {
//                    // Update the form or modal with input elements based on the JSON data
//                    // For simplicity, let's assume there's a function called updateForm() that does this
//                    updateForm(data.data);
//                } else {
//                    alert('Invalid data format. Expected an array.');
//                }
            } else {
                alert('Error fetching test case data: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error fetching test case data:', error);
        });
    }

    // Example function to update the form or modal with input elements based on JSON data
    function updateForm(data) {
        // You can customize this function based on your JSON data structure
        // For simplicity, let's assume data is an array of objects with 'field_name' and 'field_type'
        var form = document.getElementById('dynamic_form');
        form.innerHTML = '';  // Clear existing form elements

        data.forEach(function (field) {
            var inputElement = document.createElement('input');
            inputElement.type = field.field_type;
            inputElement.name = field.field_name;
            // Add additional attributes or properties based on your JSON data
            // ...

            // Append the input element to the form
            form.appendChild(inputElement);
        });

        // Display the form or modal
        // For simplicity, let's assume there's a function called showModal() that does this
        showModal();
    }


