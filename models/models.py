from sqlalchemy import *
import psycopg2
class Database:
    engine = create_engine('postgres://postgres:anojk@localhost:5432/schoolapp')
    conn = engine.connect()
    metadata = MetaData()

    student = Table('student', metadata,
    Column('student_id', Integer,autoincrement=true,primary_key=true),
    Column('student_name', String(16), nullable=False),
    Column('father_name', String(16), nullable=False),
    Column('email', String(60)),
    Column('address', String(200), nullable=False),
    Column('school_name', String(200), nullable=False)
    )

