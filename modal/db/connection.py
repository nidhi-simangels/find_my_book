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

    def get_book_summary(self,page_id,limit):
        try:
            query = """
                        select 
                            book_id,
                            number_of_book_genre,
                            number_rating_given,
                            round(average_rating, 2 ) average_rating,
                            number_people_added_favorite
                        from 
                            books_summary
                        order by book_id
                        limit {0}
                        offset {1}
                        """.format(limit,page_id*limit)
            curser = self.engine.execute(query)
            response = curser.fetchall()
            data =  []
            for row_tuple in  response:
                data_dict = {}
                for index,key in enumerate(curser.keys()):
                    if key=='average_rating' and row_tuple[index]!=None:
                        data_dict[key] = float(row_tuple[index])
                    else:
                        data_dict[key] = row_tuple[index]
                data.append(data_dict)
            print("data",data)
            return {"statusCode":200,"body":data}

        except Exception as e:
            print("error in get_book_summaryget_book_summary",e)
            return {"statusCode":500,"body":"error in get_book_summaryget_book_summary "+e}



connection = DbConnection()
