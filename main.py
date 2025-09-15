import os
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
CORS(app)

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    print("OpenAI client initialized successfully.")
except Exception as e:
    print(f" Error initializing OpenAI client: {e}")
    exit()

@app.route('/api/ask', methods=['POST'])
def ask_question():
    """
    Handles incoming questions, sends them to OpenAI, and returns the AI's response.
    Can handle both text-only and multi-modal (text + image) requests.
    """
    print("\n" + "="*50)
    print(" Received a new request...")

    data = request.json
    if not data or 'prompt' not in data:
        print(" Error: Request is missing a 'prompt'.")
        return jsonify({"error": "Prompt is missing"}), 400

    user_prompt = data['prompt']
    image_data_url = data.get('image_data_url')
    
    print(f" User Prompt: '{user_prompt}'")

    try:
        system_prompt = {
            "role": "system",
            "content": "You are Formgenie, a helpful assistant for filling out complex government forms in India. Your answers should be simple, clear, and trustworthy. When explaining a term, provide a concise definition and an actionable next step for the user."
        }
        if image_data_url:
            print(" Image data detected! Using the vision model (gpt-4-vision-preview).")
            user_content = [
                {"type": "text", "text": user_prompt},
                {"type": "image_url", "image_url": {"url": image_data_url}}
            ]
            model_to_use = "gpt-4-vision-preview"
        else:
            print(" Text-only request. Using the standard model (gpt-4-turbo).")
            user_content = user_prompt
            model_to_use = "gpt-4-turbo"

        messages = [
            system_prompt,
            {"role": "user", "content": user_content}
        ]
        
        print(" Calling OpenAI API...")
        response = client.chat.completions.create(
            model=model_to_use,
            messages=messages,
            max_tokens=300 
        )
        
        ai_response = response.choices[0].message.content
        print(" Successfully received response from  AI.")
        
        return jsonify({"answer": ai_response})

    except Exception as e:
        print(f" An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
