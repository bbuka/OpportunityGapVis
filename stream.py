import pandas as pd
import streamlit as st

df = pd.read_csv('national_percentile_outcomes.csv')

def calculate_percentage(outcome, race, gender, percentile):
    try:
        return df.at[percentile - 1, f"{outcome}_{race}_{gender}"]
    except KeyError:
        return "Data Not Available"

# Mapping for dropdown options and descriptions
outcome_options = {"College": {"value": "coll", "description": "Completing College"},
                   "Jail": {"value": "jail", "description": "Being In Jail at age 30"},
                   "Income": {"value": "kfr", "description": "Household Income Percentile"},
                   "Married": {"value": "married", "description": "Being Married at age 30"},
                   "Public Assistance": {"value": "proginc", "description": "Receiving Public Assistance Income"},
                   'Teen Birth': {"value": "teenbrth", "description": "having and claiming a child between 13 and 19"}}
race_options = {"Asian": "asian", "Black": "black", "White": "white", "Native American": "natam", "Hispanic": "hisp", "Other": "other"}
sex_options = {"Male": "male", "Female": "female"}

# Check if the session_state variable exists
if "first_load" not in st.session_state:
    st.session_state.first_load = True

#Title
st.title("The Student Opportunity Gap")

# Header
if st.session_state.first_load:
    st.session_state.first_load = False  # Set the flag to False after the first load
    welcome_message = """
        <div style="text-align: left;">
            <p>Welcome to the Opportunities Explorer! Here are some quick pointers:</p>
            <ul>
                <li>This tool generates a value based on several factors that you give it</li>
                <li>To create a child, please select a race, a sex, and choose their parents' income percentile</li>
                <li>A percentage will be returned representing the expected chance that your chosen outcome will occur</li>
            </ul>
            <p>Click 'Okay' to continue.</p>
        </div>
    """
    st.markdown(welcome_message, unsafe_allow_html=True)
    st.button("Okay")

# Title
#st.title("The Opportunity Gap")

# Dropdowns
outcome = st.selectbox("Outcome", list(outcome_options.keys()))
# Display outcome description
#st.write(f"**Outcome Description:** {outcome_options[outcome]['description']}")

race = st.selectbox("Race", list(race_options.keys()))
sex = st.selectbox("Sex", list(sex_options.keys()))

# Slider
selected_value_slider = st.slider("Parental Income", 1, 100, 50)

# Button to Trigger Calculation
if st.button("Calculate"):
    # Call the calculation function with mapped values
    result = calculate_percentage(
        outcome_options[outcome]["value"], race_options[race], sex_options[sex], selected_value_slider
    )

    # Format the result as a percentage within a message
    formatted_result = f"The predicted probability of your individual {outcome_options[outcome]['description'].lower()} is: {result:.2%}" if result != "Data Not Available" else "Data Not Available"
    if outcome == "Income":
        formatted_result = f"Your individual is expected to be in the {result:.2%} percentile of income"


    
    # Display the result in a larger box
    st.markdown(f'<div style="font-size: 18px; padding: 20px; border: 1px solid #ccc; border-radius: 5px; text-align: center; margin-top: 20px; background-color: #193929; color: #DFFDE9;">{formatted_result}</div>', unsafe_allow_html=True)
    #st.success(formatted_result)
