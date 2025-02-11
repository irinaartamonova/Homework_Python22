import pytest
from sqlalchemy import Connection, create_engine
from your_module import place_name, Base

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

def test_add_place_name(setup_database: Connection):
    connection = setup_database
    new_student =place_name(name="John Doe")
    connection.execute(place_name.__table__.insert(), {
    "name": new_place_name.name
    })
    result = connection.execute(place_name.__table__.select()).fetchall()
    assert len(result) == 1
    assert result[0].name == "John Doe"

