from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_api():
    url = "https://meme.breakingbranches.tech/api?limit=15&type=dank"
    response = json.loads(requests.get(url).text)
    title = [meme["title"] for meme in response["memes"]]
    url = [meme["url"] for meme in response["memes"]]
    return title, url

def get_years():
    years = ['2020', '2021', '2022', '2023']
    return years

@app.route("/")
@app.route("/index")
def index():
    years = get_years()
    title, url = get_api()
    return render_template("index.html", years=years, title=title, url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
