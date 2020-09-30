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

    postgreSQL_select_Query = "select * from tmask_var"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from tmask table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("ID = ", row[0], )
        print("ZMIENNA = ", row[1])
        print("WARTOSC  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
