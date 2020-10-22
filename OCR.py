import requests
 
url = "https://api.aiforthai.in.th/ocr-id-front-iapp"
 
files = {'uploadfile':open('⁨/Users/pawanee/Desktop/Card_id.jpg', 'rb')}
 
headers = {
    'Apikey': "sOfhlcELXnWcqauYcr9pEgCsCO7k1UNK",
    }
 
response = requests.post(url, files=files, headers=headers)
print(response.json())