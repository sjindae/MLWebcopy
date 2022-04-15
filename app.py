from flask import Flask,render_template,request
import os,pickle
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':    # 이게 몰까유?
    app.run(debug=True)