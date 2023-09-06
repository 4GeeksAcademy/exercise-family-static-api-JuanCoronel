"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


# Define una clase llamada FamilyStructure
class FamilyStructure:
    def __init__(self, last_name):
       
        self.last_name = last_name

        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        }, {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        }, {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # metodo para generar ID de miembros de forma aleatoria 
    def _generateId(self):
        return randint(0, 99999999)

    # metodo para agregar un miembro a la familia
    def add_member(self, member):
        # agrega el miembro proporcionado a la lista de miembros
        self._members.append(member)
        return None  # Devuelve None 

    # metodo para eliminar un miembro de la familia por el ID
    def delete_member(self, id):
        # Busca y elimina un miembro con el ID 
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return member  # Devuelve el  eliminado

    # metodo para obtener un miembro de la familia por el ID
    def get_member(self, id):
        # va a buscar y devolvolver un miembro con el ID proporcionado
        for member in self._members:
            if member["id"] == id:
                return member

    # metodo para obtener una lista con todos los miembros de la familia 
    def get_all_members(self):
        return self._members  #  va a devolver la lista de miembros