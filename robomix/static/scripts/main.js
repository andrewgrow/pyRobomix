$(".nav .nav-link").on("click", function(){
    $(".nav").find(".active").removeClass("active");
    $(this).addClass("active");
});

$('#top_menu').find('a').bind('click', function(e){
    e.preventDefault();
    var href = $(this).attr('href');
    getAjaxContent(href);
});

$('#welcome').find('a').bind('click', function(e){
    e.preventDefault();
    var href = $(this).attr('href');
    getAjaxContent(href);
});

function getAjaxContent(href) {
    $.ajax({
        url: "/ajax_content",
        type: "get",
        data: {jsdata: href},
        success: function(response) {
        $("#body_content").html(response);
        },
        error: function(xhr) {
            // We may to do something to handle error
        },
        timeout : 1000 //timeout of the ajax call
    });
}

function email() {
    email1='andrew'
    email2='gahov'
    full_address = email1 + "@" + email2 + ".com"
    html_str = "<p>You can contact me via email: <a style='font-size:22px;' href='mailto:" + full_address + "'>" + full_address + "</a></p>"
    $("#email").html(html_str);
}