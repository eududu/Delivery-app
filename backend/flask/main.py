from flask import Flask
import requests

app = Flask(__name__)

@app.route("/<int:cep>")
def hello_world(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if response.status_code == 200:
        x = response.json()
        return "R$ 1" if x['uf'] == "CE" else float('inf')
    else:
        return "cep não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
