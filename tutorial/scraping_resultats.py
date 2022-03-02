import requests

url = "https://www.matchendirect.fr/resultat-foot-01-03-2022/"
html_output_name = input('Name for html file: ')

req = requests.get(url, 'html.parser')

with open(html_output_name, 'w') as f:
    f.write(req.text)
    f.close()


