import pymysql


def query_db_data(sql):
    connect_string = {
        'host': '192.168.2.160',
        'user': 'root',
        'password': '123456',
        'db': 'agileone',
        'port': 3306
    }
    con = pymysql.connect(**connect_string)
    cur = con.cursor()
    cur.execute(sql)
    dd = cur.fetchall()
    cur.close()
    con.close()
    return dd




if __name__ == '__main__':
    sql = 'select noticeid from notice order by noticeid desc limit 1'
    qd = query_db_data(sql)
    print(qd[0][0])
    print(type(qd[0][0]))