var slider = document.getElementById("myRange");
var output = document.getElementById("range_output_hw");
output.innerHTML = slider.value;
slider.oninput = function() {
  output.innerHTML = this.value;
}