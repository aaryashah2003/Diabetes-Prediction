from flask import *
import random
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import make_column_transformer

app = Flask(__name__,template_folder='templates', static_folder='static')

#loading the model
#model = joblib.load("diabetes.joblib.dat")
model=pickle.load(open("multi.pkl",'rb'))
#xgb_reg =joblib.load("xgb_reg.sav")
#model_xgb_2 = xgb.Booster()
#model_xgb_2.load_model("model.json")




# Landing Page
@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/in_form', methods=['GET', 'POST'])
def get_form():
    return render_template('form.html')

      # features = [np.array(float_....)]
     # prediction = model.form(features)
      # bmi = float[]
    

@app.route('/result', methods=['POST','GET'])
def result():
  if request.method == 'POST':
    name = request.form["name"]
    gender = request.form["gender"]
    age = float(request.form["Age"])  # Convert age to float
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    bpvalue = float(request.form["highBP"])
    cholvalue = float(request.form["highChol"])
    smoker = float(request.form["smoker"])
    stroke = float(request.form["stroke"])
    heart = float(request.form["HeartDiseaseorAttack"])
    physical = float(request.form["PhysActivity"])
    walk = float(request.form["Diffwalk"])
    veggies = float(request.form["Veggies"])
    fruits = float(request.form["Fruits"])
    alcohol = float(request.form["HeavyAlcoholConsumption"])
    genHealth = float(request.form["genHealth"])
    phyHealth = float(request.form["phyHealth"])
    nodoc = float(request.form["nodoc"])  # Get nodoc from form
    diabetes = float(request.form["diabetes"])
    # Create a dictionary for the DataFrame
    data = {
        "gender": gender,
        "age": age,
        "smoker": smoker,
        "bpvalue": bpvalue,
        "diabetes": diabetes,
        "cholvalue": cholvalue,
        "stroke": stroke,
        "physical": physical,
        "fruits": fruits,
        "veggies": veggies,
        "alcohol": alcohol,
        "nodoc": nodoc,
        "walk": walk
    }
    # Create DataFrame from dictionary
    df = pd.DataFrame(data, index=[0])

    X_test_ct = df.to_numpy()
    prediction = model.predict(X_test_ct)
    if prediction == 1:
        txt = "The model says you have Diabetes."
    elif prediction == 2:
        txt = "The model says you have Heart Disease."
    elif prediction == 3:
        txt = "The model says you have Hypertension."
    elif prediction == 0:
        txt = "The model says you are healthy."
    else:
        txt = "The model says you are mad."  # Modify this message as needed
    return render_template('result.html', name=name, features=txt)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8001, debug=True)

