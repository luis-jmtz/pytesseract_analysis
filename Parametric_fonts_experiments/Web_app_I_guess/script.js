// Get elements for each axis from the DOM
const textElement = document.getElementById("text");

// Map each input ID to its respective axis name
const inputs = {
  weight: "wght",
  width: "wdth",
  slant: "slnt",
  grade: "GRAD",
  figureHeight: "YTLC", // YTLC stands for Figure Height in Roboto Flex
};

// Function to update font variation settings dynamically
function updateFontStyles() {
  const settings = Object.entries(inputs)
    .map(([id, axis]) => {
      const value = document.getElementById(id).value;
      return `"${axis}" ${value}`;
    })
    .join(", ");

  textElement.style.fontVariationSettings = settings;
}

// Add event listeners to all input fields
Object.keys(inputs).forEach((id) => {
  document.getElementById(id).addEventListener("input", updateFontStyles);
});

// Initialize default styles
updateFontStyles();
