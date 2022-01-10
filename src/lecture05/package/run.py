from . import core
from .util import db, my_math, network

def main():
    db_conn = db.connect('url', 5000, 'user', 'passwd')
    print(db_conn)
    net_conn = network.connect('url', 5000, 'user', 'passwd')
    print(net_conn)
    print(my_math.square(10))
    core.func1()
