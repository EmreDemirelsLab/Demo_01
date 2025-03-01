# import requests
# response = requests.get("http://www.google.com")
# print(response.text)

import webbrowser
url = 'http://google.com'
webbrowser.get('safari').open_new(url)
