from flask import Flask, jsonify
import requests
import json
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="test",
  database="tokaimura"
)

@app.route("/")
def test():
    myconn = mydb.cursor();
    myconn.execute("Select * from twitter_jp")
    result = myconn.fetchall()
    return jsonify(result)
    
@app.route("/twitter")
def twitter():
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=official_JAPC&count=10"

    payload={}
    headers = {
      'Authorization': 'OAuth oauth_consumer_key="2heiEgeSUeLsEukxvwGJuS2OI",oauth_token="1392741513478606850-qOT2FpE19VkH7pfJ15nOF6H4xryBAM",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1621476325",oauth_nonce="RuiVqzuEfHN",oauth_version="1.0",oauth_signature="iaF3EOhLTZAsGA5FvcLDdfkvfHU%3D"',
      'Cookie': 'guest_id=v1%3A162147351949996385; personalization_id="v1_4JWwxgH5evBtd8XhVg9a9g=="; lang=ja'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return (data[0]["id_str"])
@app.route("/electric")
def electric():
      return "0"
if __name__ == "__main__":
      app.run(debug=True)

