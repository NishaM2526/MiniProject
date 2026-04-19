import mysql.connector
import DataExtract as de

mysql_connection = mysql.connector.connect(
            user="root",
            host="localhost",
            password="Nisha@2506",
            database='phone_pe_pulse'
            )
cursor = mysql_connection.cursor()
print("Connection established..")

class create_sql_table:
    def db_create_database(self):
        # create database
        cursor.execute("create database phone_pe_pulse")

    def db_create_table(self):
        # table creation for aggregated data
        # table for aggregated_transaction
        cursor.execute("""create table if not exists aggregated_transaction(
        State    varchar(255),
        Year     int,
        Quarter  int,
        Transaction_type  varchar(255),
        Transaction_count bigint,
        Transaction_amount bigint
        )""")

        # table for map_transaction
        cursor.execute("""create table if not exists map_transaction(
        State    varchar(255),
        Year     int,
        Quarter  int,
        District varchar(100),
        Transaction_count bigint,
        Transaction_amount bigint
        )""")

        # table for top_transaction_district
        cursor.execute("""create table if not exists top_transaction_district(
        State    varchar(255),
        Year     int,
        Quarter  int,
        District  varchar(255),
        Transaction_count bigint,
        Transaction_amount bigint
        )""")

        # table for top_transaction_pincode
        cursor.execute("""create table if not exists top_transaction_pincode(
        State    varchar(255),
        Year     int,
        Quarter  int,
        Pincode  int,
        Transaction_count bigint,
        Transaction_amount bigint
        ) """)

        # table creation for users details
        # table for aggregated_users
        cursor.execute("""create table if not exists aggregated_users(
        State    varchar(255),
        Year     int,
        Quarter  int,
        User_brand  varchar(255),
        User_count bigint,
        User_percentage float
        ) """)

        # table for map_users
        cursor.execute("""create table if not exists map_users(
        State    varchar(255),
        Year     int,
        Quarter  int,
        District  varchar(255),
        Registered_user bigint,
        App_opens bigint
        ) """)

        # table for top_users_district
        cursor.execute("""create table if not exists top_users_district(
        State    varchar(255),
        Year     int,
        Quarter  int,
        District  varchar(255),
        Registered_user bigint
        ) """)

        # table for top_users_pincode
        cursor.execute("""create table if not exists top_users_pincode(
        State    varchar(255),
        Year     int,
        Quarter  int,
        Pincode  int,
        Registered_user bigint
        ) """)

        # table creation for insurance data
        # table for aggregated_insurance
        cursor.execute("""create table if not exists aggregated_insurance(
        State    varchar(255),
        Year     int,
        Quarter  int,
        Payment_type  varchar(255),
        Insurance_count bigint,
        Insurance_amount bigint
        )""")

        # table for map_insurance
        cursor.execute("""create table if not exists map_insurance(
        State    varchar(255),
        Year     int,
        Quarter  int,
        District  varchar(255),
        Insurance_count bigint,
        Insurance_amount bigint
        )""")

        # table for top_insurance_district
        cursor.execute("""create table if not exists top_insurance_district(
        State    varchar(255),
        Year     int,
        Quarter  int,
        District  varchar(255),
        Insurance_count bigint,
        Insurance_amount bigint
        ) """)

        # table for top_insurance_pincode
        cursor.execute("""create table if not exists top_insurance_pincode(
        State    varchar(255),
        Year     int,
        Quarter  int,
        Pincode  int,
        Insurance_count bigint,
        Insurance_amount bigint
        ) """)

class insert_sql_table:   
    # inserting values into transaction table 
    # inserting values into aggregated_transaction table
    def insert_to_aggregated_transaction(self):
        data = de.get_aggregated_trans_load().values.tolist()
        query = "insert into aggregated_transaction values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into map_transaction table
    def insert_to_map_transaction(self):
        data = de.get_map_trans_load().values.tolist()
        query = "insert into map_transaction values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into top_transaction_district table
    def insert_to_top_transaction_district(self):
        data = de.get_top_trans_dist_load().values.tolist()
        query = "insert into top_transaction_district values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into top_transaction_pincode table
    def insert_to_top_transaction_pincode(self):
        data = de.get_top_trans_pincode_load().values.tolist()
        query = "insert into top_transaction_pincode values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into users table
    # inserting values into aggregated users table
    def insert_to_aggregated_users(self):
        data = de.get_aggregated_user_load().values.tolist()
        query = "insert into aggregated_users values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()
    
    # inserting values into  map_users table
    def insert_to_map_users(self):
        data = de.get_map_user_load().values.tolist()
        query = "insert into map_users values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into  top_users_district table
    def insert_to_top_users_district(self):
        data = de.get_top_user_dist_load().values.tolist()
        query = "insert into top_users_district values(%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into  top_users_pincode table
    def insert_to_top_users_pincode(self):
        data = de.get_top_user_pincode_load().values.tolist()
        query = "insert into top_users_pincode values(%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into aggregated_insurance table
    def insert_to_aggregated_insurance(self):
        data = de.get_aggregated_ins_load().values.tolist()
        query = "insert into aggregated_insurance values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into map_insurance table
    def insert_to_map_insurance(self):
        data = de.get_map_ins_load().values.tolist()
        query = "insert into map_insurance values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into top_insurance_district table
    def insert_to_top_insurance_district(self):
        data = de.get_top_ins_dist_load().values.tolist()
        query = "insert into top_insurance_district values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

    # inserting values into top_insurance_pincode table
    def insert_to_top_insurance_pincode(self):
        data = de.get_top_ins_pincode_load().values.tolist()
        query = "insert into top_insurance_pincode values(%s,%s,%s,%s,%s,%s)"
        for i in data:
            cursor.execute(query, tuple(i))
        mysql_connection.commit()

#create_table = create_sql_table()
#create_table.db_create_database()

def load_data_to_table():
    create_table = create_sql_table()
    insert_table = insert_sql_table()

    create_table.db_create_table()

    insert_table.insert_to_aggregated_transaction()
    insert_table.insert_to_map_transaction()
    insert_table.insert_to_top_transaction_district()
    insert_table.insert_to_top_transaction_pincode()

    insert_table.insert_to_aggregated_users()
    insert_table.insert_to_map_users()
    insert_table.insert_to_top_users_district()
    insert_table.insert_to_top_users_pincode()

    insert_table.insert_to_aggregated_insurance()
    insert_table.insert_to_map_insurance()
    insert_table.insert_to_top_insurance_district()
    insert_table.insert_to_top_insurance_pincode()

load_data_to_table()
cursor.close()