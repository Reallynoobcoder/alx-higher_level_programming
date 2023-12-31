#!/usr/bin/python3
"""that prints all City objects from the database"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    all_cities = session.query(State, City)\
        .join(State, State.id == City.state_id).all()

    for state, city in all_cities:
        print(f"{state.name}: ({city.id}) {city.name}")
