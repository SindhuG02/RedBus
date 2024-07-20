import mysql.connector
#pip install mysql-connector-python if any error related to password
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678'
)
cursor=con.cursor()

query="create database if not exists Redbus"
cursor.execute(query)

query='use Redbus'
cursor.execute(query)

query='''create table bus_routes(
                ID int NOT NULL AUTO_INCREMENT,
                Route_name varchar(100),
                Route_link varchar(500),
                Busname varchar(50),
                Bustype varchar(100),
                Departing_time datetime,
                Duration varchar(50),
                Reaching_time datetime,
                Star_rating float,
                Price decimal(6,2),
                Seats_available varchar(50),
                Government_Bus_name varchar(10),
                PRIMARY KEY (ID))'''
cursor.execute(query)