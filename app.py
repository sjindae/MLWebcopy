from flask import Flask,render_template,request
import os,pickle
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mnist',methods=['GET','POST'])
def mnist():
    if request.method == 'GET':
        return render_template('mnistform.html')
    else:
        f = request.files['mnistfile']
        path = os.path.dirname(__file__)+'/upload/'+f.filename
        f.save(path)
        img = Image.open(path).convert('L')
        img = np.resize(img,(1,784))
        mpath = os.path.dirname(__file__)+'/model1.pickle'
        with open(mpath, 'rb') as f:
            model = pickle.load(f)
        pred = model.predict(img)
        return render_template('mnistresult.html',data=pred)




if __name__ == '__main__':    # 이게 몰까유?
    app.run(debug=True)