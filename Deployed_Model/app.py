from flask import Flask, request, jsonify
from flask_restful import Api, Resource 
import cloudpickle
import pandas as pd
import numpy as np



app = Flask(__name__)
api = Api(app)

with open('model.clpkl', 'rb') as f:
    model = cloudpickle.load(f)




class Predict(Resource):
    
    def post(self): #post request
        json_data = request.get_json()
        
        df = pd.DataFrame(json_data.values(),index=json_data.keys()).transpose()
        df = df.astype({'ApplicantIncome': np.float64,
                        'CoapplicantIncome': np.float64,
                        'LoanAmount': np.float64,
                        'Loan_Amount_Term': np.float64,
                        'Credit_History': np.float64})
        
        #df = pd.DataFrame(json_data)
        
        result = model.predict(df)
        return result.tolist()


api.add_resource(Predict,'/predict')


if __name__ == '__main__': 
    app.run(debug=True)
