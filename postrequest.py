import requests
import json

if __name__ == "__main__":

    url = 'http://10.177.191.56:5005/postrequest'
    myobj = {'Test':'hello'}

    x = requests.post(url, data = json.dumps(myobj))

    print(x.text)