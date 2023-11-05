// script.js

function calculatePercentage() {
    // Get selected values from the HTML elements
    const outcome = document.getElementById("outcome").value;
    const race = document.getElementById("race").value;
    const sex = document.getElementById("sex").value;
    const percentile = document.getElementById("rowNumber").value;

    // Prepare the data to send to the Flask backend
    const data = {
        outcome: outcome,
        race: race,
        sex: sex,
        percentile: percentile
    };

    // Make an AJAX request to the Flask backend
    fetch("http://localhost:8000/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        // Update the result on the HTML page
        document.getElementById("result").textContent = `Result: ${data.result}`;
    })
    .catch(error => {
        // Handle errors
        console.error("Error:", error);
        document.getElementById("result").textContent = "Error calculating percentage.";
    });
    
}

// Update the displayed row number value when the slider changes
const rowNumberSlider = document.getElementById("rowNumber");
const rowNumberValue = document.getElementById("rowNumberValue");

rowNumberSlider.addEventListener("input", () => {
    rowNumberValue.textContent = rowNumberSlider.value;
});
