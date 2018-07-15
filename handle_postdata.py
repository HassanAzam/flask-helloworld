from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

#   {
#        "x": 10
#        "y": 12
#   }
@app.route("/addnums", methods=["POST"])
def add_nums():
    # get json posted data from request object
    data = request.get_json()

    if "x" not in data or "y" not in data:
        return "Error, post data missing!", 400

    x = data["x"]
    y= data["y"]

    z = x+y

    retJson = {
        "z": z
    }

    return jsonify(retJson), 200

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000)