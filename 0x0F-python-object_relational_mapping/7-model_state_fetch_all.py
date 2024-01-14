#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://sys.argv[1]:sys.argv[2]@localhost:\
                           3306/sys.argv[3]', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    [print("{}: {}".format(state.id, state.name)) for state in states]
