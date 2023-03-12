import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
cur = mydb.cursor()

#cur.execute("create database Student")
#cur.execute('create table Student.ClassA(stdId int, firstName varchar(25) , lastName varchar(30) , sub varchar(20))')
#cur.execute("""insert into Student.ClassA values(4, "Shyamali", "Dolekar", "React"),
#(5, "Akshata", "M", "Java"),
#(6, "Sanjana", "Pawar", "Angular")""")
#mydb.commit()

#cur.execute('select * from Student.ClassA')
#for i in cur:
#  print(i)

cur.execute('select stdId , firstName ,sub from Student.ClassA')
for i in cur:
  print(i)

cur.execute('select * from Student.ClassA where lastName = "Pawar"')
for i in cur:
  print(i)

cur.execute('update Student.ClassA set firstName ="Shambhavi" where stdId =5')

mydb.commit()

cur.execute('delete from Student.ClassA where firstName ="Shambhavi"')

mydb.commit()

cur.execute('select min(stdId) from Student.ClassA')
for i in cur:
  print(i)

cur.execute('select max(stdId) from Student.ClassA')
for i in cur:
  print(i)

cur.execute('select count(*), lastName from Student.ClassA group by lastName')
for i in cur:
  print(i)