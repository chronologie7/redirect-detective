import requests, re
from sys import argv

def validate_url(url):    
    patron = re.compile(
        r'^https?://'
        r'([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
        r'(:\d+)?'
        r'(/[-a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=]*)?'
        r'(\?[-a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=]*)?'
        r'(#[-a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=]*)?$'
    )
    return bool(patron.match(url))

if len(argv) != 2:
    print("error: no correct arguments")
    exit(1)

url = argv[1]

if validate_url(url) == False:
    print("URL no valida")
    exit(1)

print(f"initial URL => {url}")
while True:
    response = requests.get(url, allow_redirects=False)
    if response.status_code >= 300 and response.status_code <=399:
        location = response.headers["location"]
        print(f"{response.status_code} - redirect to => {location}")
        url = location
    else:
        print(f"{response.status_code} - final destination => {url}")
        break
exit(0)
