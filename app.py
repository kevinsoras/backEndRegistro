from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_cors import CORS, cross_origin
from json import dumps

app = Flask(__name__)
CORS(app)
cors=CORS(app,resources={
    r"/*":{
        "origins":"*"

    }
})

@app.route('/',methods=['POST'])
def agregarinteresado():
    return request.json


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)