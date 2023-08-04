import streamlit as st

def ask_question(question):
    # Logic to generate responses based on the question
    # You can use your OpenAI API key here to make API calls and get responses
    
    # Return a list of options as the response
    options = ['Option 1', 'Option 2', 'Option 3']
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
