import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=sa;PWD=12345')
cursor = cnxn.cursor()

class Register:
  def Addmember(self,member_id,member_name):
    cursor.execute("insert into users(user_id,user_name) values(?, ?)",(member_id,member_name))
    cnxn.commit()

Reg = Register()

Reg.Addmember(4993123,"John")
cursor.execute("select user_id, user_name from users")
rows = cursor.fetchall()
for row in rows:
    print row.user_id, row.user_name