from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import pathlib, sqlalchemy, sys, os

class SQLAlchemy():

    def __init__(self, engine):
        self.engine   = engine
        self.Model    = declarative_base()
        self.factory  = sessionmaker(bind=self.engine)
        self.Session  = scoped_session(self.factory)

    def create_tables(self):
        self.Model.metadata.create_all(self.engine)

    def __enter__(self):
        self.temp = self.Session()
        return self.temp

    def __exit__(self, t, u, v):
        try:
            self.temp.commit()
        except Exception as error:
            self.temp.rollback()
            raise
        finally:
            self.temp.close()
            del self.temp

location = sys.argv[0] or __name__.split('.')[0]
parent = pathlib.Path(location).absolute()
if 'test' in str(parent):
    parent = os.sep.join(str(parent).split(os.sep)[:-1])
database = pathlib.Path(parent, 'database.sql')

engine = sqlalchemy.create_engine(f'sqlite:////{database}')
database = SQLAlchemy(engine)
