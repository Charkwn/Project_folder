# Set up and run this Streamlit App
import streamlit as st
from utility import check_password

from logics.customer_query_handler import process_user_message

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Welcome!"
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()
    
# endregion <--------- Streamlit App Configuration --------->

st.markdown("# Main page 🎈")

st.markdown("<h1 style='font-size:24px;'>Domain #3: Understanding CPF LIFE Policy</h1>", unsafe_allow_html=True)

form = st.form(key="form")
form.subheader("Welcome to the homepage")

user_prompt = form.text_area("Ask a question on CPF LIFE, such as 'Tell me about CPF LIFE' ", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
    print(f"User Input is {user_prompt}")


st.sidebar.markdown("# Main page 🎈")

st.write(
    """

    
    
IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.

"""
)