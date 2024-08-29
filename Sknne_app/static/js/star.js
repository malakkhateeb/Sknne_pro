$(document).ready(function () {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});
$(document).ready(function () {
    $('input[name="rating"]').on('change', function (e) {
        e.preventDefault(); // Prevents the form from submitting the traditional way
        $.ajax({
            type: 'POST',
            url: '/submit-rating',
            data: {
                rating: $('input[name="rating"]:checked').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function () {
                // Redirect or update the UI on successful submission
                window.location.href = '/room';  // Redirect after successful submission
            },
            error: function (xhr, status, error) {
                console.error('Submission failed:', error);
            }
        });
    });
});
// $(document).ready(function () {
//     $('#form2').on('submit', function (e) {
//         e.preventDefault(); // Prevents the form from submitting the traditional way
//         $.ajax({
//             type: 'POST',
//             url: '/show-distance',
//             data: {
//                 university: $('#university').val(),
//                 transportation: $('#transportation').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
//             },
//             dataType: 'json', // Expect JSON response
//             success: function (response) {
//                 '<%Session["time"]'= response.time,
//                 '<%Session["distance"]'= response.distance,
//             },
//             error: function (xhr, status, error) {
//                 console.error('Submission failed:', status, error);
//                 alert('There was an error submitting the form.');
//             }
//         });
//     });
// });

// $(document).ready(function () {
//     $('#form2').on('submit', function (e) {
//         e.preventDefault(); // Prevents the form from submitting the traditional way

//         $.ajax({
//             type: 'POST',
//             url: '/show-distance',
//             data: {
//                 university: $('#university').val(),
//                 transportation: $('#transportation').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
//             },
//             success: function(response) {
//                 // Assuming 'response' contains the JSON data returned from the server
//                 console.log('Server response:', response);

//                 // Update the HTML content with the new data
//                 $('#distance').text(response.distance);
//                 $('#time').text(response.time);
//             },
//             error: function(xhr, status, error) {
//                 // Handle errors
//                 console.error('Submission failed: ', status, error);
//                 alert('There was an error submitting the form.');
//             }
//         });
//     });
// });
// $(document).ready(function () {
//     $('#form2').on('submit', function (e) {
//         e.preventDefault(); // Prevents the form from submitting the traditional way

//         $.ajax({
//             type: 'POST',
//             url: '/show-distance',
//             data: {
//                 university: $('#university').val(),
//                 transportation: $('#transportation').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
//             },
//             success: function(response) {
//                 // Handle the response from the server
//                 // For example, display a message or redirect
//                 alert('Form submitted successfully!');
//                 // You can also redirect if needed
//                 // window.location.href = '/success-page';
//             },
//             error: function(xhr, status, error) {
//                 // Handle errors
//                 console.error('Submission failed: ', status, error);
//                 alert('There was an error submitting the form.');
//             }
//         });
//     });
// });
// $(document).ready(function () {
//     $('#form2').on('submit', function (e) {
//         e.preventDefault(); // Prevents the form from submitting the traditional way
//         $.ajax({
//             type: 'POST',
//             url:'/show-distance',
//             data: {
//                 university: $('#university').val(),
//                 transportation : $("#transportation").val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
//             },// Redirect after successful submission
//         });
//     });
// });


// // Example usage:
// const pieChart = document.querySelector('.c100.p70');
// updatePieChartColor(pieChart, 70);

// var percentage = document.getElementById('percentage').innerHTML;
// var element = document.getElementById('color');
// element.classList.add('c100 p'+percentage+ 'pink');


// // $(document).ready(function () {
//     $("#star1").on('submit', function (e) {
//         e.preventDefault();
//         $.ajax({
//             type: 'POST',
//             url: '/submit-rating',
//             data: {
//                 rating: $('input[name="rating"]:checked').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
//             },
//             success: function (response) {
//                 // Handle success, e.g., redirect or update UI
//                 window.location.href = '/room';  // Redirect after successful submission
//             },
//             error: function (xhr, status, error) {
//                 // Handle error
//                 console.error('Submission failed:', error);
//             }
//         });
//     });

//     // Submit form when a radio button is clicked
//     $('input[name="rating"]').on('change', function () {
//         $("#star1").submit();
//     });
// });
// $(document).ready(function () {
//     $("#star1").on('submit', function (e)  {
//         e.preventDefault();
//         function getCSRFToken() {
//             return $('meta[name="csrf-token"]').attr('content');
//         }
//         $.ajaxSetup({
//             headers: {
//                 'X-CSRFToken': getCookie('csrftoken'),
//             }
//         });
//         $.ajax({
//             type: 'POST',
//             url: '/submit-rating',
//             data: {
//                 rating: $('input[name="rating"]').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//             },
//         });
//     });
// });

// $(document).ready(function() {
//     $('#star2').on('submit', function(event) {
//         event.preventDefault();
//         function getCSRFToken() {
//             return $('meta[name="csrf-token"]').attr('content');
//         }
//         $.ajaxSetup({
//             headers: {
//                 'X-CSRFToken': getCookie('csrftoken'),
//             }
//         });
//         $.ajax({
//             type: 'POST',
//             url: '/submit-rating',
//             data: {
//                 '<%Session["vote"]' : $('#two').val(),
//                 rating: $('#rate').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//             },
//         });
//     });
// });

// $(document).ready(function() {
//     $('#star3').on('submit', function(event) {
//         event.preventDefault();
//         function getCSRFToken() {
//             return $('meta[name="csrf-token"]').attr('content');
//         }
//         $.ajaxSetup({
//             headers: {
//                 'X-CSRFToken': getCookie('csrftoken'),
//             }
//         });
//         $.ajax({
//             type: 'POST',
//             url: '/submit-rating',
//             data: {
//                 '<%Session["vote"]' : $('#two').val(),
//                 rating: $('#rate').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//             }
//         });
//     });
// });

// $(document).ready(function() {
//     $('#star4').on('submit', function(event) {
//         event.preventDefault();
//         function getCSRFToken() {
//             return $('meta[name="csrf-token"]').attr('content');
//         }
//         $.ajaxSetup({
//             headers: {
//                 'X-CSRFToken': getCookie('csrftoken'),
//             }
//         });
//         $.ajax({
//             type: 'POST',
//             url: '/submit-rating',
//             data: {
//                 '<%Session["vote"]' : $('#two').val(),
//                 rating: $('#rate').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//             },
//         });
//     });
// });
// $(document).ready(function() {
//     $('#star5').on('submit', function(event) {
//         event.preventDefault();
//         function getCSRFToken() {
//             return $('meta[name="csrf-token"]').attr('content');
//         }
//         $.ajaxSetup({
//             headers: {
//                 'X-CSRFToken': getCookie('csrftoken'),
//             }
//         });
//         $.ajax({
//             type: 'POST',
//             url: '/submit-rating',
//             data: {
//                 '<%Session["vote"]' : $('#two').val(),
//                 rating: $('#rate').val(),
//                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
//             },
//         });
//     });
// });

// $(document).ready(function() {
//     $('.fa-star').on('mouseover', function() {
//         var rating = $(this).prev().val();
//         $('.fa-star').removeClass('checked');
//         $(this).prevAll().addBack().addClass('checked');
//     });
// });