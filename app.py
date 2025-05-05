from flask import Flask, request, jsonify
import joblib
import numpy as np

# Application Flask
app = Flask(__name__)

# Importation du modèle
try:
    model = joblib.load("model_rf.pkl")
except Exception as e:
    print(f"Erreur lors du chargement du modèle : {e}")
    model = None

# Chemin pour la prédiction du modèle
@app.route('/predict', methods=['POST'])
def predict():

    if model is None:
        return jsonify({'error': 'Modèle non chargé'}), 500

    try:
        # Récupération des arguments envoyés par le client
        data = request.get_json()

        # Vérification de la présence de la clé features
        if 'features' not in data:
            return jsonify({'error': "La clé 'features' est manquante"}), 400

        # Vérification qu'il y a bien 8 arguments
        features = data['features']
        if not isinstance(features, list) or len(features) != 8:
            return jsonify({'error': "Les arguments doivent être au nombre de 8 sous forme de liste"}), 400

        # Conversion et redimensionnement du tableau
        features = np.array(features).reshape(1,-1)

        # Prédiction
        prediction = model.predict(features)

        # Retour de la prédiction en JSON
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': f"Erreur lors de la prédiction : {str(e)}"})
        
# Lancement
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)