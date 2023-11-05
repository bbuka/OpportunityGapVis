import pandas as pd

# Reading a CSV file
df = pd.read_csv('national_percentile_outcomes.csv')





# Replace this function with your actual Python method
def calculate_percentage(outcome, race, gender, percentile):
    return df.at[percentile - 1, f"{outcome}_{race}_{gender}"]


