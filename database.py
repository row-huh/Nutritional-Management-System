import oracledb

# Establish the database connection
connection = oracledb.connect(
    user='your_username',
    password='your_password',
    dsn='your_dsn'  # DSN (Data Source Name) typically includes host, port, and service name
)

# Create a cursor object
cursor = connection.cursor()


def insert_data():
    #TODO
    ...

    
def delete_date():
    #TODO
    ...

def update_data():
    #TODO
    ...
    
def query_date():
    #TODO
    ...