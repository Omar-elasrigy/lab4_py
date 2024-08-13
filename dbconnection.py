import psycopg2
import sys
host="localhost"
user="postgres"
password="12345678"
dbname="iti"
def connect():
    try:
        connection=psycopg2.connect(database=dbname,user=user,password=password,
                                    host=host)
        return connection
     
    except:
        print(sys.exc_info()[1])

def inserttrainee(id,name,track_id):
    connection=connect()
    try:
        cur=connection.cursor()
        cur.execute(f"insert into trainee values ({id},'{name}',{track_id})")
        connection.commit()
    except:
        print(sys.exc_info()[1])
def updatetrainee(id,name,track_id):

    connection=connect()
    try:
        cur=connection.cursor()
        cur.execute(f"""update trainee 
                    set name='{name}',track_id={track_id}
                    where trainee_id={id};""")
        connection.commit()
    except:
        print(sys.exc_info()[1])
def delete_from_trainee(id):
    connection=connect()
    try:
        cur=connection.cursor()
        cur.execute(f"delete from trainee where trainee_id={id};")
        connection.commit()
    except:
        print(sys.exc_info()[1])
def inserttrack(track_id,track_name,capacity):
    connection=connect()
    try:
        cur=connection.cursor()
        cur.execute(f"insert into tracks values ({track_id},'{track_name}',{capacity})")
        connection.commit()
    except:
        print(sys.exc_info()[1])
def updatetrack(track_id,name,capacity):
    connection=connect()
    try:
        cur=connection.cursor()
        cur.execute(f"""update tracks
                    set name='{name}',capacity={capacity}
                    where track_id={track_id};""")
        connection.commit()
    except:
        print(sys.exc_info()[1])
def delete_from_tracks(track_id):
    connection=connect()
    try:
        cur=connection.cursor()
        cur.execute(f"delete from tracks where track_id={track_id};")
        connection.commit()
    except:
        print(sys.exc_info()[1])

def selectfromtable(table_name):
    connection=connect()
    try:
        cur=connection.cursor()
        cur.execute(f"select * from {table_name};")
        data=cur.fetchall()
        return data
    except:
        print(sys.exc_info()[1])


# inserttrainee(4,"Mariam Mahmoud",1)

delete_from_trainee(1)
print(selectfromtable("trainee"))

