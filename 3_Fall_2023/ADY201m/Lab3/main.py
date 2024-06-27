import mysql.connector
from mysql.connector import Error
import numpy as np
import pandas as pd

def test_connect():
  try:
    connection = mysql.connector.connect(
      host='localhost',
      database='demo',
      user='root',
      password='12345678'
    )
    if connection.is_connected():
      db_Info = connection.get_server_info()
      print("Connected to MySQL Server version ", db_Info)
      cursor = connection.cursor()
      cursor.execute("select database();")
      record = cursor.fetchone()
      print("You're connected to database: ", record)

  except Error as error:
    print("Error while connecting to MySQL", error)
  finally:
    if connection.is_connected():
      cursor.close()
      connection.close()
      print("MySQL connection is closed")

connection = mysql.connector.connect(
  host='localhost',
  database='demo',
  user='root',
  password='12345678'
)

cursor = connection.cursor()
columns_query = "show columns from chicago from demo"

def query_cols(connection = connection, query: str = columns_query):
  cursor = connection.cursor()
  cursor.execute(query)
  record = np.array(cursor.fetchall())
  cols = record[:, 0]
  print(cols)
  return cols

def query(connection = connection, query_string: str= ""):
  cursor = connection.cursor()
  cursor.execute(query_string)

  records = cursor.fetchall()
  table = pd.DataFrame(np.array(records))
  print(table)
  return table

question_1 = """
  SELECT
      NAME_OF_SCHOOL,SAFETY_SCORE,
      SAFETY_ICON
  FROM chicago
  WHERE SAFETY_SCORE not like \'%NONE%\'
  ORDER BY SAFETY_SCORE DESC LIMIT 5
"""

question_2 = """
SELECT 
  ELEMENTARY__MIDDLE__OR_HIGH_SCHOOL, 
  COUNT(*) as total_number_of_students 
FROM CHICAGO_TAB 
GROUP BY ELEMENTARY__MIDDLE__OR_HIGH_SCHOOL
"""

question_3 = """
  SELECT ROUND(AVG(CAST(REPLACE(AVERAGE_STUDENT_ATTENDANCE, '%', '') AS DECIMAL(5, 2))),2) AS average_attendance
  FROM (
    SELECT 
      Name_OF_SCHOOL,
      AVERAGE_STUDENT_ATTENDANCE,
      SAFETY_SCORE
    FROM chicago
    ORDER BY SAFETY_SCORE
    LIMIT 10
  ) AS subquery;
"""

question_4 = """
SELECT Name_OF_SCHOOL, CAST(College_Eligibility__ AS FLOAT) AS College_Eligibility_Score
FROM chicago
WHERE COLLEGE_ELIGIBILITY__ NOT LIKE '%NDA%'
ORDER BY College_Eligibility_Score DESC
LIMIT 10;
"""

# query(query_string="Select * from chicago")
# query(query_string=question_1)
# query(query_string=question_2)
# query(query_string=question_3)
# query(query_string=question_4)