from flask import Flask, render_template, request, jsonify
import openai
import os

# Set your API key (safely)
openai.api_key = os.environ.get("sk-proj-awwf2wnLXzs7PVU-fUX02HSHlzgiG8k8-Dh42tkYEiaxhQJylkNIvK-gkVB3X5Er0AgwKV8BBST3BlbkFJV1yNUeEtAEfm5awIl-X6DzVwdxb9XqQHHxxvVIhN9fhhYNRvGkTasciMwS85XE92FAMRZeWjIAY")  # store in environment variable

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    return get_chat_response(msg)

def get_chat_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful and friendly assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )

        reply = response["choices"][0]["message"]["content"].strip()
        return reply

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
