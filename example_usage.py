from mysql_connect import ConnectToDatabase, ConnectionError, CredentialsError, SQLError

config = {'host': '127.0.0.1',
           'user': 'USER',
           'password': 'PASSWORD',
           'database': 'DB_NAME'}


def write_to_DB(VALUE1: str, VALUE2: str, VALUE3: str) -> None:
    try:
        with ConnectToDatabase(config['dbconfig']) as cursor:
            _SQL = """insert into TABLE
                    (COL1, COL2, COL3) values
                    (%s, %s, %s)"""
            cursor.execute(_SQL, (VALUE1, VALUE2, VALUE3))
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
    print('Unhandled Error:', str(err))

def read_from_DB() -> 'list':
    try:
        with ConnectToDatabase(config['dbconfig']) as cursor:
            _SQL = """select * from TABLE"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        return contents
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
    print('Unhandled Error:', str(err))

