import requests

# Faz a requisição de upload para o servidor
url = 'http://localhost:5000/upload'
files = {'file': open('imagens.zip', 'rb')}
response = requests.post(url, files=files)

# Imprime a resposta do servidor
print(response.text)