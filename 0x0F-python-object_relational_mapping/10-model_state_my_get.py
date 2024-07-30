#!/usr/bin/python3
"""
Start link class to table in database
list all the states
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1],
                    sys.argv[2],
                    sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = sys.argv[4]
    result = session.query(State).filter(State.name == (sys.argv[4],)).first()
    if result:
        print(f"{result.id}")
    else:
        print("Not found")
