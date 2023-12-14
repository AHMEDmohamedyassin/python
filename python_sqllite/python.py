import sqlite3


## connect to database
def connectDB():
    try:        
        db = sqlite3.connect('app.db')
    except: db = False
    finally : return db


## create to database
def createDB (db) :
    try :
        cr = db.cursor() 
        cr.execute('create table if not exists users (name text , id integer , role text)')
        return True
    except : return False

## add to database
def addDB (db , data):  ## how to use => addDB(db , {"name" : "ahmed" , "id" : 1 , "role" : "user"})
    try:
        queries = []
        values = []
        for keys in data:
            queries.append(keys)
            values.append(f'"{data[keys]}"')
        queries = ','.join(queries)
        values = ','.join(values)

        cr = db.cursor()
        cr.execute(f'insert into users({queries}) values({values})')
        db.commit()
        return True
    except: return False

## database where handle
def usingWhere(where):
    queries = []
    for key in where:
        queries.append(f'{key} = "{where[key]}"')
    if len(queries) > 0:
        queries = f' where {" and ".join(queries)}'
    else: queries = ''

    return queries

## get from database
def getDB(db , where):  ## how to use =>  getDB(db , {"id" : 9 , "name" : "ahmed9" })
    try:
        queries = usingWhere(where)
        cr = db.cursor()
        cr.execute(f'select * from users {queries}')
        return cr.fetchall()
        # return cr.fetchone()
    except: False

## update in data base
def updateDB(db , theUpdate , where):  ## how to use => updateDB(db , {'name' : 'ahemd' , "id" : 56} , {"name" : "ahmed-1" , "id" : 1})
    upd = []
    for key in theUpdate:
        upd.append(f'{key} = "{theUpdate[key]}"')
    queries = usingWhere(where)
    
    try:
        cr = db.cursor()
        cr.execute(f'update users set {" , ".join(upd)} {queries} ')
        db.commit()
        return True
    except : return False

## delete from database
def deleteDB(db , where): ## how to use => deleteDB(db , {'name' : 'ahemd' , "id" : 56} )
    try:
        queries = usingWhere(where)
        cr = db.cursor()
        cr.execute(f'delete from users {queries}')
        db.commit()
        return True
    except: return False


# fast testing
db = connectDB()
cr = db.cursor()
data = cr.execute('select * from users order by name desc limit 3 offset 10')
ls = data.fetchall()
print(ls)



##################
### data base usage  ####

# cr.execute('create table if not exists users (name text , id integer , role text)')

# cr.execute(f'insert into users(name , id) values("ahmed" , 2 )')
# cr.execute(f'insert into users values("ahmed" , 2 )')
# cr.execute(f'insert into users values(? , ? )' , ('ahmed' , 2))

# cr.execute(f'select * from users where name = "ahmed" and id = 2 ')
# cr.execute(f'select * from users where id > 2 ')
# cr.execute(f'select * from users where id in(1 , 3) ')
# cr.execute(f'select * from users where id not in(1 , 3) ')
# cr.execute('select * from users order by name desc limit 3 offset 2')

# cr.execute("update users set name = 'Mahmoud' where user_id = 1")

# cr.execute("delete from users where user_id = 4")
