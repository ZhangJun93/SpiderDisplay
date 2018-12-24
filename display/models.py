from django.db import models
import mongoengine
# Create your models here.
from mongoengine import connect
# connect("web_news", host='127.0.0.1', port=27017)

class NewsModel(mongoengine.Document):
    title = mongoengine.StringField(max_length=100)
    content = mongoengine.StringField()
    url = mongoengine.StringField()
    date = mongoengine.StringField()