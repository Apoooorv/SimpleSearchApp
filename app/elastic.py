import os
import ConfigParser
from elasticsearch import Elasticsearch

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')

server = config.get('ELASTICSEARCH', 'SERVER')
port = config.get('ELASTICSEARCH', 'PORT')

es = Elasticsearch(['http://' + server + ':' + port], timeout=200)

def searchQuery(query):
	index = config.get('ELASTICSEARCH', 'INDEX')
	document = config.get('ELASTICSEARCH', 'DOCUMENT')
	body = {"size":100, "query":{"simple_query_string":{"query":query, "fields":["queryText"]}}}
	try:
		j = es.search(index=index, doc_type=document, body=body)
		return j['hits']['hits']
	except Exception, e:
		print e.message
		return []
