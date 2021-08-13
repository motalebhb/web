// city-count-table start
$(document).ready(function () {
    var table = $("#city_count_table").DataTable({
      dom: "Bfrtip",
      text: "Export",
      buttons: ["excelHtml5", "csvHtml5"],
    });
  });
// city-count-table end


// city-code-count-table start

$(document).ready(function () {
  var table = $("#city_code_count_table").DataTable({
    dom: "Bfrtip",
    text: "Export",
    buttons: ["excelHtml5", "csvHtml5"],
  });
});

// city-code-count-table start