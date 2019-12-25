import psycopg2

# Environmental Variables -> move later on to deployment
HOST = '0.0.0.0'
DATABASE = 'url'
USER = 'postgres'
PASSWORD = 'postgres'

def get_row(condition: str):
    '''
    Gets row data from PostgreSQL Database given a specific condition.

    Parameters:
    condition (str): The query condition, ex: 'WHERE id = 0'

    Returns:
    tuple: A tuple of the id and the corresponding Url as saved in the database.
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
    # Execute Query
    cursor.execute('SELECT id, url FROM url WHERE ' + condition)
    # The rows we got
    rows = cursor.fetchall()
    # Close connection to avoid corruption
    connection.close()

    # Hypothetically we should only be getting 1 row, however break just in case
    return rows[0]