database = "Learn"
host = "localhost"
port = "5432"
password = "123456"
user = "postgres"
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
class DbConnection:

    def __init__(self):
        self.engine_to_dispose = create_engine(
            'postgresql+psycopg2://{0}:{1}@{2}/{3}'.format(user, password, host + ':' + port, database))
        self.engine  = self.engine_to_dispose.connect()
        self.Session = sessionmaker()
        self.Session.configure(bind=self.engine)
        self.sess = self.Session()
        self.connection = self.engine_to_dispose.raw_connection()
        self.cursor = self.connection.cursor()
        print("connected")

    conn = DbConnection()
