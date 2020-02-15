# Returns list of gasoline related data fields in EIA dataset
import requests

url = "http://api.eia.gov/search/?search_term=name&search_value=\"gasoline\"&API KEY=0f657729691830a2731d0ab5459670df"

payload = {}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'api_key': ''
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

