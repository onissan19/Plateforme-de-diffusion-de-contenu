from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables d'environnement depuis .env

connection_string = os.getenv("AZURE_CONN_STRING")
container_name =  os.getenv("AZURE_CONTAINER_NAME")
json_name = os.getenv("BLOB_JSON_NAME")