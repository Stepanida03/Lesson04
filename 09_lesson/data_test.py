import pytest
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker

db_connection_string = "postgresql://postgres:79053@localhost:5432/postgres"
db = create_engine(db_connection_string)
trying = sessionmaker(bind=db)

@pytest.fixture
def db_session():
    con = db.connect()
    trad = con.begin()
    tr = trying(bind=con)

    yield tr

    tr.close()
    trad.rollback()
    con.close()

def test_db_connection(db_session):
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'student' in names

def test_insert(db_session):
    sql = text('INSERT INTO student (student_id, level, form) VALUES (student_id, level, form)')
    db_session.execute(sql, {'student_id': 2610, 'level': 'Pre-Intermediate', 'form': 'personal'})
    db_session.commit()

    result = db_session.execute(text("SELECT * FROM student WHERE student_id = :student_id"), {'student_id': 2610})
    row = result.fetchall()
    assert row is not None
    assert row [0][1] == 'Pre-Intermediate'

def test_update(db_session):
    db_session.execute(text('INSERT INTO student (student_id, level, form) VALUES (student_id, level, form)'),{'student_id': 2610, 'level': 'Pre-Intermediate', 'form': 'personal'})
    db_session.commit()

    sql = text("UPDATE student SET form = :form WHERE student_id = :student_id")
    db_session.execute(sql, {'form': 'group', 'student_id': 2610})
    db_session.commit()

    result = db_session.execute(text("SELECT form FROM student WHERE student_id = :student_id"), {'student_id': 2610})
    row = result.fetchall()
    assert row[0][0] == 'group'

def test_delete(db_session):
    db_session.execute(text('INSERT INTO student (student_id, level, form) VALUES (student_id, level, form)'),{'student_id': 2610, 'level': 'Pre-Intermediate', 'form': 'group'})
    db_session.commit()

    sql = text("DELETE FROM student WHERE student_id = :student_id")
    db_session.execute(sql, {"student_id": 2610})
    db_session.commit()

    result = db_session.execute(text("SELECT * FROM student WHERE student_id = :student_id"), {'student_id': 2610})
    row = result.fetchone()
    assert row is None