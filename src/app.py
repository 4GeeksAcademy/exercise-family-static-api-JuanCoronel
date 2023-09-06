"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():

    members = jackson_family.get_all_members()
    # this is how you can use the Family datastructure by calling its methods
    response_body = {
        "hello": "world",
        "family": members
    }

    return jsonify(members), 200



# Endpoint (GET)
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    # Obtiene un miembro específico de la familia Jackson por su ID
    member = jackson_family.get_member(member_id)
    # devuelve la información del miembro en formato JSON con el código de estado 200 (OK)
    return jsonify(member), 200



# Endpoint (POST)
@app.route('/member', methods=['POST'])
def add_member():
    try:
        # Intenta cargar los datos JSON de la solicitud
        new_member = json.loads(request.data)
        crearid = {"id": jackson_family._generateId(), "first_name":new_member["first_name"], "last_name":jackson_family.last_name, "age":new_member["age"], "lucky_numbers":new_member["lucky_numbers"] } 
        # Agrega un nuevo miembro a la familia Jackson
        jackson_family.add_member(crearid)
        # Devuelve los datos del nuevo miembro en formato JSON con el código de estado 200 
        return jsonify(crearid), 200
    except:
        # en caso de un error (por ejemplo, datos JSON no válidos), devuelve código 400 (Bad Request)
        return jsonify({"error": "bad request"}), 400

# ...

# Endpoint (DELETE)
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # elimina un miembro de la familia Jackson por su ID
    member = jackson_family.delete_member(member_id)
    # devuelve una respuesta JSON  con la clave "done": true.
    return jsonify({"done": True}), 200


    # this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)