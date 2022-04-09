from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def read_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query) #returns a list of dictionaries
        #Create an empty array to iterate append the instances of dojos
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # classmethod for adding dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s);"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results
