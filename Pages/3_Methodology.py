# Set up and run this Streamlit App
import streamlit as st

from logics.customer_query_handler import process_user_message

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Methodology"
)

st.markdown("# Methodology 💡")

st.sidebar.markdown("# Methodology 💡")

st.write(
    """
This page is to explain the implementation details and data flows for each use case, accompanied by flow charts illustrating the process flow. 
""")

st.markdown("<h1 style='font-size:24px;'>Data Pre-processing</h1>", unsafe_allow_html=True)

st.write(
    """
This flowchart illustrates the data pre-processing steps for the CPF LIFE Payouts dataset.
Online search from CPF website to get the latest information on CPF LIFE policy. These information are then stored in HTML and CSV file for further processing.
Langchain recursive function is used to extract and parse the information and store it in a JSON file.
""")

st.image(r"C:\Users\cruise\Documents\streamlit_projects\Project_folder\Data\Pre-processing_data.jpg", width=400)

st.markdown("<h1 style='font-size:24px;'>Use Case 1 - In-app Operation </h1>", unsafe_allow_html=True)

st.write(
    """
This flowchart illustrates the operation of the virtual assistant in the CPF LIFE policy page.
User would input the question in the text area and the virtual assistant would and provide the answer based on the information stored in the JSON file.
""")

st.image(r"C:\Users\cruise\Documents\streamlit_projects\Project_folder\Data\In_App_Process.jpg", use_column_width=True)

st.markdown("<h1 style='font-size:24px;'>Use Case 2 - In-app Operation </h1>", unsafe_allow_html=True)

st.write(
    """
Desired CPF LIFE Payouts page allows user to select the desired monthly payout at 50, 55 and 65 and display the CPF savings needed.
Information is stored in the CSV file and displayed as a graph from the dropdown list.
""")

# endregion <--------- Streamlit App Configuration --------->