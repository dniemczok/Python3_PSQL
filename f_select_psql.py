import psycopg2

def get_var_do_psql(var1):
    try:
        connection = psycopg2.connect(user = "dniemczok",
                                    password = "postgres",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "dniemczok")

        cursor = connection.cursor()
                                    # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")

        postgreSQL_select_Query = "select * from tmask_var where ZMIENNA = '%s'" % var1

        cursor.execute(postgreSQL_select_Query)
        #print("Selecting rows from tmask table using cursor.fetchall")
        tmask_records = cursor.fetchall()

        #print("Print each row and it's columns values")
        for row in tmask_records:
            #print("WARTOSC  = ", row[2], "\n")
            print(row[1])
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
                                        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed")

get_var_do_psql('PATH')
