from flask import Flask, jsonify
from azure.storage.blob import BlobServiceClient
import json
import config



blob_service_client = BlobServiceClient.from_connection_string(config.connection_string)
container_client = blob_service_client.get_container_client(config.container_name)

app = Flask(__name__)

def get_cyberattaques():
    try:
        """ with open('static_content.json', 'r') as file:
            data = json.load(file)
        return data """
        BlobClient = container_client.get_blob_client(config.json_name)
        blob_data = BlobClient.download_blob().readall()
        data = json.loads(blob_data)
        print(data)
        return data

    except FileNotFoundError:
        return jsonify({"error": "Fichier JSON non trouvé"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Erreur de décodage JSON"}), 400

@app.route('/api/events', methods=['GET'])
def get_events():
    data = get_cyberattaques()
    return data["cyberattaques_france_2022"]["couts"]["details"]

@app.route('/api/news', methods=['GET'])
def get_new():
    data = get_cyberattaques()
    return data["cyberattaques_france_2022"]["repartition"]["entreprises"]
if __name__ == '__main__':
    print("Server started on port 5000")
    app.run(debug=True, host='0.0.0.0' , port=5000)
