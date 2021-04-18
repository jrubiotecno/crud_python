import uuid

class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        #tiene la asignacion con un if si viene el uid lo usa si no lo define como uuid4
        self.uid = uid or uuid.uuid4()

    #importante para poder convertir la informacion como diccionario y enviarlo a disco 
    def to_dict(self):
        return vars(self)      

    #metodo estatico.. se puede ejecutar sin necesidad de declarar una instacia de clase
    @staticmethod
    def schema():
        return ['name','email','company','position','uid']


