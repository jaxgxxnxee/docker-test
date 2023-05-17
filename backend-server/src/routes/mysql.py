import pymysql
from fastapi import APIRouter

router = APIRouter(prefix="/mysql")

conn = pymysql.connect(user='root',
                       password='root',
                       host='mariadb',  # docker-compose service_name
                       port=3306
                      )

cursor = conn.cursor()

@router.get('/get')
async def get_dummy_data():

    sql = """
            SELECT * FROM example.tbl1;
          """
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    result =  {"data": [{'id': row[0], "value": row[1]} for row in rows]}
    
    return result