# we build a simple web application with python Flask webframework
# first of all, we must install flask package on your python environment
# pip install flask

# secondly, we also should install the package jsonify
# pip install jsonify

# we import the essnetional packages
from flask import Flask
from flask import jsonify

# init and APP
app = Flask(__name__)

@app.route('/', methods=['GET'])

def get():
    return jsonify({'msg':'Hello, Python Flask REST API web application!,\
                    Week 6 Demo!'})

# run our web application
if __name__ == '__main__':
    app.run(debug=True)