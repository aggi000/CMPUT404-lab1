import requests
url = "https://raw.githubusercontent.com/aggi000/CMPUT404-lab1/main/test.py"
res = requests.get(url)
print(res.text)