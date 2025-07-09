from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Your actual SerpAPI key
SERPAPI_API_KEY = "f5171aeb2ddbe049941ca3378e07f67c63255539a504b42c85d5cdc22ee1f3db"

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    return get_serpapi_result(msg)

def get_serpapi_result(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "engine": "google"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "organic_results" in data and data["organic_results"]:
        top_result = data["organic_results"][0]
        title = top_result.get("title", "No title")
        link = top_result.get("link", "#")
        snippet = top_result.get("snippet", "No description")
        return f"<b>{title}</b><br>{snippet}<br><a href='{link}' target='_blank'>{link}</a>"
    else:
        return "No results found."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # allow deployment platform to set port
    app.run(host="0.0.0.0", port=port, debug=True)  # bind to public interface
