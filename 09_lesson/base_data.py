from sqlalchemy import create_engine 

db_connection_string = "postgresql://V:06071992@localhost:5432/квест"
db = create_engine(db_connection_string)

with create_engine() as connection:
     result = connection.execute("SELECT 1;")
     print(result.fetchone())