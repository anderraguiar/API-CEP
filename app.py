from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)


#funcao
def get_tempo(cidade):
    key = "c4380707dde242f4b78202712252204"
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={cidade}&lang=pt"
    result = requests.get(url).json()
    return {"temperatura":result['current']['temp_c'], 
            "umidade":result['current']['humidity'], 
            "velocidade_vento":result['current']['vis_km'], 
            "pressao_atm":result['current']['pressure_mb'], 
            "regiao":result['location']['region'], 
            "time_local":result['location']['localtime']}


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Olá, mundo!"), 200

@app.route('/senai', methods=['GET'])
def senai():
    return jsonify(message="Olá, turma python com framework!"), 200

# endpoint - pesquisar endereço através do cep, retorna em fomato json
@app.route('/pesquisacep', methods=['GET', 'POST'])
def pesquisacep():
    if request.method == 'GET':
        return render_template("cep.html")

    elif request.method == "POST":
        cep = request.form['cep']
        url = f'https://viacep.com.br/ws/{cep}/json/'
        resposta = requests.get(url).json()
        return render_template("cep.html", **resposta)

# endpoint - retorna a previsão do tempo 
@app.route('/tempo', methods=['GET', 'POST'])
def tempo():
    opcoes = [
        "Sao Paulo",
        "Rio de Janeiro",
        "Belo Horizonte",
        "Curitiba",
        "Recife",
        "Presidente Prudente",
        "Sandovalina"
    ]

    if request.method == 'GET':
        result = get_tempo("São Paulo")
        return render_template("monitoramento.html", **result, opcoes=opcoes)

    elif request.method == 'POST':
        cidade = request.form['cidade']
        result = get_tempo(cidade)
        return render_template("monitoramento.html", **result, opcoes=opcoes, selecionado=cidade)


    
    



if __name__ == '__main__':
    app.run(debug=True)
