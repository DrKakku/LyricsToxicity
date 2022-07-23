from flask import render_template,request
from classifyLyric import app
from classifyLyric.lyrics import get_lyrics,beautifyLyrics
import requests as re


@app.route('/')
@app.route('/home')
def home():
    return render_template("homepage.html")


@app.route('/predict',methods=["GET","POST"])
def getData():
    if request.method == "POST":
        form = request.form
        # artist = form["artist"]
        song = form["song"]
        # print(artist)
        lyrics = get_lyrics(song=song)
        lyrics = lyrics.split("Lyrics",maxsplit=1)
        payload = {"data": lyrics[-1] }
        lyrics[-1] = beautifyLyrics(lyrics[-1])
        print(lyrics)
        pred = re.post("http://172.20.40.100:8080/classify",params=payload)
        val = pred.json()['pred']
        return render_template("Prediction.html",pred = val,data = lyrics[0],lyrics=lyrics[-1])