from flask_sqlalchemy import SQLAlchemy
from random import randint

db = SQLAlchemy()

class FamilyTree:
    def __init__(self, last):
        self.last = last

        self.members = {
            'id': 1,
            'first': 'Abuelo',
            'last': 'self.last',
            'age': '32',
            'parent': 'none',
            'child': '2, 3'    
        },
         self.members = {
            'id': 2,
            'first': 'Abuelo',
            'last': 'self.last',
            'age': '32',
            'parent': 'none',
            'child': '2, 3'    
        },
         self.members = {
            'id': 3,
            'first': 'Abuelo',
            'last': 'self.last',
            'age': '32',
            'parent': 'none',
            'child': '2, 3'    
        },
         self.members = {
            'id': 4,
            'first': 'Abuelo',
            'last': 'self.last',
            'age': '32',
            'parent': 'none',
            'child': '2, 3'    
        },
         self.members = {
            'id': 5,
            'first': 'Abuelo',
            'last': 'self.last',
            'age': '32',
            'parent': 'none',
            'child': '2, 3'    
        },
         self.members = {
            'id': 6,
            'first': 'Abuelo',
            'last': 'self.last',
            'age': '32',
            'parent': 'none',
            'child': '2, 3'    
        },
         self.members = {
            'id': 7,
            'first': 'Abuelo',
            'last': 'self.last',
            'age': '32',
            'parent': 'none',
            'child': '2, 3'    
        },

        # def generateId (self):
        #     return randint (0, 9999999999999)
        #     def addMember(self,{data})