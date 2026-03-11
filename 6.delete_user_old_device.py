import pymysql
import mysql.connector

# 连接数据库
db = mysql.connector.connect(
    host="drdsfacbm800jknqpublic.drds.aliyuncs.com",
    user="qimao_all_test",
    password="P3LTGTCgHgvzt1ol",
    database="qimao_free",
)


def Delete_From():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL语句更新数据
    sql_1 = """truncate table user_old_device"""
    sql_2 = """truncate table user_old_device_extend"""

    try:
        # 执行SQL语句
        cursor.execute(sql_1)
        # 提交到数据库执行
        db.commit()
        print("删除user_old_device数据成功")
        cursor.execute(sql_2)
        db.commit()
        print("删除user_old_device_extend数据成功")

    except Exception as e:
        print("删除数据失败：case%s" %e)
        # 发生错误时回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()


def main():
    Delete_From()


# 删除测试环境所有老设备
if __name__ == '__main__':
    main()