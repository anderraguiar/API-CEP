from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Olá, mundo!"), 200

@app.route('/senai', methods=['GET'])
def senai():
    return jsonify(message="Olá, turma python com framework!"), 200

# endpoint - pesquisar endereço através do cep, retorna em fomato json
@app.route('/pesquisacep/<cep>', methods=['GET'])
def pesquisacep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    return resposta.json()

# endpoint - retorna a previsão do tempo 
@app.route('/tempo', methods=['GET', 'POST'])
def tempo():
    key = "c4380707dde242f4b78202712252204"
    cidade = "Presidente Prudente"
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={cidade}&lang=pt"
    resposta = requests.get(url)
    result = resposta.json()
    #return resposta.json()

    temperatura = result['current']['temp_c']
    umidade = result['current']['humidity']
    velocidade_vento = result['current']['vis_km']
    pressao_atm = result['current']['pressure_mb']
    regiao = result['location']['region']
    time_local = result['location']['localtime']

    return render_template("monitoramento.html", 
    temperatura=temperatura, 
    umidade=umidade,
    pressure_mb=pressao_atm,
    region=regiao,
    localtime=time_local,
    vis_km=velocidade_vento)

    
    



if __name__ == '__main__':
    app.run(debug=True)
