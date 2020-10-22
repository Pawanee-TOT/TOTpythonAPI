import requests
 
url = "https://api.aiforthai.in.th/ssense"
 
text = 'สาขานี้พนักงานน่ารักให้บริการดี'
 
params = {'text':text}
 
headers = {
    'Apikey': "sOfhlcELXnWcqauYcr9pEgCsCO7k1UNK"
    }
 
response = requests.get(url, headers=headers, params=params)
 
print(response.json())