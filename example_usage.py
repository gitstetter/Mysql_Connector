from mysql_connect import ConnectToDatabase

config = {'host': '127.0.0.1',
           'user': 'USER',
           'password': 'PASSWORD',
           'database': 'DB_NAME', }


def write_to_DB(VALUE1: str, VALUE2: str, VALUE3: str) -> None:
    with ConnectToDatabase(config['dbconfig']) as cursor:
        _SQL = """insert into TABLE
                (COL1, COL2, COL3) values
                (%s, %s, %s)"""
        cursor.execute(_SQL, (VALUE1, VALUE2, VALUE3))

def read_from_DB() -> 'list':
    with ConnectToDatabase(config['dbconfig']) as cursor:
        _SQL = """select * from TABLE"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    return contents


