import os

import warnings
warnings.filterwarnings('ignore')

payload = {
    '5008807': [65, 0, 1, 10000, 1]
}

def lambda_handler(event, context):

    cwd = os.getcwd()
    
    print(cwd)


lambda_handler(payload, context=None)