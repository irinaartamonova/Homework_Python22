import pytest
from sqlalchemy import create_engine
from place_name import place_name, Base

DATABASE_URL = "postgresql://V:06071992@localhost:5432/квест"

@pytest.fixture(scope='module')
def setup_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    connection = engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()

def test_delete_place_name(setup_database):
     connection = setup_database
     connection.execute(place_name.__table__.delete().where(place_name.name == "Jane Doe"))
     result = connection.execute(place_name.__table__.select().where(place_name.name == "Jane Doe")).fetchone()
     assert result is None
