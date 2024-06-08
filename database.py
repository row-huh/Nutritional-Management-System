import oracledb

# Establish the database connection
connection = oracledb.connect(
    user='your_username',
    password='your_password',
    dsn='your_dsn'  # DSN (Data Source Name) typically includes host, port, and service name
)

# Create a cursor object
cursor = connection.cursor()


'''
Each of the functions below will take in parameters
required to perform an operation such as to insert a new 
entry in data, we'll need "calorie-figure" or whatever other fields are
'''

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