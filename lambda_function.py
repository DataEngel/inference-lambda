from joblib import load

import warnings
warnings.filterwarnings('ignore')

payload = {
    '5008807': [65, 0, 1, 10000, 1]
}

def lambda_handler(event, context):
    my_model = load('./model_risk.joblib')
    result = my_model.predict([payload['5008807']]) 
    print(result)


lambda_handler(payload, context=None)