import openai
from flask import Flask, request, jsonify, send_file
from openai import OpenAI
import os

api_key = os.environ.get('OPENAI_API_KEY')
app = Flask(__name__)
openai.api_key = api_key
client = OpenAI()

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.json
    humor_prompt = data['prompt'] + "\nMake it humorous:"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a witty AI."
            },
            {
                "role": "user",
                "content": humor_prompt
            },
        ],
        max_tokens=50
    )

    # 提取回应内容
    message = response.choices[0].message.content

    return jsonify({"message": message})

if __name__ == '__main__':
    app.run()