#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/26 7:00 下午
# @Filename : comment_script.py
# @Author : Liulu
# 用于查询用户的评论信息


import sys
import os
import json
import time



curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from utils import dbHelper
from utils import MoHelper
from utils import RedisHelper


month_time = time.strftime('%Y%m', time.localtime(time.time()))

def connect_mysql():
    host = "rm-uf6b86e0rc52d5k9iqo.mysql.rds.aliyuncs.com"
    user = "free_testuser"
    password = "fr5Bo7kTetuK"
    db = "free_comment"
    con_mysql = dbHelper.MySQLHandel(host, user, password, db)
    return con_mysql


def connect_mongo(db_name, tb_name):
    host = "mongodb://root:bhjcEfe6nB3666xJvxE@dds-uf6d8ab76ea102441317-pub.mongodb.rds.aliyuncs.com:3717"
    con_mongo = MoHelper.Mongo(host, db_name, tb_name)
    return con_mongo


def connect_redis():
    redis_config = {
        "host": "free-test.redis.rds.aliyuncs.com",
        "port": 6379,
        "password": "jOub9uga3sun2miK"
    }
    con_redis = RedisHelper.RedisClass(redis_config, db=9)
    return con_redis


def mod(num1, num2):
    return num1 % num2

uc_mongo = connect_mongo(db_name='free_book_coin_detail_data', tb_name='coin_detail_20220804')
mon_query = {"type" : 153}
res_4 = uc_mongo.search_by_find(mon_query)
print(res_4)

def comment_data_verify(*args):
    """
    发表评论数据入库校验
    :param args: book_id,uid,comment_id   约定传参的格式 可根据传参任意修改sql语句
    :return:
    """
    comment_mysql = connect_mysql()
    content_mongo = connect_mongo(db_name='comment', tb_name='content')
    uc_tb_name = f'user_active_comment_{args[1] % 128}'
    uc_mongo = connect_mongo(db_name='free_comment_user', tb_name=uc_tb_name)
    # book_comment_xx 评论表
    # sql_1 = f'select * from book_comment_{args[0] % 128} where book_id={args[0]} and uid={args[1]} and id={args[2]}'
    sql_1 = f'select * from book_comment_{args[0] % 128} where book_id={args[0]} and uid={args[1]}'
    res_1 = comment_mysql.query_all(sql_1)
    # print(type(res_1[0]))
    print(f'------------------------- book_comment_{args[0] % 128} 表的数据信息如下：------------------------- \n')
    # print(res_1)
    print(json.dumps(res_1[0], ensure_ascii=False))
    print('\n')
    content_id = res_1[0]['content_id']
    # comment_audit_ 审核表
    sql_2 = f'select * from comment_audit_{month_time} where book_id={args[0]} and uid={args[1]} and comment_id={args[2]}'
    res_2 = comment_mysql.query_all(sql_2)
    print(f'------------------------- comment_audit_{month_time}表的数据如下：------------------------- \n')
    print(json.dumps(res_2, ensure_ascii=False))
    print('\n')
    # comment/content  内容存储表
    res_3 = content_mongo.search_by_ObjectId(content_id)
    print(f'------------------------- content表的数据信息如下：-------------------------\n')
    print({res_3["content"]})
    print('\n')
    # free_comment_user/user_active_comment_%d  记录用户个人发表的评论数据
    mon_query = {"user_id": args[1], "book_id": args[0], "comment_id": args[2]}
    res_4 = uc_mongo.search_find_one(mon_query)
    print(f'------------------------- user_active_comment表的数据信息如下: ------------------------- \n')
    print(json.dumps(res_4, default=str, ensure_ascii=False))
    comment_mysql.close()


def comment_reply_verify(*args):
    """
    发表回复数据入库校验
    :param args: book_id,uid,comment_id ,reply_id  可根据传参任意修改sql语句
    :return:
    """
    comment_mysql = connect_mysql()
    content_mongo = connect_mongo(db_name='comment', tb_name='content')
    # comment_reply_ 回复表
    sql_1 = f'select * from comment_reply_{args[2] % 256} where book_id={args[0]} and uid={args[1]} and id={args[3]}'
    # sql_1 = f'select * from comment_reply_{args[2] % 256} where book_id={args[0]} and uid={args[1]}'
    res_1 = comment_mysql.query_one(sql_1)
    # res_1 = comment_mysql.query_one(sql_1)
    res_1 = json.loads(res_1)
    content_id = res_1['content_id']
    print(f'------------------------- comment_reply_{args[2] % 256} 的数据信息如下：-------------------------')
    print(res_1)
    print('\n')
    # comment_audit_ 评论审核表
    sql_2 = f'select * from comment_audit_{month_time} where book_id={args[0]} and uid={args[1]} and comment_reply_id={args[3]}'
    res_2 = comment_mysql.query_one(sql_2)
    print(f'------------------------- comment_audit表 的数据信息如下：-------------------------')
    print(res_2)
    print('\n')
    # comment/content  内容存储表
    res_3 = content_mongo.search_by_ObjectId(content_id)
    print(f'------------------------- content表的数据信息如下：------------------------- \n')
    print({res_3["content"]})
    comment_mysql.close()


def like_data_verify(*args):
    """
    点赞数据入库校验
    :param args:
    :return:
    """
    pass


def topic_data_verify(*args):
    """
    发表话题数据入库校验
    :param args: id(topic_id) 、uid 、book_id
    :return:
    """
    comment_mysql = connect_mysql()
    content_mongo = connect_mongo(db_name='comment', tb_name='content')
    uc_tb_name = f'user_active_comment_{args[1] % 128}'
    uc_mongo = connect_mongo(db_name='free_comment_user', tb_name=uc_tb_name)
    #  topic  话题表
    sql_1 = f'select * from topic where id={args[0]}'
    res1 = comment_mysql.query_one(sql_1)
    print(f' ------------------------- topic 表的数据信息如下：------------------------- \n')
    print(res1)
    print('\n')
    # topic_comment_  推书评论表
    # 一般操作多于查最新发布的一条，所以先sql语句先写死查该话题下最新发布的一条评论
    sql_2 = f'select * from topic_comment_{args[0] % 64} where topic_id={args[0]} and comment_uid={args[1]} and book_id={args[2]} order by id desc limit 1'
    res2 = comment_mysql.query_one(sql_2)
    print(f' ------------------------- topic_comment_{args[0] % 64} 表的的数据信息如下：------------------------- \n')
    print(res2)
    print('\n')
    res2 = json.loads(res2)
    comment_id = res2['comment_id']
    content_id = res2['content_id']
    sql_3 = f'select * from book_comment_{args[2] % 128} where  id={comment_id}'
    res3 = comment_mysql.query_one(sql_3)
    print(f'------------------------- book_comment_{args[2] % 128} 表的数据信息如下：------------------------- \n')
    print(res3)
    print('\n')
    # comment_audit_ 审核表
    sql_4 = f'select * from comment_audit_{month_time} where book_id={args[2]} and uid={args[1]} and comment_id={comment_id}'
    res4 = comment_mysql.query_one(sql_4)
    print(f'------------------------- comment_audit_{month_time}的数据信息如下：------------------------- \n')
    print(res4)
    print('\n')
    # comment/content  内容存储表
    res_5 = content_mongo.search_by_ObjectId(content_id)
    print(f'------------------------- content 表的数据信息如下：------------------------- \n')
    print({res_5["content"]})
    print('\n')
    # free_comment_user/user_active_comment_%d  记录用户个人发表的评论数据
    mon_query = {"user_id": args[1], "book_id": args[2], "comment_id": comment_id}
    res_6 = uc_mongo.search_find_one(mon_query)
    print(f'------------------------- user_active_comment表的数据信息如下: -------------------------\n')
    print(res_6)
    comment_mysql.close()


# if __name__ == '__main__':
    # 传入 book_id,uid,comment_id
    # comment_data_verify(209718, 505124208, 288949)

    # 传入 book_id,uid,comment_id ,reply_id
    # comment_reply_verify(150539, 503804011, 278283, 2697)

    # id(topic_id) 、uid 、book_id
    # topic_data_verify(2588, 503804011, 150993)
