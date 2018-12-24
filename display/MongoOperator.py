#encoding:utf=8
import pymongo as pm
import json


class MongoOperator:
    def __init__(self, host, port, db_name, default_collection, user=None, passwd=None):
        '''
        设置mongodb的地址，端口以及默认访问的集合，后续访问中如果不指定collection，则访问这个默认的
        :param host: 地址
        :param port: 端口
        :param db_name: 数据库名字
        :param default_collection: 默认的集合
        :param user: 用户名
        :param passwd: 密码
        '''
        #建立数据库连接
        self.client = pm.MongoClient(host=host, port=port)
        #选择相应的数据库名称
        self.db = self.client.get_database(db_name)
        # 若需验证权限，则登录
        if user != None and passwd != None:
            self.db.authenticate(name=user, passwd=passwd)
        #设置默认的集合
        self.collection = self.db.get_collection(default_collection)

    def insert(self, item, collection_name = None):
        '''
        插入数据
        :param item: 需要插入的数据
        :param collection_name:  可选，需要访问哪个集合
        :return:
        '''
        if collection_name != None:
            collection = self.db.get_collection(collection_name)
            collection.insert(item)
        else:
            self.collection.insert(item)

    def find(self, expression =None, collection_name=None):
        '''
        进行查询，导出数据
        :param expression: 查询条件，可以为空
        :param collection_name: 集合名称
        :return: 所有结果
        '''
        if collection_name != None:
            collection = self.db.get_collection(collection_name)
            if expression == None:
                return collection.find()
            else:
                return collection.find(expression)
        else:
            if expression == None:
                return self.collection.find()
            else:
                return self.collection.find(expression)


if __name__ == "__main__":

    db = MongoOperator('127.0.0.1', 27017, 'test_db', 'test_collection')

    # 1：插入数据
    item = {}
    item['name'] = 'xxx'
    item['age'] = '23'
    item['date'] = '2017-01-01'
    db.insert(item)
    for item in db.find():
       pass

    # 2: 导出数据
    # 导出日期为“2017-01-01”的数据
    date = '2017-01-01'
    expression = {'date': date}
    data_set = db.find(expression)             # 若express为空，返回表中所有数据