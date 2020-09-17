import pandas as pd
from config import DB_DETAILS
import mysql.connector as mc
from mysql.connector import errorcode as ec
import psycopg2

def load_db_details(env):
    return DB_DETAILS[env]


def get_mysql_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = mc.connect(user=db_user,
                                host=db_host,
                                password=db_pass,
                                database=db_name
                                )

    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
        else:
            print(error)
    return connection


def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_user=db_user,
                                          db_host=db_host,
                                          db_pass=db_pass,
                                          db_name=db_name
                                          )
    if db_type == 'postgres':
        connection = get_pg_connection(db_user=db_user,
                                       db_host=db_host,
                                       db_pass=db_pass,
                                       db_name=db_name
                                       )
    return connection

def get_pg_connection(db_host, db_name, db_user, db_pass):
    connection = psycopg2.connect(f"user={db_user} host={db_host} password={db_pass} dbname={db_name}")
    return connection

def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded == "yes"')

