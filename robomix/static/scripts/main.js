$(".nav .nav-link").on("click", function(){
    $(".nav").find(".active").removeClass("active");
    $(this).addClass("active");
});

$('#top_menu').find('a').bind('click', function(e){
    e.preventDefault();
    var href = $(this).attr('href');

    $.ajax({
      url: "/ajax_content",
      type: "get",
      data: {jsdata: href},
      success: function(response) {
        $("#body_content").html(response);
//        dynamic change link
//        window.history.pushState({"pageTitle":href},"", href);
      },
      error: function(xhr) {
        // We may to do something to handle error
      },
      timeout : 1000 //timeout of the ajax call
    });
});