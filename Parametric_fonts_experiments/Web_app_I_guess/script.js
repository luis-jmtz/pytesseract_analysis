// Get elements from the DOM
const textElement = document.getElementById("text");
const weightSlider = document.getElementById("weight");
const widthSlider = document.getElementById("width");
const yopqSlider = document.getElementById("yopq");

// Function to update the font styles dynamically
function updateFontStyles() {
  const weight = weightSlider.value;
  const width = widthSlider.value;
  const yopq = yopqSlider.value;

  textElement.style.fontVariationSettings = `
    "wght" ${weight},
    "wdth" ${width},
    "YOPQ" ${yopq}
  `;
}

// Attach event listeners to sliders
weightSlider.addEventListener("input", updateFontStyles);
widthSlider.addEventListener("input", updateFontStyles);
yopqSlider.addEventListener("input", updateFontStyles);

// Initialize default styles
updateFontStyles();
