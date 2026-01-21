import google.generativeai as genai
import os

# Initialize with the provided API Key
# Note: In a production environment, it's best practice to use environment variables.
API_KEY = "AIzaSyC4bu5G3Y2HvvFL__Buvat-T0bzqf4EKV0"
genai.configure(api_key=API_KEY)

def main():
    try:
        # Initialize the model (using an available model from the list)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Make a basic prompt
        prompt = "Hello, write a collection of 3 haikus about coding."
        print(f"Prompt: {prompt}\n")
        
        # Generate content
        response = model.generate_content(prompt)
        
        # Print the output
        print("Response:")
        print(response.text)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
