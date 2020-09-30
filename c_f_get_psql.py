import psycopg2

class TmaskPslq:

# Dodaj wartość
    def ins_var_to_psql(var1, var2):

        try:
            connection = psycopg2.connect(user = "dniemczok",
            password = "postgres",
            host = "127.0.0.1",
            port = "5432",
            database = "dniemczok")

            cursor = connection.cursor()
            # Print PostgreSQL Connection properties
            #print ( connection.get_dsn_parameters(),"\n")

            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            #print("You are connected to - ", record,"\n")

            postgres_insert_query = """ INSERT INTO tmask_var (ZMIENNA, WARTOSC) VALUES (%s,%s)"""
            record_to_insert = (var1, var2)
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
                #print("PostgreSQL connection is closed")

# Pobierz wartość
    def get_var_to_psql(var1):
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

                                #get_var_do_psql('PATH')

# Wyświetl wszystko
    def all_var_to_psql():
        try:
            connection = psycopg2.connect(user = "dniemczok",
            password = "postgres",
            host = "127.0.0.1",
            port = "5432",
            database = "dniemczok")

            cursor = connection.cursor()
            # Print PostgreSQL Connection properties
            #print ( connection.get_dsn_parameters(),"\n")

            postgreSQL_select_Query = "select * from tmask_var"

            cursor.execute(postgreSQL_select_Query)
            #print("Selecting rows from tmask table using cursor.fetchall")
            mobile_records = cursor.fetchall()

            #print("Print each row and it's columns values")
            for row in mobile_records:
                print("ZMIENNA = ", row[0])
                print("WARTOSC  = ", row[1], "\n")

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")
