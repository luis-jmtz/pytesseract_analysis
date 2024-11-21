// Define the font variation settings with their ranges and default values
const fontSettings = [
    { name: "wght", min: 100, max: 1000, default: 400 }, // Weight
    { name: "wdth", min: 50, max: 200, default: 100 },  // Width
    { name: "slnt", min: -15, max: 0, default: 0 },     // Slant
    { name: "opsz", min: 8, max: 144, default: 12 },    // Optical size
  ];
  
  // Get the controls container and text output element
  const controlsContainer = document.getElementById("controls");
  const textOutput = document.getElementById("text-output");
  
  // Generate sliders and inputs for each font setting
  fontSettings.forEach((setting) => {
    const controlGroup = document.createElement("div");
    controlGroup.className = "control-group";
  
    // Create a label
    const label = document.createElement("label");
    label.textContent = `${setting.name.toUpperCase()}`;
  
    // Create a range slider
    const slider = document.createElement("input");
    slider.type = "range";
    slider.min = setting.min;
    slider.max = setting.max;
    slider.value = setting.default;
    slider.step = 1;
    slider.dataset.name = setting.name;
  
    // Create a number input
    const numberInput = document.createElement("input");
    numberInput.type = "number";
    numberInput.min = setting.min;
    numberInput.max = setting.max;
    numberInput.value = setting.default;
    numberInput.dataset.name = setting.name;
  
    // Sync slider and number input
    slider.addEventListener("input", () => {
      numberInput.value = slider.value;
      updateFontSettings();
    });
  
    numberInput.addEventListener("input", () => {
      slider.value = numberInput.value;
      updateFontSettings();
    });
  
    // Append elements to the control group
    controlGroup.appendChild(label);
    controlGroup.appendChild(slider);
    controlGroup.appendChild(numberInput);
    controlsContainer.appendChild(controlGroup);
  });
  
  // Update the font-variation-settings dynamically
  function updateFontSettings() {
    const settings = Array.from(
      document.querySelectorAll(".control-group input[type=range]")
    )
      .map((slider) => `"${slider.dataset.name}" ${slider.value}`)
      .join(", ");
    textOutput.style.fontFamily = "'Roboto Flex', sans-serif"; // Ensure font family is applied
    textOutput.style.fontVariationSettings = settings;        // Apply dynamic settings
  }
  
  // Initialize with default settings
  updateFontSettings();
  