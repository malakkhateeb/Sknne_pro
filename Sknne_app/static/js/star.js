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
$(document).ready(function() {
    $('#form1').on('click', function(event) {
        event.preventDefault();
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        });
        $.ajax({
            type: 'POST',
            url: '/submit-rating',
            data: {
                '<%Session["vote"]' : $('#two').val(),
                rating: $('#rate').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        });
    });
});

$(document).ready(function() {
    $('#star2').on('submit', function(event) {
        event.preventDefault();
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        });
        $.ajax({
            type: 'POST',
            url: '/submit-rating',
            data: {
                '<%Session["vote"]' : $('#two').val(),
                rating: $('#rate').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        });
    });
});

$(document).ready(function() {
    $('#star3').on('submit', function(event) {
        event.preventDefault();
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        });
        $.ajax({
            type: 'POST',
            url: '/submit-rating',
            data: {
                '<%Session["vote"]' : $('#two').val(),
                rating: $('#rate').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            }
        });
    });
});

$(document).ready(function() {
    $('#star4').on('submit', function(event) {
        event.preventDefault();
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        });
        $.ajax({
            type: 'POST',
            url: '/submit-rating',
            data: {
                '<%Session["vote"]' : $('#two').val(),
                rating: $('#rate').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        });
    });
});
$(document).ready(function() {
    $('#star5').on('submit', function(event) {
        event.preventDefault();
        function getCSRFToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
        $.ajaxSetup({
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        });
        $.ajax({
            type: 'POST',
            url: '/submit-rating',
            data: {
                '<%Session["vote"]' : $('#two').val(),
                rating: $('#rate').val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            },
        });
    });
});

$(document).ready(function() {
    $('.fa-star').on('mouseover', function() {
        var rating = $(this).prev().val();
        $('.fa-star').removeClass('checked');
        $(this).prevAll().addBack().addClass('checked');
    });
});