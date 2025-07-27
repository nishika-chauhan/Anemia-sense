from flask import Flask, render_template, request
import pickle 

app = Flask(__name__)

model = pickle.load(open('final.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    gender = request.form['gender']
    hb = float(request.form['hb'])
    mch = float(request.form['mch'])
    mchc = float(request.form['mchc'])
    mcv = float(request.form['mcv'])

    if gender.lower() == 'female':
            gender_encoded = 1
    else:
            gender_encoded = 0

     # Make prediction using model
    prediction = model.predict([[gender_encoded, hb, mch, mchc, mcv]])

    if prediction[0] == 1:
        result = 'You have anemic disease'
    else:
        result = 'You do not have anemic disease'

    return render_template('predict.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)

