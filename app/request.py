import requests

# API endpoint URL
url = 'http://localhost:8080/predict_api'

# Input SMS
sms = {
    'sms': 'Congratulations! You have won a free trip to the Bahamas. Reply to claim your prize.'
}
# sms = {
#     'sms': 'Congratulations! You deserve it.'
# }
response = requests.post(url, json=sms)

print(response.json())