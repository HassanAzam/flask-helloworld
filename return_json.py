from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    jsonObject = {
        "id": "007",
        "name": "James Bond"
    }
    return jsonify(jsonObject)

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)