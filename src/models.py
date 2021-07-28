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
            'age' : 81,
            'parent' : None,
            'child' : [6]
        } ,
        {
            'id' : 2,
            'first' : 'Tio',
            'last' : self.last,
            'age' : 63,
            'parent' : 2,
            'child' : [3],
        } ,
        {
            'id' : 3,
            'first' : 'Padre',
            'last' : self.last,
            'age' : 65,
            'parent' : 2,
            'child' : [2]
        },
        {
            'id' : 4,
            'first' : 'Luis',
            'last' : self.last,
            'age' : 31,
            'parent' : 2,
            'child' : None
        },
        {
            'id' : 5,
            'first' : 'Luis Hermano',
            'last' : self.last,
            'age' : 23,
            'parent' : 1,
            'child' : None
        },
        {
            'id' : 6,
            'first' : 'Tio2',
            'last' : self.last,
            'age' : 54,
            'parent' : 2,
            'child' : [3]
        },
        {
            'id' : 7,
            'first' : 'Primo',
            'last' : self.last,
            'age' : 33,
            'parent' : 2,
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