from flask import Flask, render_template, redirect, url_for, request
import requests
import json

app = Flask(__name__)

@app.route("/")
@app.route("/recommend/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/recommendation", methods=["POST", "GET"])
def recommendation():
    if request.method == "POST":
        anime_name = request.form["anime_name"]
        return redirect(url_for("anime", anime_name=anime_name))
    else:
        return render_template("index.html")

@app.route("/recommend/<anime_name>")
def anime(anime_name):
    api_url = "http://54.164.159.198/anime_recommendation"
    data = {"anime_name": anime_name}
    
    response = requests.post(api_url, json=data)
    status = response.json()["status"]
    if status == "ok":
        recommendation_data = response.json()["message"]
        return render_template("recommendation.html", data=recommendation_data)
    else:
        return render_template("error.html")

@app.route("/ref")
def ref():
    return render_template("ref.html")

@app.route("/temp-map-2018")
def temp_map_2018():
    return render_template("temp_map_2018.html")

@app.route("/top-studio-2018")
def top_studio_2018():
    return render_template("top_studio_2018.html")

@app.route("/user-nature-2018")
def user_nature_2018():
    return render_template("user_nature_2018.html")

@app.route("/top-rated-2018")
def top_rated_2018():
    return render_template("top_rated_anime_2018.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
