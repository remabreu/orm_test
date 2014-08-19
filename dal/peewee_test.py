'''
Created on Aug 19, 2014

@author: rodrigoabreu
'''
from peewee import *
from datetime import date

db = SqliteDatabase('/Users/rodrigoabreu/people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

#Person.create_table()
#db.create_table([Person])

if __name__ == "__main__":
#    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
#    uncle_bob.save()
    print Person.get().name