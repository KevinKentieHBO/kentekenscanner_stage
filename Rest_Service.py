import requests

def getjSON():
    response = requests.get("http://localhost:8080/betaaltarief")
    print(response.json())