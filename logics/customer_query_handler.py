import json
from helper_functions import llm
import os
import pandas as pd

cpf_life_info = {
    'Plans': ['Standard Plan', 'Basic Plan', 'Escalating Plan'],
    'Benefits': ['Retirement income', 'Payouts'],
    'Payouts': ['Monthly payouts', 'Payout start age', 'Payout duration'],
    'Premiums': ['Premium amount', 'Premium payment period'],
    'Others': ['Withdrawal conditions', 'Nomination']
}

# Load the JSON file
filepath = './data/CPFLife_data.json'
with open(filepath, 'r', encoding='utf-8') as file:
    json_string = file.read()
    dict_of_info = json.loads(json_string)

#This function identifies relevant categories and information from a user message related to CPF LIFE.
def identify_category_and_info(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to the subject on CPF LIFE or any specific information
    in the Python dictionary below, where each key is a `category`
    and the value is a list of `info`.

    If there are any relevant info(s) found, output the pair(s) of a) `info` the relevant information and b) the associated `category` into a
    list of dictionary object, where each item in the list is a relevant info
    and each info is a dictionary that contains two keys:
    1) category
    2) info

    {cpf_life_info}

    If no relevant information is found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    category_and_info_response_str = llm.get_completion_by_messages(messages)
    category_and_info_response_str = category_and_info_response_str.replace("'", "\"")
    category_and_info_response = json.loads(category_and_info_response_str)
    return category_and_info_response
    
#This function retrieves the information details based on the relevant categories and information.
def get_info_details(list_of_relevant_category_n_info: list[dict]):
    info_list = []
    for x in list_of_relevant_category_n_info:
        info_list.append(x['info']) # x["info"]

    list_of_info_details = []
    for info in info_list:
        list_of_info_details.append(dict_of_info.get(info))
    return list_of_info_details

#This function generates a response based on the information details.
def generate_response_based_on_info_details(user_message, info_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about CPF LIFE, \
    understand the relevant information from the following list.
    All available information shown in the json data below:
    {info_details}

    Step 2:{delimiter} Use the information about CPF LIFE to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the CPF LIFE information.
    Your response should be as detailed as possible and \
    include information that is useful for the customer to better understand CPF LIFE.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    customers to make their decision.
    Complete with details such as eligibility, payouts, and premiums.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer

#This function processes the user message and returns the response.
def process_user_message(user_input):

    # Process 1: If relevant information is found, look it up
    category_n_info = identify_category_and_info(user_input)
    print("category_n_info : ", category_n_info)

    # Process 2: Get the Information Details
    info_details = get_info_details(category_n_info)

    # Process 3: Generate Response based on Information Details
    reply = generate_response_based_on_info_details(user_input, info_details)

    # Process 4: Append the response to the list of all messages
    return reply
