import pickle
from flask import Flask
from flask import request
from flask import jsonify
 
model_file = 'model1.bin'
dv_file = 'dv.bin'
 
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)
 
app = Flask('churn')
 
@app.route('/predict', methods=['POST'])
def predict():
    # json = Python dictionary
    customer = request.get_json()
 
    X = dv.transform([customer])
    model.predict_proba(X)
    y_pred = model.predict_proba(X)[0,1] 
    churn = y_pred >= 0.5
 
    result = {
        # the next line raises an error so we need to change it
        #'churn_probability': y_pred,
        'subscribe_probability': float(y_pred),
        # the next line raises an error so we need to change it
        #'churn': churn
        'churn': bool(churn)
    }
 
    return jsonify(result) 
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)