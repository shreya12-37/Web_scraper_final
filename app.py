from flask import Flask, request, make_response, jsonify, send_from_directory , send_file
from flask_cors import CORS ,cross_origin
import subprocess
import requests
from bs4 import BeautifulSoup
import csv
from summary import reviewScraper
configs = {
    "ORIGINS": [
        "http://localhost:3000/",
        "http://127.0.0.1:3000/",
        "https://review-scraper-app.herokuapp.com",
        "*"
    ],
    "SECRET_KEY": "Hello World",
}
app = Flask(__name__)
app.secret_key = configs['SECRET_KEY']
CORS(app, supports_credentials=True)
app.config["CLIENT_CSV"] = "H:/Web/Projects/Review Scrapper/Review-Scraper-Project"
@app.route("/download-csv-file", methods=["GET"])
def scrape():
    data = request.args.to_dict()
    url = data["url"]
    pages = data["pages"]
    res = reviewScraper(url, pages)
    print(pages,"\n")
    return jsonify(msg=res)



@app.route("/download-summary", methods=["GET"])
def summary():
    data = request.args.to_dict()
    my_url = data["url"]
    r = requests.get(my_url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, "html.parser")
    product_title = soup.find(class_=["a-text-ellipsis"]).get_text()
    overall_rating = soup.find(class_=["averageStarRating"]).get_text()
    global_rating_reviews = (
        soup.find(class_=["a-row a-spacing-base a-size-base"]).get_text().strip()
    )
    five_star = soup.find(class_=["5star"])["title"]
    four_star = soup.find(class_=["4star"])["title"]
    three_star = soup.find(class_=["3star"])["title"]
    two_star = soup.find(class_=["2star"])["title"]
    one_star = soup.find(class_=["1star"])["title"]

    summary = {
        "product name": product_title,
        "overall rating": overall_rating,
        "number of global reviews and ratings": global_rating_reviews,
        "five stars": five_star,
        "four stars": four_star,
        "three stars": three_star,
        "two stars": two_star,
        "one stars": one_star,
    }
    response = jsonify(message=summary)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


if __name__ == "__main__":
    app.run(debug=True)
