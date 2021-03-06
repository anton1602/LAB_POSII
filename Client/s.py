from flask import Flask, render_template, request
import os
import requests
from run_client import predict
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		
		input1 = request.form['input1']
		input2 = request.form['input2']
		input3 = request.form['input3']
		input4 = request.form['input4']
		input5 = request.form['input5']
		input6 = request.form['input6']
		input7 = request.form['input7']
		input8 = request.form['input8']
		input9 = request.form['input9']
		input10 = request.form['input10']
		input11 = request.form['input11']
		input12 = request.form['input12']
		input13 = request.form['input13']
		result = predict({'age': input1, 'sex': input2, 'cp': input3, 'trestbps': input4, 'chol': input5, 'fbs': input6, 'restecg': input7, 'thalach': input8, 'exang': input9, 'oldpeak': input10, 'slope': input11, 'ca': input12, 'thal': input13})
		print(result)
		if float(result) == 0:
			result = "Heart disease -"
		else:
			result = "Heart disease +"
	else:
		result = 'ya slomalsya'
	return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
