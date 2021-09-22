import config
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
class DbConnection:

    def __init__(self):
        self.engine_to_dispose = create_engine(
            'postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(config.user, config.password, config.host + ':' + config.port, config.database))
        self.engine  = self.engine_to_dispose.connect()
        self.Session = sessionmaker()
        self.Session.configure(bind=self.engine)
        self.sess = self.Session()
        self.connection = self.engine_to_dispose.raw_connection()
        self.cursor = self.connection.cursor()
        print("connected")

connection = DbConnection()