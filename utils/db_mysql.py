# coding=utf-8

import pymysql


class OpMySql( object ):
    def __init__(self, host, user, password, db, port=3306, charset='utf8'):  # 必填参要放在默认参前面
        schema = {
            'user': user,
            'host': host,
            'password': password,
            'db': db,
            'port': port,
            'charset': charset
        }
        try:
            self.conn = pymysql.connect( **schema )
        except Exception as e:
            print( '数据库连接异常！%s' % e )
            quit( '数据库连接异常！%s' % e )
        else:  # 没有出异常的情况下，建立游标
            self.cur = self.conn.cursor( cursor=pymysql.cursors.DictCursor )

    def execute(self, sql):
        try:
            self.cur.execute( sql )
        except Exception as e:
            print( 'sql语句有错误%s' % e )
            return e
        if sql[:6].upper() == 'SELECT':
            return self.cur.fetchall()
        else:  # 其他sql语句commit一下
            self.conn.commit()
            return 'OK'

    def __del__(self):
        self.conn.close()
        # self.cur.close()
        # self.conn.close()


db = OpMySql( 'localhost', 'root', 'root', db='test')
# print(mpp.execute('select * from stu;'))
