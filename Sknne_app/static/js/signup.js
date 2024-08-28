const signup_form = document.getElementById('signup_form')
const first_name = document.getElementById('first_name')
const first_name_error = document.getElementById('first_name_error')
const last_name = document.getElementById('last_name')
const last_name_error = document.getElementById('last_name_error')
const email = document.getElementById('email')
const email_error = document.getElementById('email_error')
const password = document.getElementById('password')
const password_error = document.getElementById('password_error')
const confirm_password = document.getElementById('confirm_password')
const confirm_password_error = document.getElementById('confirm_password_error')
const number = document.getElementById('number')
const number_error = document.getElementById('number_error')
const login_email = document.getElementById('pxp-signin-email')
const login_email_error = document.getElementById('login_email_error')
const login_password = document.getElementById('pxp-signin-pass')
const login_password_error = document.getElementById('login_password_error')
const msg = document.getElementById('msg')
/*signup_form.addEventListener('submit', (x) => {
    var email_check = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (first_name.value == '' || first_name.value == null) {
        x.preventDefault()
        first_name_error.innerHTML = "Enter a First Name"
    }
    else {
        first_name_error.innerHTML = null
    }
    if (last_name.value == '' || last_name.value == null) {
        x.preventDefault()
        last_name_error.innerHTML = "Enter a Last Name"
    }
    else {
        last_name_error.innerHTML = null
    }
    if (!email.value.match(email_check)) {
        x.preventDefault();
        email_error.innerHTML = "Valid Email is required";
    }
    else {
        email_error.innerHTML = null;
    }
    if (password.value == '' || password.value == null) {
        password_error.innerHTML = "Password cant be empty"
    }
    else if (password.value.length != 0 && password.value.length < 8) {
        x.preventDefault();
        password_error.innerHTML = 'Password should be 8 characters at least '
    }
    else {
        password_error.innerHTML = null;
    }
})*/
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
    $("#login_form").on('submit', function (event) {
        var email_check = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        });
        $.ajax({
            type: 'POST',
            url: '/front_validation',
            data: {
                login_email: $("#login_email").val(),
                login_password: $('#login_password').val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
        if (login_password.value == '' || login_password.value == null) {
            event.preventDefault()
            login_password_error.innerHTML = "Password Field Can not be Empty";
        }
        else {
            login_password_error.innerHTML = null;
        }
        if (login_email.value == '' || login_email.value == null) {
            event.preventDefault();
            login_email_error.innerHTML = "Email field can not be empty"
        }
        else {
            login_email_error.innerHTML = null;
        }
    })
});

$(document).ready(function () {
    $("#signup_form").on('input', function (event) {
        var email_check = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        });
        $.ajax({
            type: 'POST',
            url: '/front_validation',
            data: {
                first_name: $("#first_name").val(),
                last_name: $("#last_name").val(),
                email: $("#email").val(),
                number: $("#number").val(),
                password: $('#password').val(),
                confirm_password: $("#confirm_password").val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
        if (first_name.value.length != 0 && first_name.value.length < 2) {
            event.preventDefault();
            first_name_error.innerHTML = "2 characters at least"
        }
        else {
            first_name_error.innerHTML = null;
        }
        if (last_name.value.length != 0 && last_name.value.length < 2) {
            event.preventDefault();
            last_name_error.innerHTML = "2 characters at least"
        }
        else {
            last_name_error.innerHTML = null;
        }
        if (email.value == '') {
            email_error.innerHTML = null;
        }
        else if (email.value != '' && !email.value.match(email_check)) {
            event.preventDefault();
            email_error.innerHTML = "Valid Email is required";
        }
        else {
            email_error.innerHTML = null;
        }
        if (password.value.length != 0 && password.value.length < 8) {
            event.preventDefault();
            password_error.innerHTML = "Password should be 8 characters at least"
        }
        else {
            password_error.innerHTML = null;
        }
        if (confirm_password.value.length != 0 && confirm_password.value != password.value) {
            event.preventDefault();
            confirm_password_error.innerHTML = "Passwords do not match"
            confirm_password_error.style.color = "red"
        }
        else if (confirm_password.value == password.value && confirm_password.value.length != 0) {
            confirm_password_error.innerHTML = "Passwords Match"
            confirm_password_error.style.color = "green"
        }
        if (number.value.length != 0 && number.value.length < 10 || number.value.length > 10) {
            event.preventDefault();
            number_error.innerHTML = "Enter a valid number starting with 05*****"
        }
        else if (number.value.length == 10) {
            number_error.innerHTML = null
        }
        console.log(number_error.innerHTML)
        if (first_name.value != "" && last_name.value != "" && email.value != "" && password.value != "" && confirm_password.value != "" && number.value != "" && first_name_error.innerHTML == "" && last_name_error.innerHTML == "" && email_error.innerHTML == "" && password_error.innerHTML == "" && number_error.innerHTML == "") {
            signup_btn.style.display = "block"
        }
        else {
            signup_btn.style.display = "none"
        }
    })
});



/*document.querySelector("#signupForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    // Example AJAX call (using fetch API)
    fetch('/signup', {
        method: 'POST',
        body: new FormData(this)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            // Show SweetAlert if there's an error
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: data.error_message,
                confirmButtonText: 'Try Again'
            });
        } else {
            // Redirect or show success message if signup is successful
            Swal.fire({
                icon: 'success',
                title: 'Success!',
                text: 'You have been registered successfully!',
                confirmButtonText: 'Proceed'
            }).then(() => {
                window.location.href = '/dashboard'; // Redirect to another page
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Something went wrong!',
            confirmButtonText: 'Try Again'
        });
    });
});*/

/*document.querySelector("#loginform").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission

    // Example AJAX call (using fetch API)
    fetch('/login', {
        method: 'POST',
        body: new FormData(this)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            // Show SweetAlert if there's an error
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: data.error_message,
                confirmButtonText: 'Try Again'
            });
        } else {
            // Redirect or show success message if signup is successful
            Swal.fire({
                icon: 'success',
                title: 'Success!',
                text: 'You have been registered successfully!',
                confirmButtonText: 'Proceed'
            }).then(() => {
                window.location.href = '/dashboard'; // Redirect to another page
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Something went wrong!',
            confirmButtonText: 'Try Again'
        });
    });
});*/
/*$(document).ready(function () {
    $("#signup_form").on('input', function (event) {
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCSRFToken()
            }
        });
        $.ajax({
            type: 'POST',
            url: '/signup',
            data: {
                first_name: $("#first_name").val(),
                last_name: $("#last_name").val(),
                email: $("#email").val(),
                number: $("#number").val(),
                password: $('#password').val(),
                confirm_password: $("#confirm_password").val(),
                message : $('message').val(),
                csrfmiddlewaretoke: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        })
    })
});*/
// function initMap() {
//     let map;
//     var locations = {{ locations| safe}};
// var infoWindow = [];
// map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: locations[0].latitude, lng: locations[0].longitude },
//     zoom: 12
// })
// locations.forEach(function (location) {
//     var marker = new google.maps.Marker({
//         position: { lat: location.latitude, lng: location.longitude },
//         map: map,
//         title: location.name
//     })
//     var infowindow = new google.maps.InfoWindow({
//         content: location.name
//     });
//     infoWindow.push(infowindow);
//     marker.addListener('click', function () {
//         infoWindow.forEach(function (iw) {
//             iw.close();
//         });
//         infowindow.open(map, marker);
//     });
// });
// }
// window.initMap = initMap

// "use strict";

// !function () {
//     var t = window.driftt = window.drift = window.driftt || [];
//     if (!t.init) {
//         if (t.invoked) return void (window.console && console.error && console.error("Drift snippet included twice."));
//         t.invoked = !0, t.methods = ["identify", "config", "track", "reset", "debug", "show", "ping", "page", "hide", "off", "on"],
//             t.factory = function (e) {
//                 return function () {
//                     var n = Array.prototype.slice.call(arguments);
//                     return n.unshift(e), t.push(n), t;
//                 };
//             }
//     } ();
//     drift.SNIPPET_VERSION = '0.3.1';
//     drift.load('g6s3dpwhnudz');
// }
// $(document).ready(function() {
//     $('.fa-star').on('click', function() {
//         var rating = $(this).prev().val();
//         $('.fa-star').removeClass('checked');
//         $(this).prevAll().addBack().addClass('checked');
//         $.ajax({
//             type: 'POST',
//             url: '{% url "submit_rating" %}',
//             data: {
//                 // 'appartment_id': $('#appartment_id').val(),
//                 'rating': $('#rating').val(),
//                 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
//             },
//             success: function(response) {
//                 console.log('Rating submitted successfully.');
//             },
//             error: function(xhr, status, error) {
//                 console.log('Error: ' + error);
//             }
//         });
//     });
// });
