import datetime
from pymongo import MongoClient
import requests

API_KEY = '32ae62cb563c4eed9a34b44c6c64219f'

BASE_URL = 'https://newsapi.org/v2/everything'
SOURCES = ['abc-news', 'aftenposten', 'al-jazeera-english', 'ansa', 'ars-technica', 'bbc-news', 'bbc-sport', 'bloomberg', 'business-insider', 'buzzfeed', 'cnn', 'daily-mail', 'engadget', 'espn', 'financial-times', 'fox-news', 'fox-sports', 'google-news', 'hacker-news', 'medical-news-today', 'mirror', 'national-geographic', 'techcrunch', 'the-economist', 'the-hindu', 'the-new-york-times', 'the-times-of-india', 'the-wall-street-journal']

def connectMongo():
	client = MongoClient('mongodb://127.0.0.1:27017')
	db = client['SampleSearchApp']
	return db

def call(source, date):
	url = BASE_URL + '?sources=' + source
	url += '&from=' + date + '&to=' + date
	url += '&sortBy=popularity'
	url += '&apiKey=' + API_KEY

	response = requests.get(url)
	return response.json()

def save(db, obj):
	finalObject = []
	print 'Saving articles: ' + str(len(obj['articles']))
	for element in obj['articles']:
		db.newsmodel.insert_one(element)

def main():
	print len(SOURCES)
	db = connectMongo()
	startdate = '2018-02-01'
	enddate = '2018-02-28'

	startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
	enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d').date()
	date = startdate

	finalObject = []

	while date <= enddate:
		datestring = date.strftime('%Y-%m-%d')
		print 'Saving for date: ' + datestring
		print datestring
		for element in SOURCES:
			try:
				response = call(element, datestring)
				save(db, response)
			except Exception, e:
				print e.message
		date += datetime.timedelta(days=1)
	
if __name__ == '__main__':
	main()

# https://newsapi.org/v2/everything?sources=abc-news&from=2018-02-01&to=2018-02-28&sortBy=popularity&apiKey=32ae62cb563c4eed9a34b44c6c64219f