from flask_sqlalchemy import SQLAlchemy
from random import randint #libreria que entrega un numero aleatorio

# db = SQLAlchemy()

class FamilyTree:
    def __init__(self, last):
        self.last = last

        self.members = [ { 
            'id' : 1,
            'first' : 'Abuelo',
            'last' : self.last,
            'age' : 32,
            'parent' : None,
            'child' : [2, 3]
        } ,
        {
            'id' : 2,
            'first' : 'Tio',
            'last' : self.last,
            'age' : 32,
            'parent' : 1,
            'child' : None
        },
        {
            'id' : 3,
            'first' : 'Padre',
            'last' : self.last,
            'age' : 32,
            'parent' : 1,
            'child' : [4]
        },
        {
            'id' : 4,
            'first' : 'Luis',
            'last' : self.last,
            'age' : 32,
            'parent' : 3,
            'child' : None
        },
        {
            'id' : 5,
            'first' : 'Luis Hermano',
            'last' : self.last,
            'age' : 32,
            'parent' : 3,
            'child' : None
        },
        {
            'id' : 6,
            'first' : 'Tio2',
            'last' : self.last,
            'age' : 32,
            'parent' : 1,
            'child' : [7]
        },
        {
            'id' : 7,
            'first' : 'Primo',
            'last' : self.last,
            'age' : 32,
            'parent' : 6,
            'child' : None
        }
        ]
    
    def memberId(self, id):
        for miembro in self.members:
            if miembro['id'] == int(id):
                return miembro
        return None

    # def generateId(self):
    #     return randint(0, 99999999999999)