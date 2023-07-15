import mysql.connector
host = '127.0.0.1' 
user = 'root' 
password = 'Kansas16'  
database = 'fb_team_database' 
def auto_increment():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()

    alter_query = '''
    ALTER TABLE players
    AUTO_INCREMENT = 1
    '''
    cursor.execute(alter_query)

    conn.commit()

    cursor.close()
    conn.close()