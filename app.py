import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask import request
import openai

openai.api_key = os.getenv("OPENAIKEY")

# Create the app
app = Flask(__name__)

# Add a route
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/question', methods=['POST'])
def question():
    data = request.get_json() # accept json request
    prompt = str(data['question']) # convert json request to string
    
    # communicate with openai

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text

# Run the app
if __name__ == '__main__':
    app.run(port=3000)
