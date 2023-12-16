#!/usr/bin/python3
"""list all State objects that contain the letter a"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter
    (State.name.like('%a%')).order_by(State.id.asc()).all()

    print("{}: {}".format(states_with_a.id, states_with_a.name))
