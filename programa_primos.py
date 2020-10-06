import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    primos = "2, "
    lista = []
    acumulador = 0
    numero = 3
    while len(lista) < 99:
        for i in range(1, (numero+1)):
            if numero % i == 0:
                acumulador += 1
        if acumulador == 2:
            primos = primos + str(numero) + ", "
            lista.append(numero)
        acumulador = 0
        numero += 1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
