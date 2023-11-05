

function calculatePercentage() {
    // Get input values from the HTML form
    const rowNumber = parseInt(document.getElementById("rowNumber").value);
    const outcome = document.getElementById("outcome").value;
    const race = document.getElementById("race").value;
    const sex = document.getElementById("sex").value;

    // Call the calculatePercentage function
    calculatePercentageFromCSV(rowNumber, outcome, race, sex, (err, result) => {
        if (err) {
            // Display error message
            document.getElementById("result").innerHTML = "Error: " + err.message;
        } else {
            // Display the result
            document.getElementById("result").innerHTML = "Result: " + result;
        }
    });
}

function calculatePercentageFromCSV(rowNumber, outcome, race, sex, callback) {
    // Replace 'national_percentile_outcomes.csv' with the actual path to your CSV file
    const filePath = 'national_percentile_outcomes.csv';

    const fs = require('fs');
    const parse = require('csv-parse');

    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            return callback(err);
        }

        parse(data, {
            columns: true,
            trim: true,
        }, (err, records) => {
            if (err) {
                return callback(err);
            }

            // Find the corresponding column name based on outcome, race, and sex
            const columnName = `${outcome}_${race}_${sex}`;

            // Find the record at the specified row number
            const record = records[rowNumber - 1];

            if (!record) {
                return callback(new Error(`Row number ${rowNumber} does not exist.`));
            }

            // Get the value from the specified column
            const percentage = record[columnName];

            if (percentage === undefined) {
                return callback(new Error(`Column ${columnName} not found.`));
            }

            callback(null, percentage);
        });
    });
}
