from flask import Flask,render_template,request
import pickle

pred = pickle.load(open('kidn.pkl','rb'))
import numpy as np

model = pickle.load(open('kidn.pkl', 'rb'))

app = Flask(__name__)

l = ()
@app.route('/')
def hello():
    return render_template('input2kidnay.html')

@app.route('/info',methods = ['POST'])
def info():
    in1 = request.form['input1']
    in2 = request.form['input2']
    in3 = request.form['input3']
    in4 = request.form['input4']
    in5 = request.form['input5']
    in6 = request.form['input6']
    in7 = request.form['input7']
    in8 = request.form['input8']
    in9 = request.form['input9']
    in10 = request.form['input10']
    in11 = request.form['input11']
    in12 = request.form['input12']
    in13 = request.form['input13']
    in14 = request.form['input14']
    in15 = request.form['input15']
    in16 = request.form['input16']
    in17 = request.form['input17']
    in18 = request.form['input18']
    in19 = request.form['input19']
    in20 = request.form['input20']
    in21 = request.form['input21']
    in22 = request.form['input22']
    in23 = request.form['input23']
    in24 = request.form['input24']
    in25 = request.form['input25']




    arr = np.array([[in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15,in16,in17,in18,in19,in20,in21,in22,in23,in24,in25]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

if __name__ == '__main__':
    app.run(debug=True)