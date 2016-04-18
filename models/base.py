from cassandra.cqlengine.models import Model

__author__ = 'hangvirus'


class Base(Model):
    __abstract__ = True
    __keyspace__ = "cassandra_final_try"
