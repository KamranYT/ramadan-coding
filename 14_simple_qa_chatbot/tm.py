import google.generativeai as genai 
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Main caht loop
while True:
    # Get user input from terminal
    user_input = input("\nEnter your message: (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Thanks for chatting! Goodbye!")
        break
    
    # Generate response using user's input
    response = model.generate_content(user_input)

    # Print the response
    print(response.text)