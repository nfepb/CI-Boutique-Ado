// Get value of country field on page load and store in variable
let countrySelected = $("#id_default_country").val();
// Empty var if not selected --> if not selected, display in color:
if (!countrySelected) {
  $("#id_default_country").css("color", "#aab7c4");
}
// Capture change event every time box change, capture value & determine color
$("#id_default_country").change(function () {
  countrySelected = $(this).val();
  if (!countrySelected) {
    $(this).css("color", "#aab7c4");
  } else {
    $(this).css("color", "#000");
  }
});
