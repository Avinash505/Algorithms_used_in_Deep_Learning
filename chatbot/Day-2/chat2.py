# import streamlit as st
# import langchain
# import pinecone
# import openai

# # Set up OpenAI API credentials
# openai.api_key = "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"

# # Set up LangChain and Pinecone client
# langchain_client = langchain.Client(api_key="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")
# pinecone.init(api_key="d178ddde-a21a-48d1-9cbb-de3ef5e7bcfb", environment="northamerica-northeast1-gcp")

# # Define the question-answering function using GPT-3.5
# def ask_question(question):
#     # Call GPT-3.5 API using OpenAI
#     response = openai.Completion.create(
#         engine="text-davinci-0035",
#         prompt=question,
#         max_tokens=100,
#         n=3,  # Number of options to generate
#         stop=None,
#         temperature=0.7,
#     )

#     # Extract the generated options from the GPT-3.5 response
#     options = [option["choices"][0]["text"].strip() for option in response["choices"]]

#     return options

# # Main function to run the chatbot interface
# def main():
#     st.title("Chatbot with Question Options")
#     # Text input to ask the question
#     question = st.text_input("Ask a question:")
#     if question:
#         # Call the ask_question function to get the response options
#         options = ask_question(question)
        
#         # Display the response options as buttons
#         selected_option = st.selectbox("Select an option:", options)
        
#         # Process the selected option
#         if selected_option:
#             st.write("You selected:", selected_option)
    
# if __name__ == "__main__":
#     main()

import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

# Define the question-answering function using GPT-3.5 Turbo
def ask_question(question):
    # Call GPT-3.5 Turbo API using OpenAI
    response = openai.Completion.create(
        # engine="text-davinci-003",
        model="gpt-3.5-turbo",
        prompt=question,
        max_tokens=100,
        n=3,  # Number of options to generate
        stop=None,
        temperature=0.7,
    )

    # Extract the generated options from the GPT-3.5 Turbo response
    options = [option["choices"][0]["text"].strip() for option in response["choices"]]

    return options

# Main function to run the chatbot interface
def main():
    st.title("Chatbot with Question Options")
    
    # Text input to ask the question
    question = st.text_input("Ask a question:")
    
    if question:
        # Call the ask_question function to get the response options
        options = ask_question(question)
        
        # Display the response options as buttons
        selected_option = st.selectbox("Select an option:", options)
        
        # Process the selected option
        if selected_option:
            st.write("You selected:", selected_option)
    
if __name__ == "__main__":
    main()
