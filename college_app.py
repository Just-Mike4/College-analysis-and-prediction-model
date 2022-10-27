from flask import Flask, request, jsonify, render_template 
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)

model=pickle.load(open("college_std.pkl","rb"))

@app.route("/")
def home():
          return render_template("app.html")


@app.route("/predict",methods=["POST"])
def predict():
          value=request.form.to_dict()
          values=[list(value.values())]
          print(values)
          prediction=model.predict(values)
          return render_template("app.html",prediction_text = "You will stay in school {}".format(prediction))

if __name__=="__main__":
          app.run(debug=True)