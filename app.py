"""
The main app
"""
from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from prompts import get_character_prompt


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """
    Hello world test endpoint
    """
    return "hello world"

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """
    This function handles the /chat endpoint, which is called by the frontend to send a message to the AI.
    """
    print('/chat called')
    conversation = request.get_json().get('conversation', [])
    print(conversation)

    # If the conversation is more than 20 messages long, keep only the first and last 10
    if len(conversation) > 20:
        conversation = conversation[:10] + conversation[-10:]

    # Create a list of messages for the OpenAI API, mapping 'human' to 'user' and 'ai' to 'assistant'
    messages = [{"role": "user" if message['sender'] == "human" else "assistant", 
                 "content": message['text']} for message in conversation]

    # Add a system message at the beginning of the conversation
    character_prompt = get_character_prompt()
    messages.insert(0, {"role": "system", "content": character_prompt})

    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        max_tokens=150,
    )

    # Extract the AI's message from the response
    ai_message = response['choices'][0]['message']['content']

    # Send the AI's message back to the frontend
    return jsonify({"response": ai_message, })

if __name__ == '__main__':
    app.run(debug=True)
