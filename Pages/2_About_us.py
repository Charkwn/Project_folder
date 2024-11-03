# Set up and run this Streamlit App
import streamlit as st

from logics.customer_query_handler import process_user_message

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About us"
)

st.markdown("# About Us 🚀")

st.sidebar.markdown("# About Us 🚀")

st.write(
    """
This page provides details on the project scope, objectives of the project, data sources used, and features of the app.
""")

st.markdown("<h1 style='font-size:24px;'>Project Scope</h1>", unsafe_allow_html=True)

st.write(
    """
This prototype web-based application serves is capstone project for the AI Champions Bootcamp (Jul 2024 - Oct 2024). 
The application is designed to provide information on CPF LIFE policy to citizens by providing a virtual assistance 
to answer queries and display a chart on the required CPF savings to achieve the desired monthly payout from CPF LIFE. 
""")

st.markdown("<h1 style='font-size:24px;'>Objective</h1>", unsafe_allow_html=True)

st.write(
    """
Virtual assistance to answer questions on CPF LIFE for citizens by using the most recent information available in CPF website.
""")

st.markdown("<h1 style='font-size:24px;'>Data Sources</h1>", unsafe_allow_html=True)

st.write(
    """    
CPF Websites
https://www.cpf.gov.sg/member/infohub/educational-resources/key-facts-of-cpf-life-you-should-know
https://www.cpf.gov.sg/member/infohub/educational-resources/what-are-the-benefits-of-cpf-life
https://www.cpf.gov.sg/member/infohub/educational-resources/how-to-plan-your-desired-retirement-with-cpf-life
""")

st.markdown("<h1 style='font-size:24px;'>Features</h1>", unsafe_allow_html=True)

st.write(
    """
Use Case 1 (Main page) display a virtual assistant to answer questions on CPF Life policy.
Use Case 2 (Payout page) display a selectable chart to display the CPF savings required at 50, 55 and 60 based on the desired monthly payouts. 

"""
)

# endregion <--------- Streamlit App Configuration --------->