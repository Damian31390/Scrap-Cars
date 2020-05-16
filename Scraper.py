from Core import make_url,allegro_scrap
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/api/<carModel>")
def car_scrap(carModel):
    temp = make_url(carModel)
    return jsonify(allegro_scrap(temp))

if __name__ == "__main__":
    app.run(host='127.10.0.0', port=5000) 