import requests

api_endpoint = 'http://localhost:8000/predict'

input_text = "This is a good job for you. Trust me...."

payload = {"text": input_text}
response = requests.post(api_endpoint, json=payload)

if response.status_code == 200:
    print(response.json())
else:
    print("Prediction failed")



 