import streamlit as st
import pandas as pd
import plotly.express as px
from utility import check_password

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Desired CPF Life Payouts"
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()
    
# endregion <--------- Streamlit App Configuration --------->

st.markdown("# Desired CPF LIFE Payouts 💰")

# Load data from CSV file
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load the data
data_file = 'C:/Users/cruise/Documents/streamlit_projects/Project_folder/Data/CPF_LIFE_payouts.csv'
df = load_data(data_file)

# Display the data in Streamlit
#st.title("CPF Life Premium and Savings Needed at Different Ages")
#st.write(df)

# Sidebar for Desired Payouts
st.sidebar.markdown("# Desired Payouts 💰")

# Streamlit UI for selecting a payout
desired_payout = st.selectbox(
    "Select Desired Monthly Payout from Age 65:",
    options=df["Desired Monthly Payout from 65"].unique()
)

# Filter the DataFrame for the selected payout
selected_row = df[df["Desired Monthly Payout from 65"] == desired_payout].iloc[0]

# Prepare data for plotting
plot_data = pd.DataFrame({
    "Age": ["55", "60", "65"],
    "Savings Needed": [
        selected_row["Savings You Need at 55"],
        selected_row["Savings You Need at 60"],
        selected_row["CPF LIFE Premium at 65 (Savings You Need at 65)"]
    ]
})

# Create a Plotly bar chart
fig = px.bar(
    plot_data, x="Age", y="Savings Needed", 
    title=f"Savings Needed for Desired Monthly Payout: {desired_payout}",
    labels={"Savings Needed": "Savings Needed (SGD)", "Age": "Age"}
)

# Display chart
st.plotly_chart(fig)
