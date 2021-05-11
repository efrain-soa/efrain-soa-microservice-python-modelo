from flask import Flask, jsonify, request


app = Flask(__name__)

import joblib
import numpy as np


# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


    # Create Data Routes
@app.route('/sendSymptom', methods=['POST'])
def sendSymptom():
   
    array = request.json['array']

    clf1= joblib.load('modelo_entredado.pkl')
    
    x=np.array([array])

    prediccion = clf1.predict(x)

    if prediccion == 1:
        recomendacion = 'Cambio de aceite'
    if prediccion == 2:
        recomendacion = 'Mantenimiento general'
    if prediccion == 3:
        recomendacion = 'Cambio de filtro de aire'
    if prediccion == 4:
        recomendacion = 'Cambio de pastillas de freno'
    
    response = {"recomendacion":recomendacion}
    print(recomendacion)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=False, port=4000)
