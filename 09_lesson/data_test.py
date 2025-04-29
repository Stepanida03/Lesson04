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
    sql = text('INSERT INTO student (user_id, level, education_form) VALUES (:user_id, :level, :education_form)')
    db_session.execute(sql, {'user_id': 2610, 'level': 'Pre-Intermediate', 'education_form': 'personal'})
    db_session.commit()

    result = db_session.execute(text("SELECT * FROM student WHERE user_id = :user_id"), {'user_id': 2610})
    row = result.fetchall()
    assert row is not None
    assert row [0][1] == 'Pre-Intermediate'

def test_update(db_session):
    db_session.execute(text('INSERT INTO student (user_id, level, education_form) VALUES (:user_id, :level, :education_form)'),{'user_id': 2610, 'level': 'Pre-Intermediate', 'education_form': 'personal'})
    db_session.commit()

    sql = text("UPDATE student SET education_form = :education_form WHERE user_id = :user_id")
    db_session.execute(sql, {'education_form': 'group', 'user_id': 2610})
    db_session.commit()

    result = db_session.execute(text("SELECT education_form FROM student WHERE user_id = :user_id"), {'user_id': 2610})
    row = result.fetchall()
    assert row[0][0] == 'group'

def test_delete(db_session):
    db_session.execute(text('INSERT INTO student (user_id, level, education_form) VALUES (:user_id, :level, :education_form)'),{'user_id': 2610, 'level': 'Pre-Intermediate', 'education_form': 'group'})
    db_session.commit()

    sql = text("DELETE FROM student WHERE user_id = :user_id")
    db_session.execute(sql, {"user_id": 2610})
    db_session.commit()

    result = db_session.execute(text("SELECT * FROM student WHERE user_id = :user_id"), {'user_id': 2610})
    row = result.fetchone()
    assert row is None