import pandas as pd

def process_csv(row_number, race, sex, outcomes):
    # Load the CSV file
    df = pd.read_csv('national_percentile_outcomes.csv')  # Replace 'your_file.csv' with the actual filename

    # Create a new DataFrame to store the processed data
    new_data = pd.DataFrame(columns=['source', 'target', 'value'])

    for outcome in outcomes:
        # Create column names based on the given inputs
        col_name_race_sex = f'{outcome}_{race}_{sex}'
        col_name_pooled_race = f'{outcome}_pooled_{sex}'
        col_name_pooled_sex = f'{outcome}_{race}_pooled'
        col_name_given_sex_race = f'{outcome}_{race}_{sex}'

        # Calculate values based on the given conditions
        value_race_sex = abs(df.at[row_number + 1, col_name_race_sex] - df.at[row_number + 1, col_name_pooled_race])
        value_race_sex = round(value_race_sex, 3) if not pd.isna(value_race_sex) else 0

        value_sex_pooled = abs(df.at[row_number + 1, col_name_race_sex] - df.at[row_number + 1, col_name_pooled_sex])
        value_sex_pooled = round(value_sex_pooled, 3) if not pd.isna(value_sex_pooled) else 0

        value_given_sex_race = abs(df.at[row_number + 1, col_name_race_sex] - df.at[50, col_name_given_sex_race])
        value_given_sex_race = value_given_sex_race if not pd.isna(value_given_sex_race) else 0

        total = value_race_sex + value_sex_pooled + value_given_sex_race


        # Add rows to the new data DataFrame
        new_data = new_data.append({'source': race, 'target': outcome, 'value': value_race_sex/total}, ignore_index=True)
        new_data = new_data.append({'source': sex, 'target': outcome, 'value': value_sex_pooled/total}, ignore_index=True)
        new_data = new_data.append({'source': str(row_number), 'target': outcome, 'value': value_given_sex_race/total},
                                   ignore_index=True)

    # Save the processed data to a new CSV file
    new_data.to_csv('processed_data.csv', index=False)

if __name__ == "__main__":
    # Example usage
    row_number = 25  # Replace with the desired row number
    race = 'black'  # Replace with the desired race
    sex = 'male'    # Replace with the desired sex
    outcomes = ['coll', "jail", "kfr"]  # Replace with the desired outcome names

    process_csv(row_number, race, sex, outcomes)
