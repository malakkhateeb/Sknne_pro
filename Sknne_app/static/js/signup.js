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
        if (email.value == ''){
            email_error.innerHTML = null;
        }
        else if (email.value != '' && !email.value.match(email_check)) {
            event.preventDefault();
            email_error.innerHTML = "Valid Email is required";
        }
        else{
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
        else if (number.value.length == 10){
            number_error.innerHTML = null
        }
        console.log(number_error.innerHTML)
        if(first_name.value != "" && last_name.value != "" && email.value != "" && password.value != "" && confirm_password.value != "" && number.value != "" && first_name_error.innerHTML == "" && last_name_error.innerHTML == "" && email_error.innerHTML == "" && password_error.innerHTML == "" && number_error.innerHTML == "" ){
            signup_btn.style.display = "block"
        }
        else{
            signup_btn.style.display = "none"
        }
    })
});
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