import os
import ConfigParser
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')

def connectMongo():
	server = config.get('MONGODB', 'SERVER')
	port = config.get('MONGODB', 'PORT')
	
	url = 'mongodb://' + server + ':' + port
	client = MongoClient(url)
	return client

def searchDoc(docid):
	client = connectMongo()
	database = config.get('MONGODB', 'DATABASE')
	model = config.get('MONGODB', 'MODEL')

	db = client[database]
	document = db.newsmodel.find_one({'_id':ObjectId(docid)})
	# print document
	client.close()
	return document
