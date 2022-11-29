
from flask import Flask,jsonify,request,render_template
from project_app.utils import MedicalInsurance

import config

app = Flask(__name__)


@app.route("/")  
def hello_flask():
    return render_template("user.html")
    
@app.route("/result", methods= ['POST','GET'])

def get_insurance_charges():
    if request.method == "POST":
        res = request.form
        age  = res["Age"]
        sex  = res["Sex"]
        bmi  = res["Bmi"]
        children = res["Children"]
        smoker = res["Smoker"]
        region = res["Region"]

        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charge = med_ins.get_predict_charges()

        # return jsonify({"Return" : f"Predicted medical isurance charges are :{charge}"})
        return render_template("result.html", charge= charge)
        

app.run()