from flask import Flask, render_template, request
import openai
import os

openai.api_key = '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'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI developed by OpenAI, functioning as a Tax Resolution Expert. You provide guidance on the IRS Fresh Start Program. Once you have the necessary information, you will inform the client that our Case Manager, Sami, will be calling them shortly. Sami can be reached directly at Sami@freshstarttaxco.com or 858-649-9433 during office hours (9 AM to 5 PM EST, Monday through Friday)."},
            {"role": "user", "content": message}
        ]
    )
    response_text = response['choices'][0]['message']['content']

    # Split the response into sentences and join them without bullet points
    response_sentences = response_text.split('. ')
    response_text = ' '.join([f'{sentence}' for sentence in response_sentences if sentence])

    return response_text

if __name__ == '__main__':
    app.run(debug=True)
