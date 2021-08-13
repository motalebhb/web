// slider-area start
$(document).ready(function($){
   $('.slider_area').slick({
      //  dots: true,
       arrows: false,
       autoplay: true,
       autoplaySpeed: 2000
   }) 
});

// slider-area end

// main csv datatable start

$(document).ready(function () {
    var table = $("#example").DataTable({
      dom: "Bfrtip",
      text: "Export",
      buttons: ["excelHtml5", "csvHtml5"],
    });
  });
 
//  main csv datatable end