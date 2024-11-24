from flask import Flask,render_template,request
import pickle
import numpy as np
import joblib

try:
    model=joblib.load("model.pkl")
    print("Model loaded successfully")
except Exception as e:
    print(f"Some error occured {e}")



app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=['POST'])
def predict():
    try:
        size=float(request.form["size"])
        cup_size=float(request.form["cup-size"])
        bra_size=float(request.form["bra-size"])
        category=float(request.form["category"])
        if category==0:
            cat="Bottoms"
        elif category==1:
            cat="Dress"
        elif category==2:
            cat="New"
        elif category==3:
            cat="Outerwear"
        elif category==4:
            cat="Sale"
        else:
            cat="Weddings"
        length=float(request.form["length"])
        fit=float(request.form["fit"])
        shoe_size=float(request.form["shoe-size"])
        shoe_width=float(request.form["shoe-width"])

        input_arr=np.array([[size,cup_size,bra_size,category,length,fit,shoe_size,shoe_width]])
        prediction=model.predict(input_arr)
        print("prediction:",prediction)
        return render_template(
            "results.html",
            prediction=round(prediction[0], 2),
            category=cat
        )
    except Exception as e:
        return f"Some error occured:{e}"

app.run(debug=True)