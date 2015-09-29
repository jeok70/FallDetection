import pyodbc
from DBconnect import DBconnect
cnxn = pyodbc.connect(DBconnect.sql)
cursor = cnxn.cursor()

class DALMember():
  def QueryMember(self,member_id):
    try:
      cursor.execute("SELECT COUNT(*) FROM users WHERE user_id = '{id}'".format(id = member_id))
      rows = cursor.fetchone()[0]
      return rows
    except pyodbc.Error:
      print 'caught an error.....continue?'   
  def Addmember(self,member_id,member_name):
    try:
      rows = self.QueryMember(member_id)
      if rows is 0:
         cursor.execute("insert into users(user_id,user_name) values(?, ?)",(member_id,member_name))
         cnxn.commit()
    except pyodbc.Error:
      print 'caught an error.....continue?'   



   




