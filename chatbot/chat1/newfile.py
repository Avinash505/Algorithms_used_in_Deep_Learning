import csv
import pinecone
from flask import Flask, render_template, request

# Initialize Flask application
app = Flask(__name__)

# Initialize Pinecone index
pinecone.init(api_key='69ae8292-055f-4eeb-81e4-e511db2392b9')
index_name = 'real_estate_index'
def generate_response(user_input):
    # Implement your chatbot logic to generate a response
    response = "This is a placeholder response."
    return response

def extract_property_preferences(user_input):
    # Implement your logic to extract property preferences from the user input
    property_preferences = {
        'min_price': 0,
        'max_price': float('inf'),
        'min_area': 0,
        'max_area': float('inf'),
        'bedrooms': None,
        'location': None,
        'city': None
    }
    
    # Extract property preferences based on the user input
    # ...

    return property_preferences

# Function to encode property listings as vectors
def encode_property(property_data):
    # Encode property data into a vector using your preferred method
    encoded_vector = ['price', 'area', 'bedrooms']
    return encoded_vector

# Function to add property listings to the Pinecone index
def add_property_to_index(property_id, property_data):
    encoded_vector = encode_property(property_data)
    pinecone.Index(index_name).upsert([{ 'id': property_id, 'vector': encoded_vector }])

# Function to perform similarity search using Pinecone
def search_similar_properties(query_vector, top_k=5):
    result = pinecone.Index(index_name).query(query_vector, top_k=top_k)
    return result.ids

# Load property listings from a CSV file
def load_property_listings(csv_file):
    property_listings = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            property_listings.append(row)
    return property_listings

# Load property listings from CSV
property_listings = load_property_listings('/home/codetrade/Downloads/Y/chatbot/chat1/Indian_House_Prices.csv')

# Add property listings to the Pinecone index
for idx, property_data in enumerate(property_listings):
    property_id = str(idx)
    add_property_to_index(property_id, property_data)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user input and display chatbot response
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    # Perform any preprocessing or validation on user input if needed

    # Pass user input to the chatbot for generating response
    response = generate_response(user_input)

    # Extract property preferences from user input if needed
    property_preferences = extract_property_preferences(user_input)

    # Encode property preferences as vector using Langchain
    preferences_vector = encode_property(property_preferences)

    # Perform similarity search with Pinecone
    similar_properties = search_similar_properties(preferences_vector)

    # Render the chat template with the response and similar properties
    return render_template('chat.html', response=response, similar_properties=similar_properties)

if __name__ == '__main__':
    app.run(debug=True)
