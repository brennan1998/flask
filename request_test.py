import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-key': "7406ce2570msh2cdf4c78aab3a28p12fc39jsn3be65634f33e",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)