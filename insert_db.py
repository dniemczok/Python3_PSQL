import psycopg2
try:
    connection = psycopg2.connect(user = "dniemczok",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "dniemczok")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    postgres_insert_query = """ INSERT INTO tmask_var (ZMIENNA, WARTOSC) VALUES (%s,%s)"""
    record_to_insert = ('PATH', '/opt/DOC')
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
