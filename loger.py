import psycopg2


class loger:
    def __init__(self,database,host,user,password,port,database_table):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database_table = database_table
        try:
            self.connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)
            self.cursor = self.connection.cursor()


        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

    def show(self):
            postgreSQL_select_Query = f"SELECT * FROM {self.database_table};"
            self.cursor.execute(postgreSQL_select_Query)
            main_data = self.cursor.fetchall()
            print(main_data)

    def add(self,nickname,password,telegram_id,key):
        self.cursor.execute(f"SELECT {telegram_id} FROM {self.database_table} ")
        ids = self.cursor.fetchall()
        print(ids)
        if ids != [] :
            print("Current user exists")
        else :
            self.cursor.execute(f"insert into {self.database_table} values (DEFAULT,'{nickname}','{password}',{telegram_id},{key});")
            self.connection.commit()


if __name__ == '__main__':
    a = loger('loger','127.0.0.1','postgres','postgres','5432','main')
    a.show()
    a.add('smail','smail',123415,12415152)
    a.show()