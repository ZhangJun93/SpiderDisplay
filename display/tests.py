from django.test import TestCase

# Create your tests here.
import mongoengine
from mongoengine import connect
#connect("zsyh_spider",host='127.0.0.1', port=27017)
connect(db="web_news",host='127.0.0.1', port=27017)

# mongoengine.register_connection("web_news", 'zsyh_spider',host='127.0.0.1', port=27017)

def print_arr(obj):
    print(obj.title)

class zsyh_spider(mongoengine.Document):
    title = mongoengine.StringField(max_length=100)
    content = mongoengine.StringField()
    url = mongoengine.StringField()
    date = mongoengine.StringField()

# test_data_list = zsyh_spider.objects(content__contains=u'上海')
# map(print_arr, test_data_list)

a = "  "
a = a.strip()
if a == '':
    print("ok")