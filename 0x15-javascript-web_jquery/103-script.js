$(document).ready(function () {
    $('INPUT#btn_translate').click(translate);

    $('INPUT#language_code').focus(function () {
        // Attach a keydown event handler to the input field
        $(this).keydown(function (e) {
            // Check if the Enter key (keyCode 13) is pressed
            if (e.keyCode === 13) {
                translate();
            }
        });
    });
});

function translate () {
    const url = 'https://www.fourtonfish.com/hellosalut/?';

    // Send a GET request to the API with the language code as a parameter
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        // Update the content of the element with ID "hello" with the translated text
        $('DIV#hello').html(data.hello);
    });
}
