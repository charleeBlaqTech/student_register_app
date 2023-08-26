from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

@app.route('/')
def index_render():
    return render_template('index.html')











if __name__ == "__main__":
    app.debug= True
    app.run(host="localhost", port= 3030)