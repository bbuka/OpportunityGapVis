from flask import Flask, render_template, request, jsonify
import pandas as pd
from flask_cors import CORS
#import os

app = Flask(__name__)
CORS(app)


# Reading a CSV file
df = pd.read_csv('national_percentile_outcomes.csv')

# Get the absolute path to the CSV file
#csv_file_path = os.path.abspath('national_percentile_outcomes.csv')
#df = pd.read_csv(csv_file_path)

# Replace this function with your actual Python method

def calculate_percentage(outcome, race, gender, percentile):
    return df.at[percentile - 1, f"{outcome}_{race}_{gender}"]
    #return "Goodbye World!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    outcome = data['outcome']
    race = data['race']
    sex = data['sex']
    percentile = int(data['percentile'])

    # Call the Python function from your file
    result = calculate_percentage(outcome, race, sex, percentile)

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
