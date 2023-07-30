from flask import Flask, request
from flask import jsonify
import openai
from prompts import get_character_prompt

app = Flask(__name__)

@app.route('/chat')
def chat():
    conversation = request.get_json().get('conversation', [])

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

    print('___________')
    # Send the AI's message back to the frontend
    return jsonify({"response": ai_message, })

if __name__ == '__main__':
    app.run(debug=True)
