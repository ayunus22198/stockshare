from flask import Flask 
import requests
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return 'INDEX'


@app.route('/news/tesla')
def tesla():
	tesla_stock_news = requests.get('https://newsapi.org/v2/everything?apiKey=ed59b5bda9904333b6f127e4498d9c7f&q=tesla&from=2020-04-30&to=2020-05-29&pageSize=20', timeout=60)
	return jsonify(tesla_stock_news.text)


@app.route('/news/amazon')
def amazon():
	amazon_stock_news = requests.get('https://newsapi.org/v2/everything?apiKey=ed59b5bda9904333b6f127e4498d9c7f&q=amazon&from=2020-04-30&to=2020-05-29&pageSize=20', timeout=60)
	return jsonify(amazon_stock_news.text)



@app.route('/news/apple')
def apple():
	apple_stock_news = requests.get('https://newsapi.org/v2/everything?apiKey=ed59b5bda9904333b6f127e4498d9c7f&q=apple&from=2020-04-30&to=2020-05-29&pageSize=20', timeout=60)
	return jsonify(apple_stock_news.text)


@app.route('/news/microsoft')
def microsoft():
	microsoft_stock_news = requests.get('https://newsapi.org/v2/everything?apiKey=ed59b5bda9904333b6f127e4498d9c7f&q=microsoft&from=2020-04-30&to=2020-05-29&pageSize=20', timeout=60)
	return jsonify(microsoft_stock_news.text)



if __name__ == '__main__':
	app.run(debug = True)

