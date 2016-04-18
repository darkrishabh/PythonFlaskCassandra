__author__ = 'hangvirus'

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from models.user import Person

connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)

sync_table(Person)
