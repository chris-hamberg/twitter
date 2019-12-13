from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import pathlib, sqlalchemy, sys, os
import inspect, logging


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
            # self.temp.commit()
            pass
        except Exception as error:
            log.error(f'{__class__} : {str(error)}')
            self.temp.rollback()
            raise
        #self.temp.close()
        # del self.temp


location = sys.argv[0] or __name__.split('.')[0]
parent = pathlib.Path(location).absolute()
if 'test' in str(parent):
    parent = os.sep.join(str(parent).split(os.sep)[:-1])
database = pathlib.Path(parent, 'database.sql')


engine = sqlalchemy.create_engine(f'sqlite:////{database}')
database = SQLAlchemy(engine)


log = logging.getLogger(__name__)
handler = logging.FileHandler(pathlib.Path(parent, 'data.log'))
handler.setLevel(logging.INFO)
formatter = logging.Formatter(' %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
