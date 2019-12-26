import psycopg2

'''
This is a utility, wrapper class to surround the functionality of basic DB operations (insert/select/delete)
'''

# Environmental Variables -> move later on to deployment
HOST = '0.0.0.0'
DATABASE = 'url'
USER = 'postgres'
PASSWORD = 'postgres'

def get_row(**data):
    '''
    Gets row data from PostgreSQL Database given the id/url.

    Parameters:
    data (id, str): The arguments to be used in the SELECT query.

    Returns:
    tuple: A tuple of the id and the corresponding url as saved in the database.
    '''

    if 'id' in data:
        # Query based on the id (row number)
        strategy = lambda cursor : cursor.execute('SELECT id, url FROM url WHERE id = ' + str(data['id']))
    
    elif 'url' in data:
        # Query based on the url (see if anything matches)
        strategy = lambda cursor : cursor.execute('SELECT id, url FROM url WHERE url = \'' + str(data['url']) + '\'')

    return db_execute_strategy(strategy, method='READ')

def insert_row(url: str):
    '''
    Inserts row data from PostgreSQL Database given a URL.
    The PostgreSQL configuration should be able to keep track of the id (SERIAL).

    Parameters:
    url (str): The url to insert in the database.
    '''
    # Insert a row with the given url (done only if nothing matches)
    strategy = lambda cursor : cursor.execute('INSERT into url (url) VALUES (\'' + url + '\')')

    return db_execute_strategy(strategy, method='CREATE')

def db_execute_strategy(strategy, **data):
    '''
    Wrapper function for all DB Queries.

    Parameters:
    strategy (func): A strategy that is applied onto the given cursor.
    **data: Type of the query to be made (CRUD).

    Returns:
    None/List[int, str]: The return type is dependent on the strategy being executed.
    '''

    # Connection to local PSQL DB
    connection = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )

    # Get Cursor 
    cursor = connection.cursor()

    # Execute Query Strategy
    # If we get something back from the strategy, we should return it
    result = strategy(cursor)
    if data['method'] == 'CREATE':
        connection.commit()

    if data['method'] == 'READ':
        return cursor.fetchall()

    # Close connection to avoid corruption
    connection.close()